from barcode import EAN13
from barcode.writer import ImageWriter
from Interface import actioninterface
from database import dbread, dbinsert
import pathlib
import os
from entities import entity

current_directory = pathlib.Path(__file__).parent
directory_save_loc = os.path.dirname(current_directory)

def generate_barcode(society_names_dropdown_value, book_category_dropdown_value, barcode_count_value):
    sequence_count = dbread.db_read(book_category_dropdown_value)
    print("Current sequence count:", sequence_count)
    if sequence_count != -1:
        #dbconfig.db_insert(book_category_dropdown_value, barcode_count_value)
        new_sequence_count_value = sequence_count + int(barcode_count_value)
        print("new sequence count value:", new_sequence_count_value)

        print("Generating barcode(s)..")
        book_identifier_sequence_value = str(int(sequence_count)).zfill(3)

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
        for i in range(sequence_count, int(new_sequence_count_value)):
            book_identifier_sequence_value = str(int(book_identifier_sequence_value) + 1).zfill(3)
            barcode_number = str(society_name_phrase_value) + str(year_last_digits_value) + str(dewey_decimal_value) + \
                             str(book_identifier_sequence_value)
            print("Barcode number:", barcode_number)
            generated_barcode = EAN13(str(barcode_number), writer=ImageWriter())
            barcode_value = str(barcode_number)
            barcode_save_directory = str(directory_save_loc) + "\\Generated Barcodes"
            barcode_save_path = barcode_save_directory + "\\" + str(book_category_dropdown_value)
            barcode_save_value = barcode_save_path + "\\" + barcode_value
            try:
                if os.path.exists(barcode_save_directory):
                    pass
                else:
                    os.mkdir(barcode_save_directory)
                    print("Generated Barcodes Directory created successfully.")
                if os.path.exists(barcode_save_path):
                    pass
                else:
                    os.mkdir(barcode_save_path)
                    print(str(book_category_dropdown_value) + " folder created successfully.")
                generated_barcode.save(barcode_save_value)
            except Exception as e:
                print("Exception occurred while saving the barcode:", e)

            print(str(i) + " Barcodes generated and saved successfully.")
            print("new sequence count value:", new_sequence_count_value)
        dbinsert.db_insert(book_category_dropdown_value, int(new_sequence_count_value))
        action_complete_frame = entity.ActionComplete()
        action_complete_frame.Show()

