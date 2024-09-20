class SelectionSort:
    def __init__(self,items):
        self.items=items

    def sort(self):
        size = len(self.items)
        for i in range(size-1):
            min_index=i
            for j in range(i+1,size):
                if self.items[j]<self.items[min_index]:
                    min_index=j
            if i!=j:
                self.items[i],self.items[min_index]=self.items[min_index],self.items[i]


if __name__ == '__main__':
    elements =[2,6,5,1,3,4]
    selection =SelectionSort(elements)
    selection.sort()
    print(elements)

