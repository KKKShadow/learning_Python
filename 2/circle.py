for letter in 'Hello 两点水':
    print(letter)

for i in range(3):
    print(i)



count = 1
sum = 0
while (count <= 100):
    sum = sum + count
    if ( sum > 1000):  #当 sum 大于 1000 的时候退出循环
        break
    count = count + 1
print(sum)


count = 1
sum = 0
while (count <= 100):
    if ( count % 2 == 0):  # 双数时跳过sum  输出奇数和
        count = count + 1
        continue       #  跳过当前循环 进入下一次循环
    sum = sum + count
    count = count + 1
print(sum)


for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         j = int(j)
         print ('%d 是一个合数' %num , end=',')
         print("其因子为 %d %d" % (i, j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)