import os
import glob

def search_files(folder_path, extensions):
    result = []
    for root, dirs, files in os.walk(folder_path):
        for extension in extensions:
            search_pattern = os.path.join(root, f"*.{extension}")
            file_list = glob.glob(search_pattern)
            result.extend(file_list)
    return result

folder_path = "D:\\邓伟清\\D盘\\WXWork"  # 替换为你要搜索的文件夹路径
extensions = ["xlsx", "pdf", "docx", "pptx"]  # 要搜索的文件扩展名列表

found_files = search_files(folder_path, extensions)
for file in found_files:
    print(file)