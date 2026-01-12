"""
文件名: more_conditional_tests.py
描述: 练习 5.2 - 更多条件测试，包含数值比较、逻辑运算及列表检查
"""

# --- 练习 5.2: 更多条件测试 ---

# 1. 检查两个字符串是否相等和不等
print("--- String Equality/Inequality Tests ---")
name = 'Alice'
print(f"Original name: {name}")
print(f"Is name == 'Alice'? {name == 'Alice'}")
print(f"Is name != 'Bob'? {name != 'Bob'}")


# 2. 使用 lower() 方法的条件测试
# 💡 逻辑: lower() 方法不会改变变量本身，只在比较时临时转换
print("\n--- Lower() Method Tests ---")
car_name = 'Audi'
print(f"Original car: {car_name}")
print(f"Is car_name.lower() == 'audi'? {car_name.lower() == 'audi'}")
print(f"Is car_name == 'audi'? {car_name == 'audi'} (Case sensitive check)")


# 3. 数值比较 (相等、不等、大于、小于、大于等于、小于等于)
print("\n--- Numerical Tests ---")
age = 18
print(f"Age is: {age}")
print(f"Is age == 18? {age == 18}")
print(f"Is age != 20? {age != 20}")
print(f"Is age > 10? {age > 10}")
print(f"Is age < 21? {age < 21}")
print(f"Is age >= 18? {age >= 18}")
print(f"Is age <= 18? {age <= 18}")


# 4. 使用关键字 and 和 or 的条件测试
print("\n--- 'and' / 'or' Keyword Tests ---")
num_1 = 20
num_2 = 30
# 💡 技巧: and 要求两边都为真，or 只要一边为真即可
print(f"Numbers: {num_1}, {num_2}")
print(f"Is num_1 > 10 and num_2 > 20? {num_1 > 10 and num_2 > 20}")
print(f"Is num_1 > 25 or num_2 > 25? {num_1 > 25 or num_2 > 25}")


# 5. 测试特定的值是否在列表中 (in)
print("\n--- List Membership ('in') Tests ---")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(f"Toppings list: {requested_toppings}")
print(f"Is 'mushrooms' in list? {'mushrooms' in requested_toppings}")
print(f"Is 'pepperoni' in list? {'pepperoni' in requested_toppings}")


# 6. 测试特定的值是否不在列表中 (not in)
print("\n--- List Membership ('not in') Tests ---")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
print(f"Banned users: {banned_users}, Current user: {user}")

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
print(f"Check result (user not in banned_users): {user not in banned_users}")


# 作者: Kris
# 日期: 2026-1-12