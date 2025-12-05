def greet(name):
    """Выводит приветствие на консоль.

    Args:
        name (str): Имя пользователя.
    """
    print(f"Привет, {name}!")

if __name__ == "__main__":
    user_name = input("Как тебя зовут? ")
    greet(user_name)