import os
import shutil

def search_and_move_files(source_folder, target_folder, extensions):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = file.split(".")[-1]
            if file_extension in extensions:
                target_path = os.path.join(target_folder, file)
                shutil.move(file_path, target_path)

source_folder = "D:\\邓伟清\\D盘\\技术部邓伟清\\08临时存放\\工作微信文件缓存\\新建文件夹"  # 替换为你要搜索的文件夹路径
target_folder = "D:\\邓伟清\\D盘\\技术部邓伟清\\08临时存放\\工作微信文件缓存\\文件"  # 替换为你要将文件移动到的目标文件夹路径
extensions = ["xlsx", "pdf", "docx", "pptx", "doc", "PDF" ,"xls"]  # 要搜索的文件扩展名列表

search_and_move_files(source_folder, target_folder, extensions)