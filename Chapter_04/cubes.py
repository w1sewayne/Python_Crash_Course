# 练习4.8: 1~10的立方
# 创建一个空列表用于存储立方值
cubes = []
# 使用 for 循环计算数字 1 到 10 的立方并添加到列表中
for value in range(1, 11):
    # 计算当前数字的立方 (3次方)
    cube = value ** 3
    # 将结果添加到列表末尾
    cubes.append(cube)
# 打印立方列表中的每个立方值
for cube in cubes:
    print(cube)

# 练习4.9：使用列表推导式创建一个包含数字 1 到 10 的立方的列表
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# 作者：Kris
# 日期：2026-1-11