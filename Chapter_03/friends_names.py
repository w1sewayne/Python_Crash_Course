# 练习 3.1：朋友的名字
# 作者：Kirs
# 日期：2025-12-28

# 这是一个存储朋友姓名的列表
names = ['Alex', 'Bruce', 'Charlie', 'Danielle']

# 访问并打印列表中的每一个元素
# 注意：Python的索引是从0开始的
print(names[0])
print(names[1])
print(names[2])
print(names[-1])


# 为每个朋友创建一条个性化的问候消息并打印出来
# 使用 f-string (格式化字符串) 来构建消息
message_0 = f"你好, {names[0]}! 最近怎么样？"
print(message_0)

message_1 = f"你好, {names[1]}! 最近怎么样？"
print(message_1)

message_2 = f"你好, {names[2]}! 最近怎么样？"
print(message_2)

message_3 = f"你好, {names[3]}! 最近怎么样？"
print(message_3)
