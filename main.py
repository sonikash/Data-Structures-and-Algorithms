class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,val):
        if self.data ==val: #refrain duplicate elements
            return
        if self.data>val: # if value is less than root node
            if self.left:
                self.left.add_child(val)
            else:
                self.left=BinarySearchTree(val)

        if self.data<val: #if value is greater than root node
            if self.right:
                self.right.add_child(val)
            else:
                self.right=BinarySearchTree(val)

    def inorder_traversal(self):
        elements=[]

        if self.left:
            elements=elements+self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements=elements+self.right.inorder_traversal()

        return elements

    def postorder_traversal(self):
        elements=[] # it again initialises empty list for every recursive call
        if self.left:
           elements =elements+ self.left.postorder_traversal()

        if self.right:
            elements=elements+self.right.postorder_traversal()

        elements.append(self.data)

        return elements

    def preorder_traversal(self):
        elements=[self.data]#adds the number that is calling the method in the list

        if self.left:
            elements=elements+self.left.preorder_traversal() #concatenating the result of every recursive call to the list.

        if self.right:
            elements=elements+self.right.preorder_traversal()

        return elements


    def search(self,val):
        if self.data == val:
            return True

        if self.data>val:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if self.data<val:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def maximum(self):
        if self.right is None:
            return self.data
        return self.right.maximum()

    def minimum(self):
        if self.left is None:
            return self.data
        return self.left.minimum()

    def sum(self):
        left_sum=self.left.sum() if self.left else 0
        right_sum=self.right.sum() if self.right else 0
        return self.data+left_sum+right_sum

    # def delete(self,val):
    #     if val<self.data:
    #         if self.left:
    #             self.left=self.left.delete(val)
    #         else:
    #             return None
    #     elif val>self.data:
    #         if self.right:
    #             self.right=self.right.delete(val)
    #         else:
    #             return None
    #
    #     else:
    #         if self.left is None and self.right is None:
    #             return None
    #         if self.left is None:
    #             return self.right
    #         if self.right is None:
    #             return self.left
    #         min_val= self.right.minimum()
    #         self.data=min_val
    #         self.right = self.right.delete(min_val)
    #
    #     return self

    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left = self.left.delete(val)
            else:
                return None

        elif val>self.data:
            if self.right:
                self.right = self.right.delete(val)
            else:
                return None
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.left is None:
                return self.right

            max_val=self.left.maximum()
            self.data= max_val
            self.left=self.left.delete(max_val)

        return self





def build_tree(elements):
    root=BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root
if __name__ == '__main__':
    elements =[30,99,78,66,2,5,7,97,23]
    number_tree = build_tree(elements)
    print(number_tree.inorder_traversal())
    print(number_tree.postorder_traversal())
    print(number_tree.preorder_traversal())
    print(number_tree.maximum())
    print(number_tree.minimum())
    print(number_tree.sum())
    print(number_tree.search(91))

    elements = ['zee','abc','des','sed','lid']
    alpha_tree = build_tree(elements)
    print(alpha_tree.inorder_traversal())
    print(alpha_tree.postorder_traversal())




