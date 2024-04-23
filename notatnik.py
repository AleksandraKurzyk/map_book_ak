users: list = [

    {"name": "Julia", "surname": "Gotowiec", "posts": 1500, },
    {"name": "Hubert", "surname": "Sybilski", "posts": 123456, },
    {"name": "Adrian", "surname": "Dobrzański", "posts": 3, },
    {"name": "Bartek", "surname": "Wyrzykowski", "posts": 666, }
]
def update_user(users: list):
    imie = input("Podaj imie użytkownika, którego dane chcesz zmienić: ")
    for user in users:
        if user["name"] == imie:

            user["name"] = input("Podaj nowe imię: ")
            user["surname"] = input("Podaj nowe nazwisko: ")
            user["posts"] = int(input("Podaj nową liczbę postów: "))

update_user(users)
print(users)