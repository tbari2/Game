from tkinter import *
import random

w = 700
h = 500
pace = 150
size = 25
body_length = 5
snakebody_color = "#FFFF00"
edible_color = "#0D0D0D"
background_display = "#FFFFFF"


class Snake:
    def __init__(self):
        self.body_size = body_length
        self.coordinates = []
        self.squares = []
        for i in range(0, body_length):
            self.coordinates.append([0, 0])
        for a, b, in self.coordinates:
            square = display.create_rectangle(a, b, a + size, b + size, fill=snakebody_color, tag="snake")
            self.squares.append(square)


class Edible:
    def __init__(self):
        a = random.randint(0, (w / size) - 1) * size
        b = random.randint(0, (h / size) - 1) * size
        self.coordinates = [a, b]
        display.create_oval(a, b, a + size, b + size, fill=edible_color, tag="edible")


def turn(snake, edible):
    a, b = snake.coordinates[0]
    if d == "up":
        b -= size
    elif d == "down":
        b += size
    elif d == "left":
        a -= size
    elif d == "right":
        a += size

    snake.coordinates.insert(0, (a, b))
    square = display.create_rectangle(a, b, a + size, b + size, fill=snakebody_color)
    snake.squares.insert(0, square)
    if a == edible.coordinates[0] and b == edible.coordinates[1]:
        global point
        point += 1
        label.config(text="Points:{}".format(point))
        display.delete("edible")
        edible = Edible()
    else:
        del snake.coordinates[-1]
    display.delete(snake.squares[-1])
    del snake.squares[-1]
    if collision(snake):
        game_over()
    else:
        app.after(pace, turn, snake, edible)


def snake_direction(d2):
    global d

    if d2 == 'left':
        if d != 'right':
            d = d2
    elif d2 == 'right':
        if d != 'left':
            d = d2
    elif d2 == 'up':
        if d != 'down':
            d = d2
    elif d2 == 'down':
        if d != 'up':
            d = d2


def collision(snake):
    a, b = snake.coordinates[0]

    if a < 0 or a >= w:
        print("Game over")
        return True
    elif b < 0 or b >= h:
        print("Game over")
        return True

    for body_part in snake.coordinates[1:]:
        if a == body_part[0] and b == body_part[1]:
            print("Game over")
            return True
    return False


def game_over():
    display.delete(ALL)
    display.create_text(display.winfo_width() / 2, display.winfo_height() / 2, font=('MS Sans Serif', 70),
                        text="Game Over", fill="black", tag="gameover")


app = Tk()
app.title("SNAKE GAME")
app.resizable(False, False)

point = 0
d = 'down'
label = Label(app, text="Points:{}".format(point), font=('MS Sans Serif', 40))
label.pack()

display = Canvas(app, bg=background_display, height=h, width=w)
display.pack()

app.update()
app_width = app.winfo_width()
app_height = app.winfo_height()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

a = int((screen_width / 2) - (app_width / 2))
b = int((screen_height / 2) - (app_height / 2))

app.geometry(f"{app_width}x{app_height}+{a}+{b}")
app.bind('<Left>', lambda event: snake_direction('left'))
app.bind('<Right>', lambda event: snake_direction('right'))
app.bind('<Up>', lambda event: snake_direction('up'))
app.bind('<Down>', lambda event: snake_direction('down'))

snake = Snake()
edible = Edible()
turn(snake, edible)
app.mainloop()
