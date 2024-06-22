#Factorial using recursive function

# def fact(num):
#     if num == 1:
#         return num
#     else:
#         return num*fact(num-1)
# number = int(input('Enter integer.'))
# print(fact(number))


#Palindrome Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.ptr =  None

def isPalindrom(head):

    temp = head
    stack = []
    isPalin = True

    while temp != None:
        stack.append(temp.data)
        temp = temp.ptr
    while head!= None:
        data = stack.pop()
        if head.data == data:
            isPalin = True
        else:
            isPalin = False
            break
        head =  head.ptr
    return isPalin


one = Node(1)
two = Node(1)
three = Node(2)
four = Node(1)

one.ptr = two
two.ptr = three
three.ptr= four
four.ptr = None
 
result = isPalindrom(one)
print("isPalindrom : ",result)


class Node:
    def __init__(self,data):
        self.data = data
        self.left =  None
        self.right = None

class BST:
    root = None

    def insert(self,key):
        node = Node(key)
        if self.root == None:
            self.root = node
            return
        prev = None
        temp = self.root
        while(temp!=None):
            if temp.data > key:
                prev = temp
                temp = temp.left
            elif temp.data < key:
                prev = temp
                temp = temp.right
        if(prev.val > key):
            prev.left = node
        else:
            prev.right = node

    def delete(self,key):
        if self.data ==  key:
            self.right = self.right.left
            self.left = self.left.right
            self.delete
        else:
            prev =  None
            temp = self.root
            while(temp!=None):
                


tree = BST()
tree.insert(10)
tree.insert(7)
tree.insert(16)
tree.insert(45)


