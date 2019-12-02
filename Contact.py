"""2) Создайте класс Contact, и объявите в конструкторе(__init__) ему поля
name, last_name и number. Далее, создайте класс ContactList, в нем
объявите переменную contacts_list = [], после, реализуйте три метода,
add_contact(), который берет в аргументы объект класса Contact и
добавляет в лист contacts_list, search_contact(), который должен вернуть
нам контакт если такой имеется в списке, remove_contact() который
должен удалить найденный контакт, эти методы также принимают в
качества аргумента объект класса Contact. Создайте несколько объектов
класса Contact, и объект класса ContactList, воспользуйтесь всеми его
методами."""


class Contact:
    def __init__(self, name, last_name, number):
        self.name = name
        self.last_name = last_name
        self.number = number


class ContactList(Contact):
    contacts_list = []

    def __init__(self, name, last_name, number):
        Contact.__init__(self, name, last_name, number)

    def add_contact(self):
        # self.contacts_list.append(ContactList(self.name, self.last_name, self.number))
        self.contacts_list.append(self.name)
        return ContactList, self.contacts_list

    def search_contact(self):
        if self.name in self.contacts_list:
            print('We have this contact')

    def remove_contact(self):
        if self.name in self.contacts_list:
            self.contacts_list.remove(self.name)


c1 = ContactList('John', 'Anderson', 2020002)
c1.add_contact()
c2 = ContactList('Tom', 'Jefferson', 3030003)
c2.add_contact()
c3 = ContactList('Kim', 'Jun', 15151515)
c3.add_contact()
print(c1.contacts_list)
print(c1.search_contact())
c3.remove_contact()
print(c1.contacts_list)
