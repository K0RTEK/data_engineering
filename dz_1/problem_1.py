import ast

from typing import Dict, List

def get_purchase_log_dict(file_path: str) -> Dict[str, str]:
    with open(file_path, mode="r", encoding="utf-8") as f:
        file: List[str] = f.readlines()
        purchases: Dict[str, str]= {}
        for line in file[1:]:
            dict_line: Dict[str, str] = ast.literal_eval(line)
            purchases[dict_line["user_id"]] = dict_line["category"]

    return purchases

if __name__ == "__main__":
    purchases = get_purchase_log_dict("dz_1/dz_files/purchase_log.txt")

    for counter, (user_id, category) in zip(range(3), purchases.items()):
        if counter == 2:
            break
        else:
            print(user_id, category)