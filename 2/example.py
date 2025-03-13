
# 打印九九乘法表
for i in range(1, 10):
        for j in range(1, i+1):
            # 打印语句中，大括号及其里面的字符 (称作格式化字段) 将会被 .format() 中的参数替换,注意有个点的
            print('{}x{}={}\t'.format(i, j, i*j), end='')  # end='' 用于将结果输出到同一行
        print()


# 判断是否是闰年
num = 1
year = int(input("请输入一个年份: "))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print('{0} 是闰年 {1}' .format(year, num)) #{} 为占位符 0.1 代表format()中的参数顺序
else:
     print('{1} 不是闰年{0}' .format(year ,num))