import turtle
import random
import math

# 设置画布
turtle.setup(800, 600)
turtle.speed(0)
turtle.hideturtle()

# 设置颜色列表
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# 写出祝福内容
def draw_birthday_message(message, radius):
    angle = 360 / len(message)
    for char in message:
        color = random.choice(colors)
        turtle.penup()
        if char == "20":
            turtle.color("pink")
            x = 0
            y = -20  # 调整"20"的位置
        else:
            turtle.color(color)
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
        turtle.goto(x, y)
        turtle.pendown()
        turtle.write(char, font=("Arial", int(48 + radius / 10), "bold"))  # 调整字体大小
        angle += 360 / len(message)

# 画出生日祝福
for i in range(10):
    draw_birthday_message("生日快乐20岁", 200 + i * 20)

# 隐藏turtle
turtle.hideturtle()

# 点击关闭窗口
turtle.done()
