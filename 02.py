import turtle
import math

def draw_tree(branch_length, level):
    if level == 0:
        return

    # Малюємо основну гілку
    turtle.forward(branch_length)

    # Ліва гілка
    turtle.left(45)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1)
    turtle.right(45)  # Повертаємо черепашку назад

    # Права гілка
    turtle.right(45)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1)
    turtle.left(45)  # Повертаємо черепашку назад

    # Повертаємось назад до початкової точки
    turtle.backward(branch_length)

def main():

    level = int(input("Введіть рівень рекурсії (рекомендується 5-10): "))


    turtle.speed(0)
    turtle.left(90)  
    turtle.up()
    turtle.goto(0, -200)  
    turtle.down()

    # Малюємо дерево
    draw_tree(100, level)

    # Завершення програми
    turtle.done()

# Запускаємо програму
main()
