# Definition for a binary tree node.
from __future__ import print_function


class Node(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
        self.visited = False
        self.adjacenciesList = []




class Tree(object):
    def __init__(self):
        self.root = Node()
        self.result = []
        self.total = 0

    def writeadjcentlist(self,root):
        if root == None:
            return
        if root.left is not None:
            root.adjacenciesList.append(root.left)
        if root.right is not None:
            root.adjacenciesList.append(root.right)
        self.writeadjcentlist(root.left)
        self.writeadjcentlist(root.right)

    def build_bst_from_sorted_values_middle(self, sorted_values):
        if len(sorted_values) == 0:
            return None
        if len(sorted_values) == 1:
            mid = 0
            root = Node(sorted_values[mid])
        else:
            mid = len(sorted_values) / 2
            root = Node(sorted_values[mid])
            root.left = self.build_bst_from_sorted_values_middle(sorted_values[:mid])
            root.right = self.build_bst_from_sorted_values_middle(sorted_values[mid + 1:])
        return root

    def __travel_xianxu(self, root):
        if root == None:
            return
        self.result.append(root.val)
        self.__travel_xianxu(root.left)
        self.__travel_xianxu(root.right)
        return self.result

    def __travel_houxu(self, root):
        if root == None:
            return
        self.__travel_houxu(root.left)
        self.__travel_houxu(root.right)
        self.result.append(root.val)
        return self.result

    def __travel_zhongxu(self, root):

        if root == None:
            return
        self.__travel_zhongxu(root.left)
        self.result.append(root.val)
        self.__travel_zhongxu(root.right)
        return self.result

    def travelling(self, root, way):
        self.result = []
        if way is None:
            return self.__travel_xianxu(root)
        if way == 1:
            return self.__travel_xianxu(root)
        if way == 2:
            return self.__travel_zhongxu(root)
        if way == 3:
            return self.__travel_houxu(root)

    def contains(self, root, num):
        if root == None:
            return False
        if num == None:
            return
        if root.val == num:
            return True
        elif root.val > num:
            return self.contains(root.left, num)
        elif root.val < num:
            return self.contains(root.right, num)
        else:
            return False


    def dfs(self, root):

        root.visited = True
        print("%s ->" % str(root.val))
        for n in root.adjacenciesList:
            if not n.visited:
                self.dfs(n)

#Implementation of leetcode 257 binary tree paths
#Given a binary tree, return all root-to-leaf paths
    def __dfspath(self, root, path, res):
        if not root.left and not root.right:
            res.append(path+str(root.val))
        if root.left is not None:
            self.__dfspath(root.left, path+str(root.val)+'-->', res)
        if root.right is not None:
            self.__dfspath(root.right, path+str(root.val)+'-->', res)
    def dfspath(self, root):
        if root is None:
            return []
        self.__dfspath(root, '', self.result)
        return self.result

    def __dfssum(self, root, pathsum, treesum):
        if not root.left and not root.right:
            treesum += pathsum + root.val
        if root.left is not None:
            self.__dfssum(root.left, pathsum+root.val, treesum)
        if root.right is not None:
            self.__dfssum(root.right, pathsum+root.val, treesum)
    def dfssum(self, root):
        if root is None:
            return 0
        self.__dfssum(root, 0, self.total)
        return self.total

    def getheight(self, root):
        if root == None:
            return 0
        return max(self.getheight(root.left), self.getheight(root.right)) + 1

    def insert(self, root, num):
        """
        :rtype: object
        """
        if num == None:
            return
        if root == None:
            return Node(num)
        if num == root.val:
            if root.left is None:
                root.left = Node(num)
            else:
                self.insert(root.left, num)
        elif num > root.val:
            if root.right is None:
                root.right = Node(num)
            else:
                self.insert(root.right, num)
        else:
            return
        return root


def main():
    values = range(10)
    tree_mid = Tree()
    treeroot = tree_mid.build_bst_from_sorted_values_middle(values)
    # 1: xianxu; 2: zhongxu; 3: houxu
    treelist = tree_mid.travelling(treeroot, 2)
    print(treelist)
    treeroot = tree_mid.insert(treeroot, 20)
    print(tree_mid.travelling(treeroot, 2))
    tree_mid.writeadjcentlist(treeroot)
    tree_mid.dfs(treeroot)
    pathlist=tree_mid.dfspath(treeroot)
    for path in pathlist:
        print(path)
    pathsum=tree_mid.dfssum(treeroot)
    print(pathsum)

    def ifcontains():
        for value in values:
            print("Is " + str(value) + " in the Tree? " + str(tree_mid.contains(treeroot, value)))
        for value in values:
            value = value - 5
            print("Is " + str(value) + " in the Tree? " + str(tree_mid.contains(treeroot, value)))
        for value in values:
            value = value + 5
            print("Is " + str(value) + " in the Tree? " + str(tree_mid.contains(treeroot, value)))

    def checkproperitity():
        print("The height of the Tree is " + str(tree_mid.getheight(treeroot)))

    # ifcontains()
    checkproperitity()


if __name__ == '__main__':
    main()
