class TreeNode:
    def __init__(self, data):
        self.data= data
        self.children =[]
        self.parent = None

    def add_child(self, child):
        child.parent=self
        return self.children.append(child)

    def get_level(self):
        level =0
        p =self.parent
        while p:
            level= level+1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' '*self.get_level()*2
        prefix = spaces + "|__" if self.parent else "" #ternary operator used here
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Lenovo"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Mac"))

    phone = TreeNode("Phone")
    phone.add_child(TreeNode("Samsung"))
    phone.add_child(TreeNode("Apple"))
    phone.add_child(TreeNode("Google"))

    television= TreeNode("Television")
    television.add_child(TreeNode("Philips"))
    television.add_child(TreeNode("LG"))


    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(television)
    return root

if __name__ == '__main__':
    root =build_product_tree()
    root.print_tree()

