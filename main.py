class BubbleSort:
    def __init__(self,items):
        self.items=items

    def bubblesort(self):

        for i in range(len(self.items)-1):
            swapped= False
            for j in range(len(self.items)-1-i):
                if self.items[j]>self.items[j+1]:
                    temp= self.items[j]
                    self.items[j]=self.items[j+1]
                    self.items[j+1]=temp
                    swapped=True
            if not swapped:
                break


if __name__ == '__main__':
    elements=[23,78,55,9,89,12,3,44,39,65]
    bubble = BubbleSort(elements)
    bubble.bubblesort()
    print(elements)