# coding=utf-8
import os
import shutil

basepath = os.getcwd()
inputpath = basepath + "\input"
outputpath = basepath + "\output"

# 情空输出文件夹
shutil.rmtree(outputpath)
# 创建新的输出文件夹
os.makedirs(outputpath)

# 开始处理图片
for filename in os.listdir(inputpath):
    # 只处理jpg文件
    if os.path.splitext(filename)[1] == '.jpg':
        output = os.popen('jpegtran.exe -copy none -optimize -progressive -outfile %s %s' % (
        outputpath + '\\' + filename, inputpath + '\\' + filename))
        print(output.read())

#打开输出文件夹
os.system("explorer.exe %s" % outputpath)