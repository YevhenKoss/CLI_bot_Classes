from collections import UserDict


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
        value = str(value)
        value = (
            value.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", ""))
        if value.isdigit() and len(value) == 12:
            self.value = value
        else:
            print('Wrong phone number format. Try "+XX(XXX)XXX-XX-XX"')
            self.value = None


class Field:
    pass
