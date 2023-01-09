def phone_number_validation(phone):
    phone = str(phone)
    phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", ""))
    if phone.isdigit() and len(phone) == 12:
        phone = phone
    else:
        print(f"Phone {phone} is not saved!\nWrong phone number format! Try '+XX(XXX)XXX-XX-XX'")
        phone = None
    return phone
