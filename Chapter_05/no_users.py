"""
文件名: no_users.py
描述: 练习 5.9 - 在循环前检查列表是否为空
"""

# --- 练习 5.9: No Users ---

# 1. 数据准备: 创建一个空列表来测试
# 你可以尝试把下面的 [] 改回包含名字的列表来验证另一种情况
usernames = [] 

# 2. 检查列表是否为空
# 💡 技巧: 在 Python 中，非空列表被视为 True，空列表被视为 False
# 所以可以直接写 'if usernames:'
if usernames:
    # 如果列表不为空，执行正常的循环
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    # 3. 处理列表为空的情况
    print("We need to find some users!")