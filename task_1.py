def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def validate_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        if 1 <= year <= 9999:
            if 1 <= month <= 12:
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    if 1 <= day <= 31:
                        return True
                elif month in [4, 6, 9, 11]:
                    if 1 <= day <= 30:
                        return True
                elif month == 2:
                    if is_leap_year(year):
                        if 1 <= day <= 29:
                            return True
                    else:
                        if 1 <= day <= 28:
                            return True

    except ValueError:
        pass

    return False


if __name__ == "__main__":
    date_str = input("Введите дату в формате DD.MM.YYYY: ")
    if validate_date(date_str):
        print("Дата корректна.")
    else:
        print("Дата некорректна.")