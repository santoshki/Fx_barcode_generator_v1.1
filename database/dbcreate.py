import sqlite3
import pathlib

current_dir = pathlib.Path(__file__).parent


def db_create(book_category_value, sequence_count_value):
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
            print("Table created in SQL lite DB.")
        else:
            print("Db already exists with the Count table.")
    except Exception as e:
        print("Exception occurred while creating db and table:", e)