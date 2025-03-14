print('\n'.join([' '.join ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))


list1=[x * x for x in range(1, 11)]
print(list1)


list1= [x * x for x in range(1, 11) if x % 2 == 0]
print(list1)


list1= [(x+1,y+1) for x in range(3) for y in range(5) if (x + y < 4)] 
print(list1)