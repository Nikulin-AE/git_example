def greet(name, surname):
    """Выводит приветствие на консоль.

    Args:
        name (str): Имя пользователя.
    """
    print(f"Привет, {name} {surname}!")

if __name__ == "__main__":
    user_name = input("Как тебя зовут? ")
    surname = input("Какая у вас фамилия? ")
    greet(user_name, surname)