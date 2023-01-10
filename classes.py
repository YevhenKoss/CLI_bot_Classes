from collections import UserDict
from datetime import datetime

from validation import *


class Field:
    def __init__(self, value) -> None:
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __repr__(self) -> str:
        return f"{self.value}"

    def __str__(self) -> str:
        return f"{self.value}"

    def __eq__(self, __o: object) -> bool:
        if self.value == __o.value:
            return True
        return False


class Name(Field):
    pass


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = phone_number_validation(value)


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = birthday_validation(value)


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday

    def __repr__(self):
        # if self.phones and self.birthday:
        return f"{self.name.value} {','.join([p.value for p in self.phones]) if self.phones else ''} {self.birthday if self.birthday else ''}"
        # elif self.phones and not self.birthday:
        #     return f"{self.name.name}, {self.phones}"
        # elif self.birthday and not self.phones:
        #     return f"{self.name.name}, {self.birthday}"
        # else:
        #     return f"{self.name.name}"

    def add(self, phone: Phone):
        if isinstance(phone, Phone):
            self.phones.append(phone)
        return f"phone {phone.value} add successful to contact {self.name.value}"

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
        # print(f"This is {self.name}"+"'s "+"contact.")
        if self.birthday:
            # self.birthday = self.birthday.birthday ???????
            today = datetime.today()
            # dob_data = self.birthday.split(".")
            # dob_day = int(dob_data[0])
            # dob_month = int(dob_data[1])
            # this_year = today.year
            next_birthday = self.birthday.value.replace(year=today.year)
            if today < next_birthday:
                gap = (next_birthday - today).days
                return "This contacts birthday is in " + str(gap) + " days."
            elif today == next_birthday:
                return "Today is contacts's birthday! Happy Birthday!"
            else:
                next_birthday = self.birthday.value.replace(year=today.year + 1)
                gap = (next_birthday - today).days
                return "This contacts birthday is in " + str(gap) + " days."
        else:
            return "Current contact doesn't have date of birth"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.index = None

    def add_record(self, record: Record):
        self.index = len(self.data) + 1
        self.data[record.name.value] = record

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


if __name__ == "__main__":
    ab = AddressBook()
    name1 = Name("Bill")
    phone1 = Phone("+380996787878")
    rec1 = Record(name1, phone1)

    rec2 = Record(Name("Jill"), Phone("+389671234545"), Birthday("12.03.1995"))

    ab.add_record(rec1)
    ab.add_record(rec2)

    phone3 = Phone("0453423434")  # This line must rise exceptions!

    rec1.add(phone3)

    phone4 = Phone("+380996787878")
    phone5 = Phone("+380667877676")

    rec1.edit(phone4, phone5)

    print(ab)
