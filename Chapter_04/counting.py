# 练习4.3
# 使用 for 循环打印数字 1 到 20（含）
for value in range(1, 21):
    print(value)

# 练习4.4
# 1. 创建一个列表，其中包含数字 1 到 1,000,000
numbers = list(range(1, 1000001))
# 2. 使用for 循环打印该列表中的每个数字
for number in numbers:
    print(number)

# 练习4.5
# 1. 创建一个列表，其中包含数字 1 到 1,000,000
numbers = list(range(1, 1000001))
# 2. 使用 min()、max() 和 sum() 函数分别找出该列表中的最小值、最大值和总和
min_number = min(numbers)
max_number = max(numbers)
sum_numbers = sum(numbers)
print(f"最小值: {min_number}")
print(f"最大值: {max_number}")  
print(f"总和: {sum_numbers}")

# 作者：Kris
# 日期：2026-1-11