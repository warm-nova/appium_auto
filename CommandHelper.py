#命令辅助方式
import os
import time

#文件夹是否存在,不存在的话则创建
def procdir(dirname):
    if os.path.exists(dirname) == False:
        os.mkdir(dirname)



