import turtle

def draw_koch_segment(t, length, level):
    """
    Рекурсивно малює один сегмент сніжинки Коха.
    :param t: Об'єкт turtle
    :param length: Довжина лінії
    :param level: Рівень рекурсії
    """
    if level == 0:
        t.forward(length)  # Базовий випадок: малюємо пряму лінію
    else:
        length /= 3.0
        draw_koch_segment(t, length, level - 1)  # Перша пряма частина
        t.left(60)
        draw_koch_segment(t, length, level - 1)  # Верхній "пік"
        t.right(120)
        draw_koch_segment(t, length, level - 1)  # Нижній "пік"
        t.left(60)
        draw_koch_segment(t, length, level - 1)  # Остання пряма частина

def draw_koch_snowflake(t, length, level):
    """
    Малює повну сніжинку Коха.
    :param t: Об'єкт turtle
    :param length: Довжина сторони сніжинки
    :param level: Рівень рекурсії
    """
    for _ in range(3):  # Сніжинка складається з трьох сегментів
        draw_koch_segment(t, length, level)
        t.right(120)

def main():
    # Запитуємо рівень рекурсії у користувача
    level = int(input("Введіть рівень рекурсії (наприклад, 3): "))
    length = 300  # Довжина сторони базового трикутника

    # Ініціалізація turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Фрактал: Сніжинка Коха")
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    # Малюємо сніжинку Коха
    draw_koch_snowflake(t, length, level)

    # Завершення
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()