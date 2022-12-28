import sqlite3
import pathlib

current_dir = pathlib.Path(__file__).parent


def db_insert(book_category_value, sequence_count_value):
    db_name = str(book_category_value) + ".db"
    print("dbname:", db_name)
    print("Sequence count value:", sequence_count_value)
    db_path = str(current_dir)
    conn = sqlite3.connect(db_path + "\\" + db_name)
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='sequence_counter_value' 
        ''')
        if cursor.fetchone()[0] == 0:
            table_create = """CREATE TABLE sequence_counter_value(COUNT TEXT)"""
            cursor.execute(table_create)
            conn.commit()
            print("Table created in SQLlite DB.")

        cursor.execute("INSERT INTO sequence_counter_value(COUNT)" "VALUES(?)", (str(sequence_count_value),))
        #cursor.execute("UPDATE sequence_counter_value SET COUNT = ?", str(sequence_count_value))
        conn.commit()
        print("Data inserted/updated in SQL lite db")

    except Exception as e:
        print("Exception occurred in dbconfig:", e)
        return 0


if __name__ == '__main__':
    book_category = "Kids"
    sequence_count_value = "0"
    db_insert(book_category, sequence_count_value)
