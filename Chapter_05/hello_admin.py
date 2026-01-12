"""
文件名: hello_admin.py
描述: 练习 5.8 - 遍历用户名列表并对管理员打印特殊消息
"""

# --- 练习 5.8: Hello Admin ---

# 1. 数据准备: 创建包含 5 个以上用户名的列表
# 其中必须包含一个 'admin'
usernames = ['admin', 'eric', 'willie', 'alice', 'david']

# 2. 遍历列表并检查用户名
# 💡 逻辑: 循环会依次取出列表中的每一个名字赋值给 user 变量
for user in usernames:
    # 3. 检查是否为管理员
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        # 4. 对普通用户的问候
        # 使用 title() 让名字首字母大写，看起来更正式
        print(f"Hello {user.title()}, thank you for logging in again.")