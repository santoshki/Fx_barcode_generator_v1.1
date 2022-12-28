import sqlite3
import pathlib

current_dir = pathlib.Path(__file__).parent


def db_read(book_category_value):
    db_name = str(book_category_value) + ".db"
    print("dbname:", db_name)
    db_path = str(current_dir)
    conn = sqlite3.connect(db_path + "\\" + db_name)
    cursor = conn.cursor()
    try:
        data = cursor.execute('''SELECT * FROM sequence_counter_value''')
        val = " "
        for row in data:
            #print(row)
            for i in row:
                val = val + i
            #print(i)
        conn.commit()
        if val == " ":
            return 0
        else:
            return int(i)
    except Exception as e:
        print("Exception occurred while reading db values:", e)
        return -1

"""if __name__ == '__main__':
    book_category = "Kids"
    db_read(book_category)"""