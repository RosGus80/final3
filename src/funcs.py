import json


def load_data(path):
    """Returns a list from a json file. Argument must be a string with the path to a file"""
    with open(path) as file:
        data = json.load(file)
    return data

def select_latest(list):
    """Takes a list with operations and returns a list only with last five executed ones"""
    sorted_list = sorted(list, key=lambda x: x.get('date', "0000-00-00T00:00:00.000000"), reverse=True)
    output = []
    i = 0
    while i < 5:
        if sorted_list[i]["state"] == "EXECUTED":
            output.append(sorted_list[i])
            i += 1
        else:
            del(sorted_list[i])
    return output

def print_operation(dict):
    """Takes a dictionary with operation info as input and prints info about it"""
    output = ""
    if "date" in dict.keys():
        output += f"{dict['date'][8:10]}.{dict['date'][5:7]}.{dict['date'][:4]} "

    output += dict['description']

    if "from" in dict.keys():
        from_ = dict["from"].split(" ")
        index = 0
        for i in range(len(from_)):
            if from_[i].isdigit():
                index = i
                break
        output += "\n"
        output += f"{' '.join(from_[0:index])}"
        output += f"{from_[index][:4]} {from_[index][5:7]}** {'*'*4} {from_[index][-4:]} "

    output += f"-> Счет **{dict['to'][-4:]}"

    output += "\n"
    output += f"{dict['operationAmount']['amount']} {dict['operationAmount']['currency']['name']}"
    return output


