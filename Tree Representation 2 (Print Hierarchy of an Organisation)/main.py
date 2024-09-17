from sys import prefix


class TreeNode:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.children =[]
        self.parent = None

    def add_child(self,child):
        child.parent =self
        self.children.append(child)

    def get_level(self):
        level = 0
        p=self.parent
        while p:
            level =level +1
            p=p.parent

        return level

    def print_tree(self, property_name):
        if property_name =="both":
            value =self.name + "("+ self.designation+")"

        elif property_name == "name":
            value = self.name

        else:
            value = self.designation

        spaces = ' '*self.get_level()*2
        prefix= spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)

def build_management_tree():
    ceo =TreeNode("Nilpul", "CEO")

    cto= TreeNode("Chinmay","CTO")
    infra_head= TreeNode("Vishwa","Infastructure Head")
    cto.add_child(infra_head)
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit","App Manager"))

    application_head = TreeNode("Aamir","Application Head")
    hr_head = TreeNode("Gels","HR Head")
    hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas","Policy Manager"))

    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo






if __name__ == '__main__':
    root =build_management_tree()
    root.print_tree("both")

