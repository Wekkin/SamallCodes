#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 今日头条 小视频下载器

import json
import requests
import time
import re
import os
import platform
import base64
isIOS=False
filename_add_datetime=True # True：保存文件名前添加发布日期及时间；False：不添加
watermark='0'
if 'Darwin' in platform.system():
	isIOS=True
	import appex, clipboard

outpath='头条'	# 视频将会保存到脚本所在文件夹下的 头条 文件夹内
outpath=os.path.join(os.getcwd(),outpath)
if not os.path.exists(outpath):
	os.mkdir(outpath)
outDir=''

#uid='50561077107'
#vid='v020161b0000bgeei8smavfbcbpe0e0g'
headers_dl={
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-cn',
	#'User-Agent': 'News/6.9.8.36 CFNetwork/758.5.3 Darwin/15.6.0',
	'User-Agent': "News 7.2.2 rv:7.2.2.15 (iPhone; iOS 10.3.3; zh_CN)",
}
def replaceSpecialString(string,repalceString=''):
	#替换删除文件名中的特殊字符，返回可作为文件名的字符串
	specialString=r'\/:*?"<>|'
	for s in specialString:
		string=string.replace(s,'')
	return string
	
def Downloader(url,outDir,filename=None,headers=None,stream=True):	# 文件下载 stream=True 不立即下载文件到内存，防止文件过大，内存不足
	import requests,os
	retry=0
	while True:
		if retry!=3:
			res=requests.get(url,headers=headers,stream=stream)
			filesize=int(res.headers['Content-Length'])
			if not filename and 'Content-Disposition' in res.headers:
				import re
				#input(res.headers['Content-Disposition'])
				m_filename=re.findall('(?<=filename=")[^"]+',res.headers['Content-Disposition'])
				if m_filename:
					filename=m_filename[0]
				else:
					filename='file'
			outfile_path=os.path.join(outDir,filename)
				#Content-Disposition: attachment; filename="635924308942-blobs-all.zip"
			if res.status_code==200:
				print('正在下载:')
				with open(outfile_path,'wb') as f_out:
					print('\t'+url)					
					for chunk in res.iter_content(chunk_size=512):	# 一块一块的下载内容
						if chunk:
							f_out.write(chunk)
					
					try:
						print('\t',outfile_path)
					except UnicodeEncodeError:
						print('\t特殊字符无法显示！')
					f_out.close()
				if(os.path.getsize(outfile_path)==filesize):
					print('\t下载完成。')
					return outfile_path
				else:
					retry+=1
					print('\t文件大小错误，开始第 %s 次重试。' % retry)
			else:
				print('\t错误：%s' % res.status_code)
				print('\t开始第 %s 次重试。' % retry)
		else:
			print('\t下载失败！')
			return False

def make_outDir(user,uid): # 创建以用户名为名称的下载保存用文件夹
	user=replaceSpecialString(user)
	if user[0]=='.':
		user='。'+user[1:] #替换用户名前面的点号，防止文件夹隐藏
	global outDir
	outDir=os.path.join(outpath,user)
	if not os.path.exists(outDir):
		os.mkdir(outDir)
	f=open(os.path.join(outDir,uid+'.txt'),'w',encoding='utf-8')
	f.write(uid)
	f.close()
	return outDir
	
def prepare(video,category=''): # 下载准备
	#input(json.dumps(video,indent=4,ensure_ascii=False))
	global watermark
	if category=='profile_short_video': # 小视频
		item_id=video['raw_data']['item_id']
		vid=video['raw_data']['video']['video_id']
		
		#dlink=get_dlink(video_list)
		dlink='https://aweme.snssdk.com/aweme/v1/play/?video_id='+vid+'&ratio=720p&watermark='+watermark+'&line=0'
		title=video['raw_data']['title']
		playerCount=video['raw_data']['action']['play_count']
		timeStamp = video['raw_data']['create_time']
		durations=video['raw_data']['video']['duration']    # 11	
	else: # 视频
		item_id=str(video['item_id'])
		vid=video['video_detail_info']['video_id']
		if category=='':
			dlink='https://aweme.snssdk.com/aweme/v1/play/?video_id='+vid+'&ratio=720p&watermark='+watermark+'&line=0'
		else:
			if 'video_play_info' in video:
				video_list=json.loads(video['video_play_info'])['video_list']
			else:
				# 此方法获取的视频链接，对应的视频是结果加密的，暂时无法解密
				play_auth_token=video['play_auth_token']
				play_auth_token,play_token=get_tokens(vid,item_id)
				info=get_playInfo(vid,item_id,play_auth_token,play_token)
				video_list=info['video_info']['data']['video_list']
			dlink=get_dlink(video_list)
		title=video['title']
		playerCount=video['video_detail_info']['video_watch_count']
		timeStamp = video['publish_time']
		durations=video['video_duration']    # 11	
	#input(item_id)
	fn=make_fileName(vid,title,timeStamp)
	print(title)
	global headers_dl
	Downloader(dlink,outDir,fn,headers=headers_dl)
	
def get_playInfo(vid,item_id,play_auth_token,play_token): # 获取视频播放信息
	url='https://ic.snssdk.com/video/openapi/v1/?action=get_playInfo&item_id='+item_id+'&ptoken='+play_token+'&video_id='+vid
	header={"Accept-Encoding": "gzip, deflate","Authorization": play_auth_token,"User-Agent": "News 7.2.2 rv:7.2.2.15 (iPhone; iOS 10.3.3; zh_CN)",}
	req=requests.get(url,headers=header)
	info=json.loads(req.text)
	#input(json.dumps(info,indent=4,ensure_ascii=False))
	return info

def get_tokens(vid,item_id): # 获取授权码
	url='https://learning.snssdk.com/toutiao/v1/play_info/?item_id='+item_id+'&resource_id='+vid #+'resolution='+'750%2A1334'
	header={"Accept-Encoding": "gzip, deflate","User-Agent": "News 7.2.2 rv:7.2.2.15 (iPhone; iOS 10.3.3; zh_CN)",}
	req=requests.get(url,headers=header)
	info=json.loads(req.text)
	#input(json.dumps(info,indent=4,ensure_ascii=False))
	play_auth_token=info['data']['play_info']['play_auth_token']
	play_token=info['data']['play_info']['play_token']
	return play_auth_token,play_token

def get_dlink(video_list,definition=0): # 挑选视频直链
	dlink=''
	for k in video_list:
		v=video_list[k]
		d=v['definition']
		if definition!=0 and d==definition:
			dlink=base64.b64decode(v['main_url'].encode()).decode()
			break
		elif int(d.replace('p',''))>definition:
			definition=int(d.replace('p',''))
			dlink=base64.b64decode(v['main_url'].encode()).decode()
	return dlink	

def make_fileName(vid,title,timeStamp): # 生成文件名
	if title=='':
		title=vid
	title=replaceSpecialString(title)
	fn=title+'.mp4'
	global filename_add_datetime
	if filename_add_datetime:
		fn=time.strftime("%Y%m%d-%H%M%S",time.localtime(timeStamp))+'_'+fn
	return fn

def get_vid(url,category,downloadAll=False):
	#url='https://m.toutiaoimg.cn/group/6638189833363652611/?iid=55270774713&app=news_article&timestamp=1545610947'
	print('正在解析。。。')
	if '/group/' in url:
		item_id=url.split('/group/')[1].split('/')[0]
	elif '/item/' in url:
		item_id=url.split('/item/')[1].split('/')[0]
	url='https://a6.pstatp.com/article/full/23/2/%s/%s/0/0/0/0/' %(item_id,item_id)
	header={"Accept": "application/json","Accept-Encoding": "gzip, deflate","Content-Type": "application/json; encoding=utf-8","User-Agent": "News 7.2.2 rv:7.2.2.15 (iPhone; iOS 10.3.3; zh_CN)",}
	#url='https://learning.snssdk.com/toutiao/v1/item_info/?'+rerferer.split('?')[1]
	req=requests.get(url,headers=header)
	info=json.loads(req.text)
	#input(json.dumps(info,indent=4,ensure_ascii=False))
	video=info['data']
	vid=''
	if info['message']=='success':
		user=video['media_name']
		uid=str(video['media_user_id'])
		outDir=make_outDir(user,uid)
		vid=video['video_detail_info']['video_id']
		#input(vid)
		if video['group_source'] in [19,21]:
			_category='profile_short_video'
		elif video['group_source']==30:
			_category='profile_video'
		else:
			_category='profile_video'
			#print(json.dumps(info,indent=4,ensure_ascii=False))
			print('意料之外的group_source：'+str(video['group_source']))
		#prepare(video)
		if not downloadAll:
			if _category=='profile_short_video':
				input('测试')
				prepare(video) # 此方法获取的视频链接，对应的视频是结果加密的，暂时无法解密
			else:
				get_videoList(uid,_category,_vid=vid)
		else:
			get_videoList(uid,category)
		
	else:
		print('解析出错:'+req.text)

def get_videoList(uid,category,offset=0,_vid=0):
	url='https://ic.snssdk.com/api/feed/profile/v1/'
	params={
		"visited_uid":uid,
		"media_id":uid,
		"client_extra_params":'{"playparam":"codec_type:0"}',
		"count":"20",
		"offset":str(offset),
		"stream_api_version":"88",
		#"category":"profile_video",
		"category":category,
		"version_code":"7.2.2",
		"app_name":"news_article",
		"channel":"App Store",
		"resolution":"750*1334", #
		"os_version":"10.3.3",
		"device_platform":"iphone",
		"device_type":"iPhone 6s"
	}
	headers={
		"Cookie": "install_id=72222682462;", #
		"User-Agent": "News 7.2.2 rv:7.2.2.15 (iPhone; iOS 10.3.3; zh_CN)",
		"Accept-Encoding": "gzip, deflate",
	}
	req=requests.get(url,headers=headers,params=params)
	content=req.text
	#input('test:'+content)
	data=json.loads(content)
	offset=data['offset']
	isFinish=False
	count=len(data['data'])
	for i in range(count):
		video=json.loads(data['data'][i]['content'])
		#input(json.dumps(video,indent=4,ensure_ascii=False))
		if category=='profile_short_video': # 小视频
			vid=video['raw_data']['video']['video_id']
		else:
			vid=video['video_detail_info']['video_id']
		if _vid!=0:
			if _vid	==vid:
				prepare(video,category)
				isFinish=True
				break
			else:
				continue
		else:
			prepare(video,category)
		#print(json.dumps(video,indent=4,ensure_ascii=False))
		
	if isFinish==False and count==20:
		get_videoList(uid,category,offset,_vid)
	else:
		print('全部下载完成！')

def main():
	# 三种入口方式
	url=None
	if isIOS:
		if appex.is_running_extension() and re.findall(r'https?://\S+',appex.get_text()):
			url = re.findall(r'https?://\S+',appex.get_text())[0]
		else:
			m = re.findall(r'https?://\S+',clipboard.get())
			if m:
				url = re.findall(r'https?://\S+',clipboard.get())[0]
		
	while not url:
		url=input('请输入链接：')
		url=re.findall(r'https?://\S+',url)
		if not url:
			print('无效的链接')
		else:
			url=url[0]
	print(url)
	#url='https://m.toutiaoimg.cn/group/6638189833363652611/?iid=55270774713&app=news_article&timestamp=1545610947'
	#url='https://toutiao.com/group/6634462754390409735/?app=news_article_social&timestamp=1557286048&req_id=20190508112728010152047045191470D&group_id=6634462754390409735'
	#https://toutiao.com/group/6627990133436058884/
	print('直接回车：仅下载当前链接视频\n输入 1：下载该用户所有 小视频\n输入 2：下载该用户所有 视频')
	s=input()
	downloadAll=False
	category=''
	if s=='1':
		downloadAll=True
		category='profile_short_video'
	elif s=='2':
		downloadAll=True
		category='profile_video'
		
	#"category":"profile_video",
		#"category":"profile_short_video",
	print(category)
	get_vid(url,category,downloadAll)

main()
#get_videoList(uid)
