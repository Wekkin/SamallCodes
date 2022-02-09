# 根据配置好的文件，搜索文件夹
import os
import io
import sys
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding='utf8')  # 处理vscode打印中文乱码问题
# 主函数
baseDir = "D:\\WXWork\\1688854610278740\\Cache\\Image\\2022-02"  # 搜索的根目录
notSearchFolderArr = ['node_modules']  # 不搜索的目录
searchFileTypeArr = ['.png']  # 搜索的文件类型


def searhMain():
    allResArr = searchFolder(baseDir)
    print('\n'.join(allResArr))


# 搜索一个文件目录 传入一个文件目录路径
def searchFolder(folderPath):
    folderName = os.path.split(folderPath)[-1]
    searFilePathArr = []
    if os.path.exists(folderPath) and (folderName not in notSearchFolderArr):  # 判断路径是有效文件夹
        fileArr = os.listdir(folderPath)  # 获取文件夹下的所有内容(文件和文件夹)
        for item in fileArr:
            currentPath = folderPath+'\\'+item
            (fileName, fileType) = os.path.splitext(item)
            if os.path.isfile(currentPath) and (fileType in searchFileTypeArr):  # 处理文件
                searFilePathArr.append(currentPath)

            if os.path.isdir(currentPath) and (item not in notSearchFolderArr):  # 处理文件夹
                innerFileArr = searchFolder(currentPath)  # 递归搜索
                searFilePathArr.extend(innerFileArr)

    return searFilePathArr


searhMain()
