import os
import shutil

def search_and_copy_files(source_folder, target_folder, extensions):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = file.split(".")[-1]
            if file_extension in extensions:
                target_path = os.path.join(target_folder, file)
                shutil.copy(file_path, target_path)

source_folder = "D:\\D盘\\WXWork"  # 替换为你要搜索的文件夹路径
target_folder = "D:\\D盘\\WXWork\\提取文件"  # 替换为你要将文件复制到的目标文件夹路径
extensions = ["xlsx", "pdf", "docx", "pptx", "doc", "PDF" ,"xls"]  # 要搜索的文件扩展名列表

search_and_copy_files(source_folder, target_folder, extensions)
for file in found_files:
    print(file)