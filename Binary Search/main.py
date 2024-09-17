class BinarySearch:
    def __init__(self,items):
        self.items=items

    def search(self,val):
        mid=0
        start_pointer =0
        end_pointer=len(self.items)-1
        while start_pointer<=end_pointer:
            mid=(start_pointer+end_pointer)//2
            mid_number=self.items[mid]
            if mid_number==val:
                return mid
            if val>mid_number:
                start_pointer=mid+1
            else:
                end_pointer=mid-1

        return None

    def binary_search_recursive(self,items,val,start_pointer, end_pointer):
        if end_pointer<start_pointer:
            return -1
        mid = (start_pointer + end_pointer) // 2
        mid_number=items[mid]

        if mid_number==val:
            return mid
        if val>mid_number:
            start_pointer=mid+1
        else:
            end_pointer=mid-1

        return self.binary_search_recursive(items,val,start_pointer,end_pointer)




if __name__ == '__main__':
    element=[2,23,34,35,66,79,88,95,100,123]
    bin=BinarySearch(element)
    print(bin.search(34))
    print(bin.binary_search_recursive(element,66,0,len(element)-1))
    print(bin.search(100))

