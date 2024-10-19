import turtle as t

def outline():
    # 绘制缩小4倍的南瓜轮廓
    t.color('#CF5E1A', '#CF5E1A')
    t.penup()
    t.goto(200, 7-100)  # 起始位置缩小为原来的四分之一
    t.pendown()
    t.seth(90)
    t.begin_fill()
    for j in range(7):  # 循环缩小
        t.fd(j / 4)  # 前进距离缩小为原来的四分之一
        t.left(3.6)
    for j in range(7, 0, -1):
        t.fd(j / 4)
        t.left(3.6)
    t.seth(-90)
    t.circle(63.5, 180)  # 半径缩小为原来的1/4
    t.end_fill()


def tail():
    # 绘制缩小4倍的南瓜枝，向右移动
    t.penup()
    t.goto(250, 20-100)  # 将位置向右移动
    t.pendown()
    t.color('#2E3C01')
    t.seth(100)
    t.pensize(6.25)  # 笔触宽度也缩小为原来的四分之一
    t.circle(15, 100)


def eyes(args):
    # 绘制缩小4倍的眼睛
    for items in args:
        position, angle, direction = items
        t.pensize(1.5)  # 笔触宽度缩小
        t.penup()
        t.goto(position / 10+260, -15-80)  # 位置缩小并调整y轴以对齐南瓜
        t.pendown()
        t.color('#4C180D', '#4C180D')
        t.begin_fill()
        t.seth(angle)
        for j in range(14):  # 眼睛循环缩小
            t.fd(1.5)  # 前进距离缩小
            if direction:
                t.left(3)
            else:
                t.right(8)
        t.goto(position / 10+260, -15-75)  # 返回起始位置
        t.end_fill()


def nose():
    # 绘制缩小4倍的鼻子
    t.penup()
    t.goto(0+260, -30-75)  # 调整y轴位置对齐南瓜
    t.seth(180)
    t.pendown()
    t.begin_fill()
    t.circle(12.5, steps=3)  # 半径缩小为原来的1/4
    t.end_fill()


def mouth():
    # 绘制缩小4倍的嘴巴
    t.color('#F9D503', '#F9D503')
    t.pensize(1)  # 笔触宽度缩小
    t.penup()
    t.goto(-37.5+260, -50-80)  # 位置缩小并调整y轴位置
    t.pendown()
    t.begin_fill()
    t.seth(-30)
    t.fd(25)  # 路径长度缩小
    t.left(90)
    t.fd(7.5)
    t.right(90)
    t.fd(15)
    t.left(60)
    t.fd(15)
    t.right(90)
    t.fd(7.5)
    t.left(90)
    t.fd(25)
    t.end_fill()


def draw_pumpkin(position):
    # 在指定位置绘制南瓜
    t.penup()
    t.goto(position)
    t.pendown()
    outline()
    tail()
    eyes_items = [(-15, 230, 0), (15, -10, 1)]  # 缩小后的眼睛位置
    eyes(eyes_items)
    nose()
    mouth()


if __name__ == '__main__':
    t.speed(10)  # 设置绘制速度
    t.bgcolor('black')  # 设置背景颜色
    
    draw_pumpkin((0, -200))  # 第一个南瓜

    t.done()
