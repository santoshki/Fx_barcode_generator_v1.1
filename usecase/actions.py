from barcode import EAN13
from barcode.writer import ImageWriter
from Interface import actioninterface

def generate_barcode(society_names_dropdown_value, book_category_dropdown_value, barcode_count_value):
    print("Generating barcode(s)..")
    book_identifier_sequence_value = "000"
    if "Norwood" in society_names_dropdown_value:
        society_name_phrase_value = "8917"
    else:
        society_name_phrase_value = "8910"
    print("Mapping Dewey decimal values..")

    if "Kids" in book_category_dropdown_value:
        dewey_decimal_value = "000"
    elif "Philosophy" in book_category_dropdown_value:
        dewey_decimal_value = "001"
    elif "Religion" in book_category_dropdown_value:
        dewey_decimal_value = "002"
    elif "Social Sciences" in book_category_dropdown_value:
        dewey_decimal_value = "003"
    elif "Language" in book_category_dropdown_value:
        dewey_decimal_value = "004"
    elif "Science" in book_category_dropdown_value:
        dewey_decimal_value = "005"
    if "Technology" in book_category_dropdown_value:
        dewey_decimal_value = "006"
    elif "Arts" in book_category_dropdown_value:
        dewey_decimal_value = "007"
    elif "Literature" in book_category_dropdown_value:
        dewey_decimal_value = "008"
    elif "History, Geography" in book_category_dropdown_value:
        dewey_decimal_value = "009"

    year_last_digits_value = actioninterface.get_cal_year()
    for i in range(0, int(barcode_count_value)):
        book_identifier_sequence_value = str(int(book_identifier_sequence_value) + 1).zfill(
            len(book_identifier_sequence_value))

        barcode_number = str(society_name_phrase_value) + str(year_last_digits_value) + str(dewey_decimal_value) + \
                         str(book_identifier_sequence_value)

        print("Barcode number:", barcode_number)
        generated_barcode = EAN13(str(barcode_number), writer=ImageWriter())
        name = "barcode" + str(i)
        generated_barcode.save(name)
        print("Barcode" + str(i) + "generated and saved successfully.")









