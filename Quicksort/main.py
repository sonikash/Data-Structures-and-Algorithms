class QuickSort:
    def __init__(self,items):
        self.items = items

    def sort(self,left,right):
        if left<right:
            partition_pos = self.partition(left,right)
            self.sort(left,partition_pos-1)
            self.sort(partition_pos+1,right)


    def partition(self,left,right):
        i=left
        j=right-1
        pivot=self.items[right]
        while i<j: # to ensure i has crossed j and its time to swap i and pivot element
            while i<right and self.items[i]<pivot: # to find element greater than pivot element
                i=i+1
            while j>left and self.items[j]>pivot:# to find element less than pivot element
                j=j-1

            if i<j:
                self.items[i],self.items[j]= self.items[j],self.items[i] # found the lesser than and greater than element wrt pivot swap both

        if self.items[i]>pivot:
            self.items[i],self.items[right] = self.items[right], self.items[i] # swap pivot and i element if i has crossed j

        return i



if __name__ == '__main__':
    elements=[22,11,88,66,55,77,33,44]
    quick = QuickSort(elements)
    quick.sort(0,len(elements)-1)
    print (elements)

