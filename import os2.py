import os

def check_folders(root_dir):
    missing_files = []
    
    # 遍历根目录下的所有子文件夹
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # 跳过根目录本身
        if dirpath == root_dir:
            continue
            
        # 检查是否包含目标文件
        if "full - 副本.md" not in filenames:
            missing_files.append(dirpath)
    
    return missing_files

def save_results(missing_folders, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for folder in missing_folders:
            f.write(folder + '\n')

if __name__ == "__main__":
    # 设置根目录为当前文件夹
    root_directory = os.getcwd()
    
    # 检查文件夹
    result = check_folders(root_directory)
    
    # 保存结果
    save_results(result, "missing_files.txt")
    
    print(f"检查完成，结果已保存到 missing_files.txt")