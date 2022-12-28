import datetime


def get_cal_year():
    print("Get calendar year function")
    try:
        today = datetime.date.today()
        year = today.strftime("%Y")
        year_last_digits_value = int(year) % 100
        return year_last_digits_value
    except Exception as e:
        print("Exception occurred while computing calendar year values:", e)
        return -1

