import os

path = r'E:\仙尊归来当赘婿'
files = os.listdir(path)

# 遍历所有文件
for file in files:
    # 构造旧文件名（包含路径）
    old_name = os.path.join(path, file)
    # print(file.rfind('第'))
    # print(file.find('集'))
    # name = file[file.rfind('第') + 1:file.find('集')]
    name = file.split(".")[0]
    type = file.split(".")[1]
    if type != 'mp4':
        continue
    # 构造新文件名
    new_name = os.path.join(path, '【知秋剧场】《仙尊归来当赘婿》EP' + name + ' #赘婿 #仙侠 #大陆 #言情.' + type)
    print(new_name)
    # 重命名文件
    os.rename(old_name, new_name)
