class Sort_algorithms:

    def insertion_sort(self, list):
        countComparing = 0

        for i in range(1, len(list)):
            item = list[i]
            j = i - 1
            while (j >= 0) and (list[j] > item):
                list[j+1] = list[j]
                j-=1
                countComparing += 1
            list[j+1] = item
        return countComparing