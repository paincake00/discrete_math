class Sort_algorithms:

    def insertion_sort(self, list):
        countComparing = 0

        for i in range(1, len(list)):
            temp = list[i]
            j = i - 1
            while (j >= 0) and (list[j] > temp):
                list[j+1] = list[j]
                j-=1
                countComparing += 1
            list[j+1] = temp
        return countComparing
    
    def bubble_sort(self, list):
        countComparing = 0

        for i in range(1, len(list)):
            for j in range(len(list)-1, i-1, -1):
                if (list[j-1] > list[j]):
                    countComparing += 1
                    list[j-1], list[j] = list[j], list[j-1]
        return countComparing
    
    def selection_sort(self, list):
        countComparing = 0

        for i in range(i, len(list)):
            k = i
            temp = list[k]
            for j in range(i+1, len(list)):
                if list[j] < temp:
                    k = j
                    temp = list[k]
                    countComparing += 1
            list[k] = list[i]
            list[i] = temp        
        return countComparing
    
    def shaker_sort(self, list):
        countComparing = 0

        left = 0
        right = len(list) - 1
        while left < right:
            for i in range(left, right):
                if list[i] > list[i+1]:
                    list[i], list[i+1] = list[i+1], list[i]
                    countComparing += 1
            right -= 1
            for i in range(right, left, -1):
                if list[i-1] > list[i]:
                    list[i-1], list[i] = list[i], list[i-1]
                    countComparing += 1
            left += 1
        return countComparing

    def shell_sort(self, arr, h):
        count = 0

        gap = len(arr) // h - 1

        while gap > 0:
            j = gap
            while j < len(arr):
                i = j - gap

                while i >= 0:
                    count += 1
                    if arr[i + gap] > arr[i]:

                        break
                    else:
                        arr[i + gap], arr[i] = arr[i], arr[i + gap]

                    i = i - gap
                j += 1
            gap = gap // h - 1

        return count

    def sortOfPart(self, arr, left, right, counter):
        pivot = arr[(left + right) // 2]
        while left <= right:
            while arr[left] < pivot: 
                left += 1
                counter[0] += 1
            while arr[right] > pivot: 
                right -= 1
                counter[0] += 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return left

    def quickSort(self, list, start, end, countComparing):
        if start < end: 
            right = self.sortOfPart(list, start, end, countComparing)
            self.quickSort(list, start, right-1, countComparing)
            self.quickSort(list, right, end, countComparing)