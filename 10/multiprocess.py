#导入进程包
# 使用进程类创建进程对象
# 启动进程执行制定任务

import time
import multiprocessing

def sing():
    for i in range(3):
        print('Singing...', i)
        time.sleep(0.5)

def dance():
    for i in range(3):
        print('Dancing...', i)
        time.sleep(0.5)


if __name__ == '__main__':
    sing()
    dance()
    # target 指定函数名 
    time.sleep(1)
    print('multiprocess')
    singprocess = multiprocessing.Process(target=sing)
    danceprocess = multiprocessing.Process(target=dance)

    singprocess.start()
    danceprocess.start()