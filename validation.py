from datetime import datetime


def phone_number_validation(phone):
    if isinstance(phone, str):
        phone = phone
    else:
        phone = str(phone)
    phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    if phone.isdigit() and len(phone) == 12:
        phone = phone
    else:
        raise ValueError(
            f"Phone {phone} is not saved!\nWrong phone number format! Try '+XX(XXX)XXX-XX-XX'"
        )
    return phone


def birthday_validation(birthday):
    # birthday = str(birthday)
    # birthday = (
    #     birthday.strip()
    #     .replace("/", ".")
    #     .replace("-", ".")
    #     .replace(" ", "."))
    # dob_data = birthday.split(".")
    # today = date.today().year
    # if dob_data[0].isdigit() and 0 < int(dob_data[0]) <= 31:
    #     if dob_data[1].isdigit() and 0 < int(dob_data[1]) <= 12:
    #         if dob_data[2].isdigit() and 0 < int(dob_data[2]) <= today and len(dob_data[2]) == 4:
    #             birthday = birthday
    #             return birthday
    try:
        return datetime.strptime(str(birthday), "%d.%m.%Y").date()
    except ValueError:
        return f"Date of birth {birthday} is not saved!\nYou have to enter numbers separated by a dot: DD.MM.YYYY"


if __name__ == "__main__":
    print(birthday_validation("10.12.1985"))
    print(birthday_validation("10-12-1985"))
