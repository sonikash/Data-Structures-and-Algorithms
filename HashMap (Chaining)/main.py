class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [[] for i in range(self.Max)] #list comprehension in done here

    def get_hash(self,key):#creating a hash code to get index so key,value can be stored at that index
        hashh = 0
        for char in key:
            hashh = hashh + ord(char)
        return hashh % 100

    def __setitem__(self,key,val): #adding key at the index in the array
        index =  self.get_hash(key)
        bucket = self.arr[index]
        found= False #this is a flag condition that will check if key value pair is already present or not
        for idx, element in enumerate (bucket):
            if len(element)==2 and element[0]== key:
                self.arr[index][idx] = (key,val)  # STORING THE KEY VALUE IN A TUPLE,THAT IS STORED IN THE LIST AND THE LIST IS STORED AT INDEX OF ARRAY
                found = True #flag condition sets to True as the pair is present and updated
                break

        if not found:
            self.arr[index].append((key,val))

    def __getitem__(self,key): #getting the value of particular key
        index = self.get_hash(key)
        bucket= self.arr[index]
        for idx,element in enumerate(bucket):
            if element[0]==key:
                return element[1]



    def __delitem__(self, key):
        index = self.get_hash(key)
        bucket = self.arr[index]
        for idx, element in enumerate (bucket):
            if element[0]==key:
                del bucket[idx]
                break







if __name__ == '__main__':
    t = HashTable()
    t['march 21']= 120
    t['march 22']= 112
    t['march 30']=139
    print(t['march 21'])
    del(t['march 21'])
    print(t['march 21'])

