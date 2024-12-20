import tkinter as tk

# Створення основного вікна
root = tk.Tk()
root.title("Рух кульки по полотну")

# Створення полотна розміром 400x400
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Початкові координати для кульки
x, y = 20, 20
radius = 10  # Радіус кульки

# Створення червоного круга в лівому верхньому куті
ball = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red")

# Змінна для зберігання попереднього положення кульки
prev_pos = [x - radius, y - radius, x + radius, y + radius]

# Функція для обчислення середини відрізка
def midpoint(pos):
    return [(pos[0] + pos[2]) / 2, (pos[1] + pos[3]) / 2]

# Функція для переміщення кульки і малювання сліду
def move_oval(event):
    global x, y, prev_pos

    # Крок зміщення
    step = 10

    # Визначення напрямків залежно від натиснутої клавіші
    if event.keysym == "Up":
        y -= step
    elif event.keysym == "Down":
        y += step
    elif event.keysym == "Left":
        x -= step
    elif event.keysym == "Right":
        x += step
    elif event.keysym == "a":  # Діагональ вгору-вліво
        x -= step
        y -= step
    elif event.keysym == "s":  # Діагональ вгору-вправо
        x += step
        y -= step
    elif event.keysym == "z":  # Діагональ вниз-вліво
        x -= step
        y += step
    elif event.keysym == "x":  # Діагональ вниз-вправо
        x += step
        y += step

    # Обмеження руху кульки в межах полотна
    x = max(radius, min(400 - radius, x))
    y = max(radius, min(400 - radius, y))

    # Отримання нових координат кульки
    new_pos = [x - radius, y - radius, x + radius, y + radius]

    # Малювання сліду
    center_start = midpoint(prev_pos)
    center_end = midpoint(new_pos)
    canvas.create_line(center_start[0], center_start[1], center_end[0], center_end[1],
                       fill="green", width=7)

    # Оновлення положення кульки
    canvas.coords(ball, *new_pos)
    prev_pos = new_pos

# Прив'язка подій клавіатури до функції move_oval
canvas.bind_all("<Key>", move_oval)

# Запуск головного циклу програми
root.mainloop()