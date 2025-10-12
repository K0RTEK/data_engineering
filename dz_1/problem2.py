import ast
import csv
import os

from typing import Dict, List

def get_purchase_log_dict(file_path: str) -> Dict[str, str]:
    with open(file_path, mode="r", encoding="utf-8") as f:
        file: List[str] = f.readlines()
        purchases: Dict[str, str]= {}
        for line in file[1:]:
            dict_line: Dict[str, str] = ast.literal_eval(line)
            purchases[dict_line["user_id"]] = dict_line["category"]

    return purchases


def join_purchases_with_visits(visits_file_path: str, purchases: Dict[str, str], dir_to_save: str = "/Users/kirill/Documents/data_engineering/dz_1/result_files/") -> None:
    if "funnel.csv" in os.listdir(dir_to_save):
            os.remove(f"{dir_to_save}funnel.csv")

    with open(visits_file_path, newline='') as csvfile:
        csv_file = csv.reader(csvfile, delimiter=',', quotechar='|')

        with open(f"{dir_to_save}funnel.csv", mode="w", encoding="utf-8") as f:
            f.write("user_id,source,category\n")

            for visit_log in csv_file:
                try:
                    f.write(f"{visit_log[0]},{visit_log[1]},{purchases[visit_log[0]]}\n")
                except:
                    pass


if __name__ == "__main__":
    purchases = get_purchase_log_dict("dz_1/dz_files/purchase_log.txt")
    join_purchases_with_visits('dz_1/dz_files/Visit Log.csv', purchases)

    with open("dz_1/result_files/funnel.csv", newline='') as csvfile:
        csv_file = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row_counter, line in zip(range(4), csv_file):
            if row_counter == 3:
                break
            else:
                print(",".join(line))