from usecase import actions
from entities import entity


def exit_app_action(self):
    print("Exit button pressed.\nExiting the application....")
    exit()


def about_app_action(self):
    print("About button pressed.\nDetails about the application")


def barcode_generation(society_names_dropdown_value, book_category_dropdown_value, barcode_count_value):
    print("Generate button pressed.\nGathering user provided information.....")
    print("Society name value:", society_names_dropdown_value)
    print("Book category dropdown value:", book_category_dropdown_value)
    print("Number of barcodes to be generated:", barcode_count_value)
    if barcode_count_value > 0:
        actions.generate_barcode(society_names_dropdown_value, book_category_dropdown_value, barcode_count_value)
