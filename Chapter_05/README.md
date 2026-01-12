# 🐍 Python Chapter 5: if 语句 (If Statements) 速查表

> **>>核心概念<<**：如果说之前的代码是一条笔直的高速公路，那么这一章就是教你如何修建**“岔路口”**。程序不再是“一条道走到黑”，而是学会了根据红绿灯（条件）来决定走哪条路。

---

## 1. 条件测试 (Conditional Tests)

**生活类比**：这就像是你在心里问问题。“今天是周六吗？”如果答案是 **True**（是），你就睡懒觉；如果答案是 **False**（否），你就去上班。

| 功能 | 英文关键字/符号 | 代码示例 | 备注/类比 |
| :--- | :--- | :--- | :--- |
| **检查相等** | `==` | `car == 'bmw'` | **双等号是发问！**<br>问：变量car的值是bmw吗？ |
| **检查不等** | `!=` | `topping != 'anchovies'` | 问：配料**不是**鳀鱼吗？ |
| **数值比较** | `>`, `<`, `>=`, `<=` | `age >= 18` | 常用于判断年龄、得分等范围。 |
| **多重条件(并且)** | `and` | `age > 18 and age < 65` | **两个都要满足**。<br>像登录：账号对 **且** 密码对。 |
| **多重条件(或者)** | `or` | `age < 4 or age > 65` | **满足一个就行**。<br>像优惠：老人 **或** 儿童免费。 |
| **在列表中** | `in` | `'mushrooms' in toppings` | 像在购物清单里找某样东西。 |
| **不在列表中** | `not in` | `'user' not in banned_users` | 像检查某人是否**没**被拉黑。 |

---

## 2. if 结构 (The if Structures)

**生活类比**：
* **if**: 路边的便利店。想买水就进去（执行），不想买就直接走过去（跳过）。
* **if-else**: 岔路口。要么左转，要么右转，必须选一条。
* **if-elif-else**: 自助餐选餐。是中餐？不是。是西餐？不是。那是甜点？是。

| 结构 | 语法 | 代码示例 | 备注/类比 |
| :--- | :--- | :--- | :--- |
| **简单 if** | `if` | `if alien_color == 'green':`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("5 points")` | 满足条件就做，不满足就跳过。 |
| **二选一** | `if-else` | `if age >= 18:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("Adult")`<br>`else:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("Minor")` | **非此即彼**。<br>要么成年，要么未成年。 |
| **多选一** | `if-elif-else` | `if age < 4:` ...<br>`elif age < 18:` ...<br>`else:` ... | **排他性**。<br>只要有一个满足，剩下的都不看了。 |

---

## 3. 列表与 if (Lists & if) **[高阶用法]**

**核心逻辑**：在处理列表前，先确认列表不是空的；或者在循环中对特定元素做特殊处理。

| 功能 | 代码示例 | 备注/类比 |
| :--- | :--- | :--- |
| **检查列表非空** | `if requested_toppings:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`for topping in ...` | **地道写法！**<br>列表有东西=True，<br>列表是空`[]`=False。 |
| **循环中特殊处理** | `for car in cars:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`if car == 'bmw':`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print(car.upper())`<br>&nbsp;&nbsp;&nbsp;&nbsp;`else:`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print(car.title())` | 就像流水线上的质检员，<br>看到特殊的'bmw'就贴个大标签。 |

---

## 4. 易错点与易混点 (Pitfalls & Confusions) **[🚨警示区]**

### **❌ 致命错误：赋值 vs 比较**
* **错误**：`if car = 'audi':` (这是把 audi 赋值给 car，Python 会报错)
* **正确**：`if car == 'audi':` (这是在问：car 等于 audi 吗？)
* **口诀**：**一个等号是动作，两个等号是问题。**

### **❌ 忽略大小写**
* `'Audi' == 'audi'` 的结果是 **False**。
* 如果用户输入了 'Admin'，你的代码只检查 'admin'，就会漏掉。
* **解决**：总是用 `.lower()` 转换成小写再比：`if user.lower() == 'admin':`

### **😵 易混淆：`elif` 还是 多个 `if`？**
* **场景 A：买票（只能买一种票）** -> 用 **if-elif-else**。
    * 因为你不能既是 5 岁又是 20 岁，只要满足一个，程序就应该停止检查。
* **场景 B：加配料（可以加多种）** -> 用 **多个独立的 if**。
    * 如果用 `elif`，加了蘑菇之后，程序就停了，不会再给你加芝士了。
    * **记住：** 想要**所有**匹配项，用多个 `if`；只要**一个**匹配项，用 `if-elif`。