class MergeSort:

    def sort(self,arr):
        if len(arr)==1:
            return

        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        self.sort(left)
        self.sort(right)

        self.merge_two_sorted_list(left,right,arr)

    @staticmethod
    def merge_two_sorted_list(a,b,arr):

        len_a = len(a)
        len_b = len(b)
        i=j=k=0
        while i<len_a and j<len_b:
            if a[i]<b[j]:
                arr[k]=a[i]
                i+=1
            else:
                arr[k]=b[j]
                j+=1
            k+=1
        while i<len_a:
            arr[k]=a[i]
            i+=1
            k+=1

        while j<len_b:
            arr[k] = b[j]
            j+=1
            k+=1

if __name__ == '__main__':
    elements=[22,11,56,98,8,77,45,23,3]
    merge = MergeSort()
    merge.sort(elements)
    print(elements)
