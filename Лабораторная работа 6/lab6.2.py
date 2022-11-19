'''
Реализовать конвертер из csv в json формат:

[{column -> value}, ... , {column -> value}]
название столбца — значение (аналог DictReader из модуля csv).
Для csv формата принять

разделитель между значениями, по умолчанию ","
разделитель строк, по умолчанию "\n".
Встроенным модулем csv пользоваться нельзя, json можно. В результате распечатать json строку с отступами равными 4.
'''
import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename) -> list[dict]:

    with open("input.csv") as csvfile:
        lines = csvfile.read().split('\n')
        json_list = []
        headers = lines[0].split(',')
        for i in range(1, len(lines)):
            current_dict = {}
            current_line = lines[i].split(',')
            for j in range(len(current_line)):
                current_dict[headers[j]] = current_line[j]
            json_list.append(current_dict)
    with open('data.json', 'w') as jsonfile:
        json.dump(json_list, jsonfile, indent=4)
    return json_list

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

