from point import Point

x1,y1 = input().split(',')
x2,y2  = input().split(',')
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
dx,dy = input().split(',')
dx = int(dx)
dy = int(dy)

p1 = Point(x1, y1)
p2 = Point(x2,y2)
print('p1点的坐标为：',p1)
print('p2点的坐标为：',p2)

p2.move_by(dx, dy)
print('移动后的坐标为：',p2)
print('p1与p2点的距离为：',p1.distance_to(p2))