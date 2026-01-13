"""
文件名: polling.py
描述: 练习 6.6 - 遍历人员名单，检查他们是否已经参与了字典中的调查
"""

# --- 练习 6.6: 调查 ---

# 1. 数据准备: 现有的调查结果字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 2. 名单准备: 创建一个包含应该接受调查的人员列表
# 💡 其中有些人已经在字典里 (如 phil)，有些人不在 (如 mike)
coders_to_poll = ['phil', 'josh', 'david', 'becca', 'sarah', 'mike']

# 3. 遍历检查: 对名单中的每个人进行判断
print("=== Polling Status Check ===")

for coder in coders_to_poll:
    # 4. 逻辑判断: 检查名字是否在字典的键中
    # 技巧: if name in dictionary 默认就是在检查 keys
    if coder in favorite_languages.keys():
        print(f"Thank you, {coder.title()}, for taking the poll!")
    else:
        print(f"{coder.title()}, please verify your email and take the poll!")

# 作者: Kris
# 日期: 2026-01-13