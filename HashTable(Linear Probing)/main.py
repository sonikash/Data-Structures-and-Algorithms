    class Hashtable:
    def __init__(self):
        self.max =100
        self.arr= [[] for i in range(self.max)]

    def get_hash(self,key):
        hashh = 0
        for char in key:
            hashh = hashh + ord(char)
        return hashh % self.max



    def __setitem__(self, key, value):
        index = self.get_hash(key)
        original_index = index
        while len(self.arr[index])!=0 and self.arr[index][0]!=key:
            index = (index+1)% self.max # to check on index, if its last index it will again set to start of array

            if index ==original_index:
                raise Exception("Hashtable is full")

        self.arr[index]= (key,value)

    def __getitem__(self, key):
        index=self.get_hash(key)
        original_index= index
        while len(self.arr[index])!=0:
            if self.arr[index][0]==key:
                return self.arr[index][1]
            index = (index+1)%self.max
            if index==original_index: # to check if the loop has completed the cycle
                break
        return None

    def __delitem__(self, key):
        index = self.get_hash(key)
        original_index=index

        while len(self.arr[index])!=0:
            if self.arr[index][0]==key:
                del self.arr[index]

                next_index=(index+1)%self.max
                while len(self.arr[next_index])!=0:
                    rehash_key,rehash_val= self.arr[next_index]
                    del self.arr[next_index]
                    self.__setitem__(rehash_key,rehash_val)
                    next_index = (next_index+1)%self.max
                return
            index = (index+1)%self.max
            if index==original_index:
                break
        return ("Key not found")




if __name__ == '__main__':
    t=Hashtable()
    t['march 21']=121
    t['march 02']=111
    t['march 30']=123
    del(t['march 02'])
    print(t['march 19'])
    print(t.arr)

