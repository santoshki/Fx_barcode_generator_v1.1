import datetime


def get_cal_year():
    print("Get calendar year function")
    today = datetime.date.today()
    year = today.strftime("%Y")
    year_last_digits_value = int(year) % 100
    return year_last_digits_value
