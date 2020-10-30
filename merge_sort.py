# Merge Sort implementation with Python

class MergeSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        def merge(l1, l2):
            result = []

            # while BOTH lists still have elements
            while l1 and l2:
                if (l1[0] > l2[0]):
                    result.append(l2[0])
                    l2.remove(l2[0])
                else:
                    result.append(l1[0])
                    l1.remove(l1[0])

            while l1:  # when only l1 has elements
                result.append(l1[0])
                l1.remove(l1[0])

            while l2:  # when only l2 has elements
                result.append(l2[0])
                l2.remove(l2[0])

            print(result)  # only to display in console
            return result

        def divide(arr):
            size = len(arr)
            if size == 1:
                return arr
            # splitting the list in two
            # first half (list)
            l1 = arr[slice(0, int(size / 2))]
            # second half (list)
            l2 = arr[slice(int((size / 2)), size)]

            l1 = divide(l1)
            l2 = divide(l2)

            return merge(l1, l2)

        divide(self.array)  # initialize the algorithm
