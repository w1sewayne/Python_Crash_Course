# 作者：Kirs
# 日期：2025-12-29

#练习 3.10: 列表操作全家桶
# 1. 创建一个包含列表的列表（在此例中为编程语言）
languages = ['Python', 'C', 'Java', 'Rust', 'Go']
print(f"Original: {languages}")

# --- 增 (Create/Add) ---
languages.append('Swift')          # 加到末尾
languages.insert(1, 'JavaScript')  # 插到索引1
print(f"After Add: {languages}")

# --- 删 (Delete/Remove) ---
del languages[2]             # 知道索引，删掉 'C'
popped_lang = languages.pop() # 弹出末尾 'Swift'
languages.remove('Java')      # 知道值，删掉 'Java'
print(f"After Delete: {languages}")
print(f"Popped language was: {popped_lang}")

# --- 改 (Update/Sort) ---
# 临时排序看看
print(f"Sorted view: {sorted(languages)}")

# 永久反转
languages.reverse()
print(f"Reversed: {languages}")

# 永久排序
languages.sort()
print(f"Permanently Sorted: {languages}")

# --- 查 (Read/Meta) ---
print(f"Final list has {len(languages)} languages.")
# 确保列表非空
# Senior Note: 在 Python 中，空列表会被视为 False，非空列表为 True。
if languages:
    print(f"The first language is {languages[0]}")