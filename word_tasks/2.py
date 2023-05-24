class NotUniqueName(Exception):
    pass


class NegativeAge(Exception):
    pass


class LowAge(Exception):
    pass


class BadEmail(Exception):
    pass


class User:
    def __init__(self, name: str, email: str, age: int):
        try:
            age = int(age)
            if age < 0:
                raise NegativeAge
            elif age < 16:
                raise LowAge
        except ValueError:
            raise ValueError

        if name in catalog.keys():
            raise NotUniqueName

        if '@' not in email or not email.split('@')[0] or not email.split('@')[1]:
            raise BadEmail

        self.name = name
        self.email = email
        self.age = age

def main(users:list):
    for user in users:
        try:
            check = User(*user)
            catalog[user[0]] = User(*user)
        except ValueError:
            print('Возраст должен быть числом')
        except LowAge:
            print("Возраст меньше 16")
        except NegativeAge:
            print("Введен отрицательный возраст")
        except NotUniqueName:
            print("Такое имя пользователя существует")
        except BadEmail:
            print("Введен некорректный email")

    for user in catalog.values():
        print(user.__dict__)

catalog = {}
if __name__ == '__main__':
    main([("aboba", "s@s", 10), ('a', 'a@', 17), ('b', 'b', 20), ('c', 'c@c', 55), ('c', 'c@c',41), ('d', 'd@d', -1), ('e', 'e@e', 29)])
