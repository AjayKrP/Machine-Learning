class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def InsertAtTail(data, head):
    if(head == None):
        return Node(data)
    else:
        if(head.next == None):
            head.next = Node(data)
        else:
            return InsertAtTail(data, head.next)

def InsertAtHead(data, head):
    temp = Node(data)
    temp.next = head
    return head

def SearchData(data, head):
    while(head):
        if(head.data == data):
            return True
    return False

# def InsertAtMiddle(data1, data2, head):
#     tail, temp = head
#     while(temp.next):
#         if(temp.data == data1):



def Print(head):
    while(head):
        print(head.data)
        head = head.next

if __name__== "__main__":
    node = Node()
    InsertAtTail(4, node)
    InsertAtTail(6, node)
    InsertAtTail(4, node)
    InsertAtTail(6, node)
    InsertAtHead(9, node)
    Print(node)