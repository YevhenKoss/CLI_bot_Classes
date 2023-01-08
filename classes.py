from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.name] = record


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

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
        self.value = value


class Field:
    pass
