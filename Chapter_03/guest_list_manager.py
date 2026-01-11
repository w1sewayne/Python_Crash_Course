# 作者：Kirs
# 日期：2025-12-28

# 练习 3.4：嘉宾邀请函及变动
# 定义嘉宾列表
guests = ['Alex', 'Bruce', 'Charlie']

# 打印邀请函
# 使用 f-string 是最现代、最高效的字符串格式化方式。
print(f"\n亲爱的{guests[0]}, 邀请您参加我的生日聚会！")
print(f"\n亲爱的{guests[1]}, 邀请您参加我的生日聚会！")
print(f"\n亲爱的{guests[2]}, 邀请您参加我的生日聚会！")

#练习 3.5：嘉宾变动
busy_guest = guests[0]
print(f"\n很遗憾, {busy_guest}不能来参加聚会。")
guests[0] = 'Anna'

# 重新打印邀请函
print(f"\n亲爱的{guests[0]}, 邀请您参加我的生日聚会！")
print(f"\n亲爱的{guests[1]}, 邀请您参加我的生日聚会！")
print(f"\n亲爱的{guests[2]}, 邀请您参加我的生日聚会！")

#练习 3.6：更多嘉宾
print("\n好消息! 我找到了一个更大的餐桌, 可以邀请更多的嘉宾参加聚会。")

# 在列表开头添加一位嘉宾
guests.insert(0, 'Xavier')
# 在列表中间添加一位嘉宾
guests.insert(2, 'Yvonne')
# 在列表末尾添加一位嘉宾
guests.append('Zach')

#重新打印邀请函
print(f"\n亲爱的{guests[0]}, 邀请您参加我的生日聚会！")
print(f"\n亲爱的{guests[1]}, 邀请您参加我的生日聚会！")
print(f"\n亲爱的{guests[2]}, 邀请您参加我的生日聚会！")
print(f"\n亲爱的{guests[3]}, 邀请您参加我的生日聚会！")
print(f"\n亲爱的{guests[4]}, 邀请您参加我的生日聚会！")
print(f"\n亲爱的{guests[5]}, 邀请您参加我的生日聚会！")
print(len(guests))

#练习3.7：缩减嘉宾名单
print("\n很遗憾, 由于餐桌无法按时送达, 我只能邀请两位嘉宾参加聚会。")
poped_guests = guests.pop()
print(f"\n亲爱的{poped_guests}, 很抱歉, 由于餐桌问题, 无法邀请您参加聚会。")
poped_guests = guests.pop()
print(f"\n亲爱的{poped_guests}, 很抱歉, 由于餐桌问题, 无法邀请您参加聚会。")
poped_guests = guests.pop()
print(f"\n亲爱的{poped_guests}, 很抱歉, 由于餐桌问题, 无法邀请您参加聚会。")
poped_guests = guests.pop()
print(f"\n亲爱的{poped_guests}, 很抱歉, 由于餐桌问题, 无法邀请您参加聚会。")
# 最后两位嘉宾仍然受邀
print(f"\n亲爱的{guests[0]}, 您仍然被邀请参加聚会！")
print(f"\n亲爱的{guests[1]}, 您仍然被邀请参加聚会！")
print(len(guests))
# 清空嘉宾名单
del guests[0]
del guests[0]
print(guests)  # 输出空列表以确认嘉宾名单已清空
print(len(guests))  # 输出0以确认嘉宾名单已清空