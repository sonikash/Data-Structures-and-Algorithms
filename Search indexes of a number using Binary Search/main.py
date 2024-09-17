class BinarySearch:
    def __init__(self, items):
        self.items = items

    def search(self, val):
        indexes=[]
        start_pointer=0
        end_pointer=len(self.items)-1
        while start_pointer<=end_pointer:
            mid=(start_pointer+end_pointer)//2
            mid_element=self.items[mid]

            if val==mid_element:
                indexes.append(mid)

                left=mid-1
                while left>=start_pointer and self.items[left] == val:
                    indexes.append(left)
                    left = left - 1


                right=mid+1
                while right <= end_pointer and self.items[right] == val:
                    indexes.append(right)
                    right = right + 1

                break
            elif val<mid_element:
                end_pointer=mid-1
            else:
                start_pointer=mid+1

        if len(indexes)==0:
            return -1
        else:
            return sorted(indexes)


if __name__ == '__main__':
    elements = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    bin = BinarySearch(elements)
    print(bin.search(15))  # Output should be [5, 6, 7]
