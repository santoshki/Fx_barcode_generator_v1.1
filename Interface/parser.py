import yaml
import pathlib
import os

current_directory = pathlib.Path(__file__).parent
yaml_filepath = os.path.dirname(current_directory) + "\\database\\config.yaml"
print(yaml_filepath)


def dbpath_parse():
    with open(yaml_filepath, "r") as stream:
        try:
            data = yaml.safe_load(stream)
            db_path = data["db_path"]
            return db_path
        except Exception as e:
            print("Exception occurred while parsing db path value:", e)
            return -1


def dbnames_parse():
    with open(yaml_filepath, "r") as stream:
        try:
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



