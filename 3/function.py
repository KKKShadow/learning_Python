
# -*- coding: UTF-8 -*-
def sum(num1,num2):
	"两数之和"  # 函数文档字符串  （用于存放函数说明）
	return num1+num2

print(sum(5,6))



def sum(num1,num2):
	# 两数之和
	if not (isinstance (num1,(int ,float)) and isinstance (num2,(int ,float))):
		raise TypeError('参数类型错误')
	return num1+num2

print(sum(1,2.0))


def division(num1, num2):
    # 求商与余数
    a = num1 % num2
    b = (num1 - a) / num2
    c = num1 // num2
    return b, a


num1 , num2 = division(9,4)
tuple1 = division(9,4)

print (num1,num2)
print (tuple1[1])

# **只有在形参表末尾的那些参数可以有默认参数值**
def print_user_info( name , age , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return

# 调用 print_user_info 函数

print_user_info( '两点水' , 18 , '女')
print_user_info( '三点水' , 25 )

# 可以通过参数名来给函数传递参数，而不用关心参数列表定义时的顺序，这被称之为关键字参数。
print_user_info( name = '两点水' ,age = 18 , sex = '女')
print_user_info( name = '两点水' ,sex = '女', age = 18 )

_no_value =object()

def print_info( a , b = _no_value ):
    if b is _no_value :
        print('b 没有赋值')
    else:
        print('b = ' , b)
    return
print_info(1)
print_info(1,2)
print('clear')

# 这里的 `object` 是 python 中所有类的基类。 你可以创建 `object` 类的实例，但是这些实例没什么实际用处，
# 因为它并没有任何有用的方法， 也没有任何实例数据(因为它没有任何的实例字典，你甚至都不能设置任何属性值)。 
# 你唯一能做的就是测试同一性。也正好利用这个特性，来判断是否有值输入。

# 位置参数、默认参数、可变参数和关键字参数
def print_user_info( name ,  age  , sex = '男' , * hobby):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print('爱好：{}'.format(hobby))
    return;

# 调用 print_user_info 函数
print_user_info( '两点水' ,18 , '女', '打篮球','打羽毛球','跑步')
print_user_info( '三点水' ,25 , '男', '画画','游泳')


# 支持关键字参数   hobby成了dict
def print_user_info( name ,  age  , sex = '男' , ** hobby ):  
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print('爱好：{}'.format(hobby))
    return;

# 调用 print_user_info 函数
print_user_info( name = '两点水' , age = 18 , sex = '女', hobby = ('打篮球','打羽毛球','跑步'))




def print_user_info( name , *, age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return;

# 调用 print_user_info 函数
print_user_info( name = '两点水' ,age = 18 , sex = '女' )

# 这种写法会报错，因为 age ，sex 这两个参数强制使用关键字参数
#print_user_info( '两点水' , 18 , '女' )
print_user_info('两点水',age='22',sex='男')