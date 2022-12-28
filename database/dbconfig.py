import dbcreate
from Interface import parser

if __name__ == '__main__':
    book_category = parser.dbnames_parse()
    if book_category != -1:
        sequence_count_value = "0"
        for i in range(0, len(book_category)):
            dbcreate.db_create(book_category[i], sequence_count_value)
    else:
        print("Unable to configure db due to issues in parsing config.yaml file.")
