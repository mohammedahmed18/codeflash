import sys


class BubbleSorter:
    def __init__(self, x=0):
        self.x = x

    def sorter(self, arr):
        print("codeflash stdout : BubbleSorter.sorter() called")
        n = len(arr)
        for i in range(n):
            swapped = False  # Early exit if no elements were swapped
            for j in range(n - 1 - i):  # Skip the last i elements (already sorted)
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        print("stderr test", file=sys.stderr)
        return arr
