# -*- coding: UTF-8 -*-

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 遍历枚举类型
for name, member in Month.__members__.items():
    print(name, '---------', member, '----------', member.value)

# 直接引用一个常量
print('\n', Month.Jan)

# 我们使用 `Enum` 来定义了一个枚举类。

# 上面的代码，我们创建了一个有关月份的枚举类型 Month ，这里要注意的是构造参数，第一个参数 Month 表示的是该枚举类的类名，第二个 tuple 参数，表示的是枚举类的值；当然，枚举类通过 `__members__` 遍历它的所有成员的方法。

# 注意的一点是 ， `member.value` 是自动赋给成员的 `int` 类型的常量，默认是从 1 开始的。