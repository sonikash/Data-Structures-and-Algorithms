class InsertionSort:
    def __init__(self,items):
        self.items=items

    def sort(self):
        for i in range(1,len(self.items)):
            j=i
            while self.items[j-1]>self.items[j] and j>0:
                self.items[j-1],self.items[j]=self.items[j],self.items[j-1]
                j-=1



if __name__ == '__main__':
    elements=[4,3,2,1,99,24,34,12,78]
    insert=InsertionSort(elements)
    insert.sort()
    print(elements)

