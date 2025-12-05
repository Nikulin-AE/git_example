def greet(name: str, surname: str):
    """Выводит приветствие на консоль.

    Args:
        name (str): Имя пользователя.
    """
    print(f"Привет, {name} {surname}!")

if __name__ == "__main__":
    user_name: str = input("Как тебя зовут? ")
    surname: str  = input("Какая у вас фамилия? ")
    greet(user_name, surname)