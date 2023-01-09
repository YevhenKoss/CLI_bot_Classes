from collections import UserDict
from validation import *


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.name] = record


class Record:
    def __init__(self, name, phone=None, day_of_birth=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = ""
        if day_of_birth:
            self.birthday += day_of_birth

    def add (self, new_phone):
        self.phones.append(new_phone)

    def edit (self, old_phone, new_phone):
        if old_phone in self.phones:
            self.phones.remove(old_phone)
            self.phones.append(new_phone)
        else:
            print(f"In this record no phone {old_phone}")

    def remove (self, old_phone):
        if old_phone in self.phones:
            self.phones.remove(old_phone)
        else:
            print(f"In this record no phone {old_phone}")


class Name:
    def __init__(self, name):
        self.name = name


class Phone:
    def __init__(self, value):
        self.__value = phone_number_validation(value)


    @property
    def value(self):
        return self.__value


    @value.setter
    def value(self, new_value):
        self.__value = phone_number_validation(new_value)


class Field:
    pass


name = Name("Bill")
phone = Phone("+380976772685")
# print(phone.value)
phone.value = 38097677222200
# print(phone.value)