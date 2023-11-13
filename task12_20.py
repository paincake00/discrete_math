from file_manager import File_manager
from search_algorithms import Search_algorithms

class Task12_20:

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def solution(self):
        File_manager().file_write(file_name=self.output_file, text='', mode='w')
        input_list = File_manager().file_read(file_name=self.input_file).split(" ")
        n = len(input_list)
        sum_compare_linear = 0
        sum_compare_binary = 0
        sum_compare_interpolate = 0

        for i in input_list:
            sum_compare_linear += Search_algorithms().linear_search_comparing(list=input_list, target=i, showCountComparing=True)
            sum_compare_binary += Search_algorithms().binary_search_comparing(list=sorted(input_list), target=i, showCountComparing=True)
            sum_compare_interpolate += Search_algorithms().interpolation_search_comparing(list=sorted(input_list), target=i, showCountComparing=True)

        File_manager().file_write(file_name=self.output_file, text="avg linear: " + str(sum_compare_linear / n) + "\n", mode='a')
        File_manager().file_write(file_name=self.output_file, text="avg binary: " + str(sum_compare_binary / n) + "\n", mode='a')
        File_manager().file_write(file_name=self.output_file, text="avg interpolate: " + str(sum_compare_interpolate / n) + "\n", mode='a')

        print(File_manager().file_read(file_name=self.output_file))