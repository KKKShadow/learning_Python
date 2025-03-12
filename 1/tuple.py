#-*-coding:utf-8-*-
list1=[123,456]
tuple1=('两点水','twowater','liangdianshui',list1)
print(tuple1)
list1[0]=789
list1[1]=100
print(tuple1)


tuple2=('两点水','twowter','liangdianshui',[123,456])
print(tuple2)
del tuple2
# print(tuple2)    #报错：NameError: name 'tuple2' is not defined  删除了整个元组

name1 = ('一点水', '两点水', '三点水', '四点水', '五点水')

name2 = ('5点水', '2点水', '3点水', '1点水', '4点水')

list1 = [1, 2, 3, 4, 5]

# 计算元素个数
print(len(name1))
# 连接,两个元组相加
print(name1 + name2)
# 复制元组
print(name1 * 2)
# 元素是否存在 (name1 这个元组中是否含有一点水这个元素)
print('一点水' in name1)
# 元素的最大值
print(max(name2))
# 元素的最小值
print(min(name2))
# 将列表转换为元组
print(tuple(list1))