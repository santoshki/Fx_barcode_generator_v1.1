import yaml
import pathlib
import os

current_directory = pathlib.Path(__file__).parent
yaml_filepath = os.path.dirname(current_directory) + "\\database\\config.yaml"
print(yaml_filepath)


def society_names_parser():
    try:
        society_names_keys = []
        society_names_values = []
        society_names_enable = []
        with open(yaml_filepath, "r") as stream:
            data = yaml.safe_load(stream)
            society_names = data["society names"]
            society_names_count = len(society_names)
            print("Number of Societies:", society_names_count)
            for i in society_names:
                society_names_keys.append(i)
                society_names_values.append(society_names[i])
            for j in range(0, society_names_count):
                if society_names_values[j] == "True":
                    society_names_enable.append(society_names_keys[j])
            return society_names_enable

    except Exception as e:
        print("Exception occurred while parsing Society name values:", e)
        return -1


def book_category_parser():
    try:
        book_category_keys = []
        book_category_values = []
        book_category_enable = []
        with open(yaml_filepath, "r") as stream:
            data = yaml.safe_load(stream)
            book_categories = data["book categories"]
            book_category_count = len(book_categories)
            print("Number of Book categories:", book_category_count)
            for i in book_categories:
                book_category_keys.append(i)
                book_category_values.append(book_categories[i])
            for j in range(0, book_category_count):
                if book_category_values[j] == "True":
                    book_category_enable.append(book_category_keys[j])
            return book_category_enable
    except Exception as e:
        print("Exception occurred while parsing Book category values:", e)
        return -1

def dbpath_parse():
    try:
        with open(yaml_filepath, "r") as stream:
            data = yaml.safe_load(stream)
            db_path = data["db_path"]
            return db_path
    except Exception as e:
        print("Exception occurred while parsing db path value:", e)
        return -1


def dbnames_parse():
    try:
        with open(yaml_filepath, "r") as stream:
            db_names_list = []
            db_names_values = []
            db_enable = []
            data = yaml.safe_load(stream)
            db_names = data["dbnames"]
            print("Total number of Dbs:", len(db_names))
            for i in db_names:
                db_names_list.append(i)
                db_names_values.append(db_names[i])

            for j in range(0, len(db_names_values)):
                if db_names_values[j] == "True":
                    db_enable.append(db_names_list[j])
            print("Dbs enabled:", db_enable)
            return db_enable
    except Exception as e:
        print("Exception occurred while parsing dbnames value:", e)
        return -1


def dewey_decimal_parser(book_category):
    try:
        dewey_decimal_keys = []
        dewey_decimal_values = []
        with open(yaml_filepath, "r") as stream:
            data = yaml.safe_load(stream)
            dewey_decimals = data["dewey decimals"]
            dewey_decimal_values_count = len(dewey_decimals)
            print("Number of Dewey decimal values:", dewey_decimal_values_count)
            for i in dewey_decimals:
                dewey_decimal_keys.append(i)
                dewey_decimal_values.append(dewey_decimals[i])

            for j in range(0, dewey_decimal_values_count):
                if str(book_category) == str(dewey_decimal_keys[j]):
                    print("Dewey Decimal value:", dewey_decimal_values[j])
                    return dewey_decimal_values[j]
                elif j > dewey_decimal_values_count:
                    return -2
    except Exception as e:
        print("Exception occurred while parsing dewey decimal values:", e)
        return -1


if __name__ == '__main__':
    dewey_decimal_parser("Literature")
