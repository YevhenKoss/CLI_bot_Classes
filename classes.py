from collections import UserDict
from validation import *


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()
        self.index = None

    def add_record(self, record):
        self.index = len(self.data) + 1
        self.data[self.index] = record

    def show(self, start=1, end=1):
        if start <= end <= len(self.data):
            while start <= end:
                record = self.data[start]
                if record.phones and record.birthday:
                    yield f"{record.name}: {record.phones}, {record.birthday}"
                elif record.phones and not record.birthday:
                    yield f"{record.name}: {record.phones}"
                elif record.birthday and not record.phones:
                    yield f"{record.name}: {record.birthday}"
                else:
                    yield f"{record.name}"
                start += 1
        else:
            print(f"Value 'end' {end} is more than numbers of Address Book")

    def __repr__(self):
        return f"{self.data}"

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        keys = tuple(self.data.keys())
        if self.index == len(self):
            raise StopIteration
        key = keys[self.index]
        record = self.data[key]
        self.index += 1
        if record.phones and record.birthday:
            return f"{record.name}: {record.phones}, {record.birthday}"
        elif record.phones and not record.birthday:
            return f"{record.name}: {record.phones}"
        elif record.birthday and not record.phones:
            return f"{record.name}: {record.birthday}"
        else:
            return f"{record.name}"


class Record:

    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday

    def __repr__(self):
        if self.phones and self.birthday:
            return f"{self.name.name}, {self.phones}, {self.birthday}"
        elif self.phones and not self.birthday:
            return f"{self.name.name}, {self.phones}"
        elif self.birthday and not self.phones:
            return f"{self.name.name}, {self.birthday}"
        else:
            return f"{self.name.name}"

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
        print(f"This is {self.name}"+"'s "+"contact.")
        if self.birthday is not None:
            self.birthday = self.birthday.birthday
            today = date.today()
            dob_data = self.birthday.split(".")
            dob_day = int(dob_data[0])
            dob_month = int(dob_data[1])
            this_year = today.year
            next_birthday = date(this_year, dob_month, dob_day)
            if today < next_birthday:
                gap = (next_birthday - today).days
                print("This abonent birhday is in " + str(gap) + " days.")
            elif today == next_birthday:
                print("Today is abonent's birthday! Happy Birthday!")
            else:
                next_birthday = date(this_year + 1, dob_month, dob_day)
                gap = (next_birthday - today).days
                print("This abonent birthday is in " + str(gap) + " days.")
        else:
            print("Current contact doesn't have date of birth")


class Name:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class Fild:
    pass


class Phone(Fild):

    def __init__(self, value):
        self.__value = phone_number_validation(value)

    def __repr__(self):
        return f"{self.__value}"

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = phone_number_validation(new_value)


class Birthday(Fild):

    def __init__(self, birthday):
        self.__birthday = birthday_validation(birthday)

    def __repr__(self):
        return f"{self.__birthday}"

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday_validation(birthday)
