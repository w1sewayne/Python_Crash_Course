# 作者：Kirs
# 日期：2025-12-28

# 练习 3.6：梦想的旅行目的地
# 定义梦想的旅行目的地列表
locations = ['Seoul', 'Melbourne', 'New York', 'Paris', 'Wonju']
# 打印原始列表
print(locations)
# 使用 sorted() 按字母顺序打印列表, 不修改原列表
print(sorted(locations))
# 再次打印原列表以确认未修改
print(locations)
# 使用 sorted() 按字母逆序打印列表, 不修改原列表
print(sorted(locations, reverse=True))
# 再次打印原列表以确认未修改
print(locations)
# 使用 reverse() 方法反转列表顺序
locations.reverse()
print(locations)
# 再次使用 reverse() 方法恢复原列表顺序
locations.reverse()
print(locations)
# 使用 sort() 方法按字母顺序永久排序列表
locations.sort()
print(locations)
# 使用 sort() 方法按字母逆序永久排序列表
locations.sort(reverse=True)
print(locations)
# --- IGNORE ---