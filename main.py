from task12_20 import Task12_20
from task12_23 import Task12_23
from task12_28 import Task12_28
from task12_50 import Task12_50
from task12_43 import Task12_43

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

def task12_28():
    Task12_28(input_file, output_file).solution()

def task12_50():
    Task12_50(input_file, output_file).solution()

def task12_43():
    Task12_43(input_file, output_file).solution()    

if __name__ == "__main__":
    RULES = """
    <?> input promts:
    0 - task 12.20 (Algorithms of searching)
    1 - task 12.23 (Insertion sort)
    2 - task 12.28 (Shaker sort)
    3 - task 12.50 (Quick sort)
    4 - task 12.43 (Shell sort)
    inp - change input file
    out - change output file
    exit - exit from program
    """

    dict_promt = {
        '0': "task12_20()",
        '1': "task12_23()",
        '2': "task12_28()",
        '3': "task12_50()",
        '4': "task12_43()",
        'inp': "change_input_file()",
        'out': "change_output_file()",
        'exit': "exit()"
    }    

    print(RULES)
    while True:
        inp = input("Enter command: ")
        if (inp in dict_promt.keys()):
            eval(dict_promt.get(inp))
        else:
            print("Incorrect command. Repeat plz!")