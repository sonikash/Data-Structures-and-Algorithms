class BubbleSort:
    def __init__(self,items):
        self.items = items

    def sort(self):
        size= len(self.items)
        for i in range(size-1):
            swapped = False
            for j in range(size-1-i):
                if self.items[j]>self.items[j+1]:
                    temp=self.items[j]
                    self.items[j]=self.items[j+1]
                    self.items[j+1]=temp
                    swapped=True
            if not swapped:
                break


if __name__ == '__main__':
    elements=[34,11,9,67,100,65,45,39,5,99]
    bubble=BubbleSort(elements)
    bubble.sort()
    print(elements)


