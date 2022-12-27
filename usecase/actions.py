def generate_barcode(society_names_dropdown_value, book_category_dropdown_value, barcode_count_value):
    print("Generating barcode(s)..")
    if "Norwood" in society_names_dropdown_value:
        society_name_phrase_value = "8917"
    else:
        society_name_phrase_value = "8910"

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









