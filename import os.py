import os
import pandas as pd

# 获取当前文件夹路径
current_dir = os.getcwd()

# 初始化表格数据
data = []

# 遍历当前文件夹下的所有子文件夹
for subdir in os.listdir(current_dir):
    subdir_path = os.path.join(current_dir, subdir)
    if os.path.isdir(subdir_path):
        # 构建full.md文件路径
        full_md_path = os.path.join(subdir_path, 'full.md')
        
        # 检查文件是否存在
        if os.path.exists(full_md_path):
            # 读取文件的前四行
            with open(full_md_path, 'r', encoding='utf-8') as file:
                lines = [file.readline().strip() for _ in range(4)]
            
            # 将数据添加到表格中
            data.append([subdir_path] + lines)

# 创建DataFrame
columns = ['子文件夹路径', '第一行', '第二行', '第三行', '第四行']
df = pd.DataFrame(data, columns=columns)

# # 输出表格
# print(df)

# 将DataFrame保存为txt文件
df.to_csv('output.txt', sep='\t', index=False, encoding='utf-8')

# 输出提示信息
print("表格已保存为output.txt")