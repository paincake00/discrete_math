from task12_20 import Task12_20
from task12_23 import Task12_23

input_file = "input.txt"
output_file  = "output.txt"

def change_input_file():
    input_file = input("Enter new input file name (without extension): ") + 'txt'

def change_output_file():
    output_file = input("Enter new output file name (without extension): ") + 'txt'

def task12_20():
    Task12_20(input_file, output_file).solution()

def task12_23():
    Task12_23(input_file, output_file).solution()

if __name__ == "__main__":
    RULES = """
    <?> input promts:
    0 - task 12.20
    1 - task 12.23
    2 - change input file
    3 - change output file
    exit - exit from program
    """

    dict_promt = {
        '0': "task12_20()",
        '1': "task12_23()",
        '2': "change_input_file()",
        '3': "change_output_file()",
        'exit': "exit()"
    }    

    print(RULES)
    while True:
        inp = input("Enter command: ")
        if (inp in dict_promt.keys()):
            eval(dict_promt.get(inp))
        else:
            print("Incorrect command. Repeat plz!")