import turtle
import time
import random

# --- 1. 游戏设置 ---
delay = 0.1  # 控制蛇移动的速度
score = 0
high_score = 0

# 设置屏幕
wn = turtle.Screen()
wn.title("Python 贪吃蛇 - By Kirs")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # 关闭屏幕自动刷新

# --- 2. 创建角色 ---

# 蛇头
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# 蛇的身体
segments = []

# 食物
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# 记分牌
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("得分: 0  最高分: 0", align="center", font=("Courier", 24, "normal"))

# --- 3. 定义函数 ---

def go_up():
    if head.direction != "down": # 不能直接掉头
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# --- 4. 键盘绑定 ---
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
# 支持方向键
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# --- 5. 游戏主循环 ---
while True:
    wn.update()

    # --- 碰撞检测：撞墙 ---
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # 隐藏身体 (虽然列表清空了，但屏幕上的图形还在，要隐藏掉)
        for segment in segments:
            segment.goto(1000, 1000) # 移到屏幕外
        
        # 清空身体列表 (用到了 clear 方法)
        segments.clear()
        
        # 重置分数
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("得分: {}  最高分: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # --- 碰撞检测：吃到食物 ---
    if head.distance(food) < 20:
        # 1. 移动食物到随机位置
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        
        # 2. 增加一节身体
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment) # 【重点】用到列表的 append!

        # 3. 增加难度（稍微变快一点）
        delay -= 0.001

        # 4. 增加分数
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("得分: {}  最高分: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # --- 移动身体 ---
    # 这是一个倒序循环：让第N节移到第N-1节的位置
    # 比如：尾巴移到倒数第二节的位置，以此类推
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # 第0节身体（脖子）移到头的位置
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # --- 碰撞检测：撞到自己 ---
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("得分: {}  最高分: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop