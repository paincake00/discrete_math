class Search_algorithms:

    def linear_search_comparing(self, list, target, showCountComparing=False):
        countComparing = 0
        for i in range(0, len(list)):
            countComparing += 1
            if list[i] == target:
                return countComparing if showCountComparing else i   
        return countComparing if showCountComparing else -1
    
    def binary_search_comparing(self, list, target, showCountComparing=False):
        low = 0
        high = len(list)-1
        countComparing = 0

        while low <= high:
            mid = (low+high)//2
            guess = list[mid]
            countComparing += 1
            if guess == target:
                return countComparing if showCountComparing else mid
            if guess > target:
                high = mid-1
            else:
                low = mid+1
        return countComparing if showCountComparing else -1
    
    def interpolation_search_comparing(self, list, target, showCountComparing=False):
        countComparing = 0
        low = 0
        high = len(list)-1
        target = int(target)

        while (low <= high) and (target >= int(list[low])) and (target <= int(list[high])):
            countComparing += 1
            if low == high:
                if int(list[low]) == target:
                    return countComparing if showCountComparing else low
                return countComparing if showCountComparing else high
            
            pos = low+((target-int(list[low])) * (high-low)) // (int(list[high])-int(list[low]))

            if int(list[pos]) == target:
                return countComparing if showCountComparing else pos
            elif int(list[pos]) < target:
                low = pos + 1
            else:
                high = pos - 1
        return countComparing if showCountComparing else -1