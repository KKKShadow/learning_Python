

# -*- coding: UTF-8 -*-
def chagne_number( b ):
    print('函数中一开始 b 的值：{}' .format( b ) )
    b = 1000
    print('函数中 b 赋值后的值：{}' .format( b ) )


b = 1
chagne_number( b )# 只是传递了 b 的值，没有改变 b 的值
print( '最后输出 b 的值：{}' .format( b )  )


def chagne_list( b ):
    print('函数中一开始 b 的值：{}' .format( b ) )
    b.append(1000)
    print('函数中 b 赋值后的值：{}' .format( b ) )


b = [1,2,3,4,5]
chagne_list( b )
print( '最后输出 b 的值：{}' .format( b )  )
