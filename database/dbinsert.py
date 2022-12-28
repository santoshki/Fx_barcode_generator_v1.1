import sqlite3
import pathlib
from Interface import parser

current_dir = pathlib.Path(__file__).parent


def db_insert(book_category_value, sequence_count_value):
    db_name = str(book_category_value) + ".db"
    print("dbname:", db_name)
    db_path_value = parser.dbpath_parse()
    if db_path_value != -1:
        db_path = str(current_dir) + str(db_path_value)
        conn = sqlite3.connect(db_path + "\\" + db_name)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO sequence_counter_value(COUNT)" "VALUES(?)", (str(sequence_count_value),))
            conn.commit()
            print("Data inserted/updated in SQL lite db")

        except Exception as e:
            print("Exception occurred while inserting values in the db:", e)
    else:
        print("Unable to create db due to error in fetching db location from the parser file.")
