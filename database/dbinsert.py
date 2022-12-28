import sqlite3
import pathlib

current_dir = pathlib.Path(__file__).parent


def db_insert(book_category_value, sequence_count_value):
    db_name = str(book_category_value) + ".db"
    print("dbname:", db_name)
    # print("Sequence count value:", sequence_count_value)
    db_path = str(current_dir)
    conn = sqlite3.connect(db_path + "\\" + db_name)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO sequence_counter_value(COUNT)" "VALUES(?)", (str(sequence_count_value),))
        conn.commit()
        print("Data inserted/updated in SQL lite db")

    except Exception as e:
        print("Exception occurred while inserting values in the db:", e)
