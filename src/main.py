from funcs import *



def main():
    data = load_data("data.json")
    latest_list = select_latest(data)
    for operation in latest_list:
        print(print_operation(operation))
        print()

main()