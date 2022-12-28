from barcode import EAN13
from barcode.writer import ImageWriter
import datetime
import pathlib
import os

"""society_name = input("Enter society name:")
book_category = input("Enter book category:")
barcode_count = input("Enter the number of barcodes to be generated:")
society_name_phrase_value = "0000"
dewey_decimal_value = "000"
book_identifier_sequence_value = "000"

if "Norwood" in society_name:
    society_name_phrase_value = "8917"

today = datetime.date.today()
year = today.strftime("%Y")
year_last_digits_value = int(year) % 100

if "Technology" in book_category:
    dewey_decimal_value = "006"
elif "Literature" in book_category:
    dewey_decimal_value = "008"
for i in range(0, int(barcode_count)):
    book_identifier_sequence_value = str(int(book_identifier_sequence_value) + 1).zfill(len(book_identifier_sequence_value))
    barcode_number = str(society_name_phrase_value) + str(year_last_digits_value) + str(dewey_decimal_value) + \
                     str(book_identifier_sequence_value)

    print("Barcode number:", barcode_number)
    generated_barcode = EAN13(str(barcode_number), writer=ImageWriter())
    name = "barcode" + str(i)
    generated_barcode.save(name)
    print("Barcode" + str(i) + "generated and saved successfully.")"""

if __name__ == '__main__':
    current_dir = pathlib.Path(__file__).parent
    print("Current location:", current_dir)
    sav_dir = os.path.dirname(current_dir)
    print(sav_dir)
    directory = "\Test_folder"
    path = str(sav_dir) + directory
    try:
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)
            print("Folder created successfully.")
    except OSError as error:
        print(error)
