from collections import UserDict
from validation import *


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.name] = record


class Record:

    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday


    def add(self, new_phone):
        self.phones.append(new_phone)

    def edit(self, old_phone, new_phone):
        if old_phone in self.phones:
            self.phones.remove(old_phone)
            self.phones.append(new_phone)
        else:
            print(f"In this record no phone {old_phone}")

    def remove(self, old_phone):
        if old_phone in self.phones:
            self.phones.remove(old_phone)
        else:
            print(f"In this record no phone {old_phone}")

    def days_to_birthday(self):
        if self.birthday is not None:
            self.birthday = self.birthday.birthday
            today = date.today()
            dob_data = self.birthday.split(".")
            dobDay = int(dob_data[0])
            dobMonth = int(dob_data[1])
            dobYear = int(dob_data[2])
            dob = date(dobYear, dobMonth, dobDay)
            thisYear = today.year
            nextBirthday = date(thisYear, dobMonth, dobDay)
            if today < nextBirthday:
                gap = (nextBirthday - today).days
                print("Abonent's birhday is in " + str(gap) + ' days.')
            elif today == nextBirthday:
                print("Today is abonent's birthday! Happy Birthday!")
            else:
                nextBirthday = date(thisYear + 1, dobMonth, dobDay)
                gap = (nextBirthday - today).days
                print("Abonent's birthday is in " + str(gap) + ' days.')
        else:
            print("Current contact doesn't have date of birth")


class Name:

    def __init__(self, name):
        self.name = name


class Fild:
    pass


class Phone(Fild):

    def __init__(self, value):
        self.__value = phone_number_validation(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = phone_number_validation(new_value)


class Birthday(Fild):

    def __init__(self, birthday):
        self.__birthday = birthday_validation(birthday)

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday_validation(birthday)


name = Name("Bill")
phone = Phone("+380976772685")
# print(phone.value)
phone.value = 380976772222
# print(phone.value)
bd = Birthday("19 02 1993")
# print(bd.birthday)
# bd.birthday = "01 03 2000"
# print(bd.birthday)
rec = Record(name, phone, bd)
print(rec.days_to_birthday())
