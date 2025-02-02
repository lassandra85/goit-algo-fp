import turtle
import math

def draw_branch(t, length, level):
    """Рекурсивна функція для малювання дерева Піфагора"""
    if level == 0:
        return
    
    # Малюємо основну гілку
    t.forward(length)

    # Зберігаємо поточну позицію та кут
    start_position = t.pos()
    start_heading = t.heading()

    # Ліва гілка
    t.left(45)
    draw_branch(t, length * math.sqrt(2) / 2, level - 1)

    # Повертаємося до попередньої позиції
    t.penup()
    t.goto(start_position)
    t.setheading(start_heading)
    t.pendown()

    # Права гілка
    t.right(45)
    draw_branch(t, length * math.sqrt(2) / 2, level - 1)

    # Повертаємося назад
    t.penup()
    t.goto(start_position)
    t.setheading(start_heading)
    t.pendown()

def draw_tree(level):
    """Ініціалізація екрану та запуск малювання дерева"""
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Орієнтація вгору
    t.penup()
    t.goto(0, -200)  # Початкова позиція
    t.pendown()
    
    draw_branch(t, 100, level)  # Початкова довжина гілки - 100
    screen.mainloop()

# Введення рівня рекурсії від користувача
level = int(input("Введіть рівень рекурсії (рекомендовано 5-10): "))
draw_tree(level)
