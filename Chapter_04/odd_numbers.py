# 练习 4.6: 使用 range() 的第三个参数创建奇数列表
# 1. 从 1 开始，每次增加 2，直到 20
odd_numbers = list(range(1, 21, 2))
# 2. 使用 for 循环打印该列表中的每个奇数
for number in odd_numbers:
    print(number)

# 练习 4.7: 创建 3~30 内能被 3 整除的列表
# 1. 使用 range() 创建一个包含 3 到 30 之间所有能被 3 整除的数字的列表
threes = list(range(3, 31, 3))
# 2. 使用 for 循环打印该列表中的每个数字
for number in threes:
    print(number)

# 作者: Kris
# 日期: 2026-1-11