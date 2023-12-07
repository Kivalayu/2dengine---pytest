
class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = [[' ' for _ in range(width)] for _ in range(height)]

    def draw_point(self, x, y, char='+'):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.screen[y][x] = char

    def render(self):
        for row in self.screen:
            print(''.join(row))

    def check_point(self, x, y, char):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.screen[y][x] == char
        return False


def test_class_circle():
    width = 1000
    height = 1000

    my_canvas = Canvas(width, height)

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

    x_circle = 20
    y_circle = 20
    radius_circle = 10
    print("Drawing a circle at ({}, {}) with radius {}".format(x_circle, y_circle, radius_circle))

    my_circle = Circle(my_canvas, x_circle, y_circle, radius_circle)

    my_circle.draw()

    my_canvas.render()

    assert my_canvas.check_point(20,15 , '*') == False
    assert my_canvas.check_point(20, 15, '*') == False
    assert my_canvas.check_point(25, 20, '*') == False
    assert my_canvas.check_point(15, 20, '*') == False