# Definition for a binary tree node.
class Node(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = Node()
        self.height = 0
        self.result = []

    def build_bst_from_sorted_values_middle(self, sorted_values):
        if len(sorted_values) == 0:
            return None
        if len(sorted_values) == 1:
            mid = 0
            root = Node(sorted_values[mid])
        else:
            mid = len(sorted_values)/2
            root = Node(sorted_values[mid])
            root.left = self.build_bst_from_sorted_values_middle(sorted_values[:mid])
            root.right = self.build_bst_from_sorted_values_middle(sorted_values[mid+1:])
        return root
    def travel_xianxu(self, root):
        if root == None:
           return
        self.result.append(root.val)
        self.travel_xianxu(root.left)
        self.travel_xianxu(root.right)
        return self.result
    def travel_houxu(self,root):
        if root == None:
           return
        self.travel_houxu(root.left)
        self.travel_houxu(root.right)
        self.result.append(root.val)
        return self.result
    def travel_zhongxu(self,root):
        if root == None:
           return
        self.__travel_zhongxu(root.left)
        self.result.append(root.val)
        self.__travel_zhongxu(root.right)
        return self.result

    def contains(self,root,num):
        if root == None:
           return False
        if num == None:
           return
        if root.val == num:
           return True
        elif root.val > num:
           return self.contains(root.left,num)
        elif root.val < num:
           return self.contains(root.right,num)
        else:
           return False
    def getheight(self,root):
        if root == None:
           return 0
        return max(self.getheight(root.left), self.getheight(root.right)) + 1

def main():
    values = range(65)
    tree_mid = Tree()
    treeroot = tree_mid.build_bst_from_sorted_values_middle(values)
    print tree_mid.travel_xianxu(treeroot)
#    print tree_mid.travel_houxu(treeroot)
#    print tree_mid.travel_zhongxu(treeroot)

    def travel():
        print "xianxu"
        print tree_mid.travel_xianxu(treeroot)
        print "houxu"
        print tree_mid.travel_houxu(treeroot)
        print "zhongxu"
        print tree_mid.travel_zhongxu(treeroot)

    def ifcontains():
        for value in values:
            print "Is " +str(value)+" in the Tree? " + str(tree_mid.contains(treeroot,value))
        for value in values:
            value = value-5
            print "Is " +str(value)+" in the Tree? " + str(tree_mid.contains(treeroot,value))
        for value in values:
            value = value+5
            print "Is " +str(value)+" in the Tree? " + str(tree_mid.contains(treeroot,value))

    def checkproperitity():   
        print "The height of the Tree is " + str(tree_mid.getheight(treeroot))

    #travel()
    #ifcontains()
    checkproperitity()


if __name__ == '__main__':
	main()