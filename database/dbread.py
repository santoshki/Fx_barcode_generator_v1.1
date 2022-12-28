import sqlite3
import pathlib
from Interface import parser
current_dir = pathlib.Path(__file__).parent


def db_read(book_category_value):
    db_name = str(book_category_value) + ".db"
    print("dbname:", db_name)
    db_path_value = parser.dbpath_parse()
    if db_path_value != -1:
        db_path = str(current_dir) + str(db_path_value)
        conn = sqlite3.connect(db_path + "\\" + db_name)
        cursor = conn.cursor()
        try:
            data = cursor.execute('''SELECT * FROM sequence_counter_value''')
            val = " "
            for row in data:
                for i in row:
                    val = val + i
            conn.commit()
            if val == " ":
                return 0
            else:
                return int(i)
        except Exception as e:
            print("Exception occurred while reading db values:", e)
            return -1
    else:
        print("Unable to create db due to error in fetching db location from the parser file.")
