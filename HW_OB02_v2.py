class User():
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self.__level = 'user'

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_level(self):
        return self.__level

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__level = 'admin'

    def add_user(self, list_users, user):
        return list_users.append(user.get_name())

    def remove_user(self, list_users, user):
        return list_users.remove(user.get_name())

    def get_level(self):
        return self.__level

#Список пользователей
users = []

#Экземпляры класса User
user1 = User(123, "Алексей")
user2 = User(146, "Максим")
user3 = User(795, "Матвей")

#Экземпляр класса Admin
admin1 = Admin(483, "Олег")


#Вывод уровня доступа user
print(user1.get_level())

#Вывод уровня доступа admin
print(admin1.get_level())

#Вывод пустого списка
print(users)

#Добавим первого пользователя и выведем на дисплей
admin1.add_user(users, user1)
print(users)

#Добавим второго пользователя и выведем на дисплей
admin1.add_user(users, user2)
print(users)

#Добавим третьего пользователя и выведем на дисплей
admin1.add_user(users, user3)
print(users)

#Удалим первого пользователя и выведем на дисплей
admin1.remove_user(users, user1)
print(users)





