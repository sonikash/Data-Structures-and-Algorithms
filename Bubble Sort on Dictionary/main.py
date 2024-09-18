class BubbleSort:
    def __init__(self,items):
        self.items=items

    def sort(self,key):
        for i in range(len(self.items)-1):
            swapped =False
            for j in range(len(self.items)-1-i):
                a = self.items[j][key]
                b = self.items[j+1][key]
                if a>b:
                    temp = elements[j]
                    self.items[j] = self.items[j+1]
                    self.items[j+1] = temp
                    swapped = True
            if not swapped:
                break




if __name__ == '__main__':
    elements=[{'name':'Andrew','transaction amount': 10000, 'device':'Mobile'},
              {'name':'Stuart','transaction amount': 2500, 'device':'Gaming Console'},
              {'name':'Lisa','transaction amount': 1500, 'device':'PC Screen'},
              {'name':'Mark','transaction amount': 9500, 'device':'Gaming Setup'},
              {'name':'Rachel','transaction amount': 500, 'device':'Apple watch'}]
    bubble= BubbleSort(elements)
    bubble.sort(key='transaction amount')
    print(elements)