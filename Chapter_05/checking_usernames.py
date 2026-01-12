"""
文件名: checking_usernames.py
描述: 练习 5.10 - 检查新用户名是否已被使用（不区分大小写）
"""

# --- 练习 5.10: Checking Usernames ---

# 1. 数据准备
# current_users 包含一些混杂大小写的名字
current_users = ['John', 'Admin', 'Alice', 'Eric', 'David']
new_users = ['sarah', 'John', 'ERIC', 'mike', 'tom']

# 2. 预处理: 创建当前用户名的全小写副本
# 💡 逻辑: 为了比较时不区分大小写，我们需要把现有的名单都转换成小写
# 这里使用列表推导式 (List Comprehension) 来快速生成
current_users_lower = [user.lower() for user in current_users]

# 或者使用初学者更容易理解的循环方式:
# current_users_lower = []
# for user in current_users:
#     current_users_lower.append(user.lower())

# 3. 遍历新用户列表
for new_user in new_users:
    # 4. 核心检查: 将新用户名也转为小写，去和拥有所有小写名的列表比较
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"Great, the username '{new_user}' is available.")