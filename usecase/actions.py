from barcode import EAN13
from barcode.writer import ImageWriter
from Interface import actioninterface
from database import dbread, dbinsert
import pathlib
import os
from entities import entity
from Interface import parser

current_directory = pathlib.Path(__file__).parent
directory_save_loc = os.path.dirname(current_directory)


def generate_barcode(society_names_dropdown_value, book_category_dropdown_value, barcode_count_value):
    try:
        sequence_count = dbread.db_read(book_category_dropdown_value)
        print("Current sequence count:", sequence_count)
        if sequence_count != -1:
            new_sequence_count_value = sequence_count + int(barcode_count_value)
            print("new sequence count value:", new_sequence_count_value)
            print("Generating barcode(s)..")
            book_identifier_sequence_value = str(int(sequence_count)).zfill(3)
            if "Norwood" in society_names_dropdown_value:
                society_name_phrase_value = "8917"
            else:
                society_name_phrase_value = "8910"
            print("Mapping Dewey decimal values..")

            dewey_decimal_value = parser.dewey_decimal_parser(book_category_dropdown_value)
            if dewey_decimal_value == -2:
                print("Error in mapping Dewey decimal values.")
            else:
                year_last_digits_value = actioninterface.get_cal_year()
                i = 0
                if int(year_last_digits_value) != -1:
                    for i in range(sequence_count, int(new_sequence_count_value)):
                        book_identifier_sequence_value = str(int(book_identifier_sequence_value) + 1).zfill(3)
                        barcode_number = str(society_name_phrase_value) + str(year_last_digits_value) + str(
                            dewey_decimal_value) + str(book_identifier_sequence_value)
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
                        print("new sequence count value:", new_sequence_count_value)
                    print(str(i) + " Barcode(s) generated and saved successfully.")
                    dbinsert.db_insert(book_category_dropdown_value, int(new_sequence_count_value))
                    action_complete_frame = entity.ActionComplete()
                    action_complete_frame.Show()
                else:
                    print("Unable to generate barcode values due to error in calendar function.")
        else:
            print("Unable to generate barcode values due to error in fetching sequence numbers from the db.\nPlease "
                  "check db configurations before proceeding further.")
    except Exception as e:
        print("Exception occurred while generating barcode values:", e)
