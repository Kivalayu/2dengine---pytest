from colorama import init, Fore

init()

class Engine2D:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = [[' ' for _ in range(width)] for _ in range(height)]
        self.color = Fore.LIGHTWHITE_EX


    def draw_point(self, x, y, char='+'):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.screen[y][x] = self.color + char


    def draw_line(self, x1, y1, x2, y2, char='+'):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            self.draw_point(x1, y1, char)
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def set_color(self, color):
        self.color = color

    def get_canvas_size(self):
        return self.width, self.height

    def render(self):
        for row in self.screen:
            print(''.join(row))



class Circle:
    def __init__(self, canvas, x, y, radius):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius


    def draw(self):
        x = 0
        y = self.radius
        delta = 1 - 2 * self.radius
        error = 0
        while y >= 0:
            self.canvas.draw_point(self.x + x, self.y + y, '*')
            self.canvas.draw_point(self.x + x, self.y - y, '*')
            self.canvas.draw_point(self.x - x, self.y + y, '*')
            self.canvas.draw_point(self.x - x, self.y - y, '*')
            error = 2 * (delta + y) - 1
            if ((delta < 0) and (error <= 0)):
                x += 1
                delta += 2 * x + 1
                continue
            error = 2 * (delta - x) - 1
            if ((delta > 0) and (error > 0)):
                y -= 1
                delta += 1 - 2 * y
                continue
            x += 1
            delta += 2 * (x - y)
            y -= 1


class Triangle:
    def __init__(self, canvas, x1, y1, x2, y2, x3, y3):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def draw(self):
        self.canvas.draw_line(self.x1, self.y1, self.x2, self.y2)
        self.canvas.draw_line(self.x2, self.y2, self.x3, self.y3)
        self.canvas.draw_line(self.x3, self.y3, self.x1, self.y1)


class Rectangle:
    def __init__(self, canvas, x1, y1, width, height):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height

    def draw(self):
        x2 = self.x1 + self.width
        y2 = self.y1
        x3 = self.x1 + self.width
        y3 = self.y1 + self.height
        x4 = self.x1
        y4 = self.y1 + self.height
        self.canvas.draw_line(self.x1, self.y1, x2, y2)
        self.canvas.draw_line(x2, y2, x3, y3)
        self.canvas.draw_line(x3, y3, x4, y4)
        self.canvas.draw_line(x4, y4, self.x1, self.y1)


width = int(input("Enter screen width: "))
height = int(input("Enter screen height: "))

my_canvas = Engine2D(width, height)

while True:
    colour = input("Want to choose a color? If yes, write its name. Available colors: Red, Blue, Green. If you don't want to select a color, press Enter: ")
    colour = colour.lower()

    if colour == "":
        break

    if colour == "red":
        my_canvas.set_color(Fore.RED)
        print("Selected color:", colour)
        break

    elif colour == "blue":
        my_canvas.set_color(Fore.BLUE)
        print("Selected color:", colour)
        break

    elif colour == "green":
        my_canvas.set_color(Fore.GREEN)
        print("Selected color:", colour)
        break

    else:
        print("Invalid color! Please choose from available colors.")

x_point = int(input("Enter the x coordinate of the point: "))
y_point = int(input("Enter the y coordinate of the point: "))

my_canvas.draw_point(x_point, y_point)

my_canvas.render()

x1_line = int(input("Enter the x coordinate of the starting line: "))
y1_line = int(input("Enter the y starting coordinate of the line: "))
x2_line = int(input("Enter the x coordinate of the line's end coordinate: "))
y2_line = int(input("Enter the end y coordinate of the line: "))

my_canvas.draw_line(x1_line, y1_line, x2_line, y2_line)

my_canvas.render()

x_circle = int(input("Enter the x coordinate of the circle's center: "))
y_circle = int(input("Enter the y coordinate of the circle's center: "))
radius_circle = int(input("Enter the radius of the circle: "))
print("Drawing a {} circle at ({}, {}) with radius {}".format(colour, x_circle, y_circle, radius_circle))

my_circle = Circle(my_canvas, x_circle, y_circle, radius_circle)

my_circle.draw()

my_canvas.render()

x1_triangle = int(input("Введите x координату первой точки треугольника: "))
y1_triangle = int(input("Введите y координату первой точки треугольника: "))
x2_triangle = int(input("Введите x координату второй точки треугольника: "))
y2_triangle = int(input("Введите y координату второй точки треугольника: "))
x3_triangle = int(input("Введите x координату третьей точки треугольника: "))
y3_triangle = int(input("Введите y координату третьей точки треугольника: "))
print("Drawing a {} triangle with vertices ({}, {}), ({}, {}), ({}, {})".format(colour, x1_triangle, y1_triangle, x2_triangle, y2_triangle, x3_triangle, y3_triangle))
my_triangle = Triangle(my_canvas, x1_triangle, y1_triangle, x2_triangle, y2_triangle, x3_triangle, y3_triangle)

my_triangle.draw()

my_canvas.render()

x1_rectangle = int(input("Введите x координату верхнего левого угла прямоугольника: "))
y1_rectangle = int(input("Введите y координату верхнего левого угла прямоугольника: "))
width_rectangle = int(input("Введите ширину прямоугольника: "))
height_rectangle = int(input("Введите высоту прямоугольника: "))
print("Drawing a {} rectangle at ({}, {}) with width {} and height {}".format(colour, x1_rectangle, y1_rectangle, width_rectangle, height_rectangle))

my_rectangle = Rectangle(Fore.RED + my_canvas, x1_rectangle, y1_rectangle, width_rectangle, height_rectangle)

my_rectangle.draw()

my_canvas.render()



