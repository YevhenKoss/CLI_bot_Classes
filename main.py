from classes import *

if __name__ == '__main__':
    name = Name("Bill")
    phone = Phone("+380971111111")
    bd = Birthday("01.01.1991")
    rec = Record(name, phone, bd)
    # print(rec)

    name1 = Name("Jill")
    phone1 = Phone("+380972222222")
    bd1 = Birthday("02/02/1992")
    rec1 = Record(name1, phone1, bd1)
    # print(rec1)

    name2 = Name("Dill")
    phone2 = Phone("+380972222222")
    rec2 = Record(name2, phone2)
    # print(rec2)

    ab = AddressBook()
    ab.add_record(rec)
    ab.add_record(rec1)
    ab.add_record(rec2)
    # print(ab)

    # for i in ab:
    #     print(i)

    # show = ab.show(1, 3)
    # for i in show:
    #     print(i)

    phone3 = Phone("38097-333-33-33")
    rec2.add(phone3)

    # print(ab)

    show = ab.show(1, 3)
    for i in show:
        print(i)

    print("\n--------------------\n")

    rec1.days_to_birthday()


