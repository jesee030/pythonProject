from turtleShow import *  # 导入模块turtle，*代表所有

speed(0)  # 将绘制速度设置为0，这是最快的

pencolor('red')  # 将笔/线的颜色设置为红色

bgcolor('green')  # 将背景/画布的颜色设置为黑色

x = 0  # 创建一个值为0的变量x

up()  # 抬起笔，所以没有画线

# nota fd()表示向前移动，bk()表示向后移动

# rt() 或 lt()表示向右倾斜一定角度

rt(45)

fd(90)

rt(135)

down()  # 放下笔，以便乌龟可以画画

while x < 120:  # 当x的值小于120时，不断地这样做：
    fd(200)

    rt(61)

    fd(200)

    rt(61)

    fd(200)

    rt(61)

    fd(200)

    rt(61)

    fd(200)

    rt(61)

    fd(200)

    rt(61)

    rt(11.1111)

    x = x + 1  # adds 1 to the value of x,

    # 所以每次循环后都接近120`
done()
