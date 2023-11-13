from file_manager import File_manager
from sort_algorithms import Sort_algorithms
import itertools

class Task12_50:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def solution(self):
        File_manager().file_write(file_name=self.output_file, text='', mode='w')
        input_list = list([int(x) for x in File_manager().file_read(file_name=self.input_file).split(" ")])
        n = len(input_list)
        count_comparing = [0]
        Sort_algorithms().quickSort(input_list, 0, len(input_list)-1, count_comparing)

        File_manager().file_write(file_name=self.output_file, text="list: " + str(input_list) + "\n", mode='a')
        File_manager().file_write(file_name=self.output_file, text="avg comparing for quick sort: " + str(count_comparing[0] / n) + "\n", mode='a')
        # n = int(File_manager().file_read(file_name=self.input_file))
        # input_list = list(range(1, n+1))
        # for x in itertools.permutations(input_list):
        #     inp = list(x)
        #     count_comparing = [0]
        #     Sort_algorithms().quickSort(inp, 0, len(x)-1, count_comparing)
        #     File_manager().file_write(file_name=self.output_file, text="list: " + str(x) + "\n", mode='a')
        #     File_manager().file_write(file_name=self.output_file, text="comparing for quick sort: " + str(count_comparing[0]) + "\n", mode='a')
        print(File_manager().file_read(file_name=self.output_file))