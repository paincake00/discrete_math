from file_manager import File_manager
from sort_algorithms import Sort_algorithms

class Task12_23:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def solution(self):
        File_manager().file_write(file_name=self.output_file, text='', mode='w')
        input_list = list([int(x) for x in File_manager().file_read(file_name=self.input_file).split(" ")])
        n = len(input_list)
        sum_of_comparing = Sort_algorithms().insertion_sort(input_list)

        File_manager().file_write(file_name=self.output_file, text="list: " + str(input_list) + "\n", mode='a')
        File_manager().file_write(file_name=self.output_file, text="avg insertion sort: " + str(sum_of_comparing / n) + "\n", mode='a')
        print(File_manager().file_read(file_name=self.output_file))