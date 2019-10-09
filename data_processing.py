"""处理多级文件夹，可以考虑先返回文件或者文件夹列表的方式"""
import os
import shutil
source_a = "/mnt/sdb/extract_ILSVRC2012/val"
source_b = "/mnt/sdb/extract_ILSVRC2012/test"
data_a = os.listdir(source_a)
data_b = os.listdir(source_b)
"""
listdir可以用老返回某一文件夹下的子文件目录，返回的是一个无序的列表。如果要排序，将得到是我列表如a
a.sort()就是一个有序的列表"""
data_a.sort()
data_b.sort()
if not os.path.exists("/mnt/sdb/extract_ILSVRC2012/validation"):
    os.mkdir("/mnt/sdb/extract_ILSVRC2012/validation")
newpath = "/mnt/sdb/extract_ILSVRC2012/validation"

for i in range(len(data_a)):
    for derName, subfolders, filenames in os.walk(source_a+"/"+data_a[i]):
        for j in range(len(filenames)):
            filepath_a = derName+"/"+filenames[j]
            if not os.path.exists(newpath+"/"+data_a[i]):
                os.mkdir(newpath+"/"+data_a[i])
            newpath_validation = os.path.join(newpath, data_a[i], filenames[j])
            shutil.copy(filepath_a, newpath_validation)

    for derName, subfolders, filenames in os.walk(source_b+"/"+data_b[i]):
        for j in range(len(filenames)):
            filepath_b = derName+"/"+filenames[j]
            newpath_validation = newpath+"/"+data_a[i]+"/"+filenames[j]
            shutil.copy(filepath_b, newpath_validation)