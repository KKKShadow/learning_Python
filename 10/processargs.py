#导入进程包
# 使用进程类创建进程对象
# 启动进程执行制定任务

import time
import multiprocessing

def sing(num ,name):
    for i in range(num):
        print(name,'Singing...', i)
        time.sleep(0.1)

def dance(num ,name):
    for i in range(num):
        print(name,'Dancing...', i)
        time.sleep(0.1)


if __name__ == '__main__':

    # target 指定函数名 
    #  args 传递参数 用元组()方式
    #  元组的元素顺序要和函数的参数顺序一致
    # kwargs 传递参数 用字典{}方式
    # 字典的key要和函数的参数名一致
    time.sleep(1)
    print('multiprocess')
    singprocess = multiprocessing.Process(target=sing,args=(5,'小明'))
    danceprocess = multiprocessing.Process(target=dance,kwargs={'name':'妹妹','num':2})

    singprocess.start()
    danceprocess.start()