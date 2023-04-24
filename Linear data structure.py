class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def delete_zero_sum(head):
    if not head:
        return None
    
    
    sum_map = {0: [None]}
    curr = head
    running_sum = 0
    while curr:
        running_sum += curr.data
        if running_sum in sum_map:
            sum_map[running_sum].append(curr)
        else:
            sum_map[running_sum] = [curr]
        curr = curr.next
    
    
    for node_list in sum_map.values():
        if len(node_list) > 1:
            for node in node_list:
                node.next = None
        else:
            node_list[0].next = None
    
   
    dummy = Node()
    dummy.next = head
    prev, curr = dummy, head
    while curr:
        if not curr.next:
            if curr.next in sum_map[0]:
                prev.next = None
        elif curr in sum_map[0]:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    
    return dummy.next

 #2)Reverse a linked list in groups of given size

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_linked_list(head, k):
    if not head or k == 1:
        return head
    

    def reverse_group(start, end):
        prev, curr = None, start
        while prev != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return end, start
    
    dummy = Node()
    dummy.next = head
    prev, curr = dummy, head
    count = 0
    while curr:
        count += 1
        if count % k == 0:
            prev, curr = reverse_group(prev.next, curr.next)
        else:
            curr = curr.next
    
    return dummy.next
#3)Merge a linked list into another linked list at alternate positions.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def merge_alternate(head1, head2):
    if not head1 or not head2:
        return head1 or head2
    
    curr1, curr2 = head1, head2
    while curr1 and curr2:
        next1, next2 = curr1.next, curr2.next
        curr1.next = curr2
        curr2.next = next1
        curr1, curr2 = next1, next2
    
    if curr2:
        curr1.next = curr2
    
    return head1
#4)In an array, Count Pairs with given sum
def count_pairs_with_sum(arr, sum):
    count = 0
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == sum:
            count += 1
            left += 1
            right -= 1
        elif curr_sum < sum:
            left += 1
        else:
            right -= 1
    return count
#5)Find duplicates in an array
def find_duplicates(arr):
    hash_table = {}
    duplicates = []
    for elem in arr:
        if elem in hash_table:
            duplicates.append(elem)
        else:
            hash_table[elem] = True
    return duplicates
#6)Find the Kth largest and Kth smallest number in an array
def find_kth_largest(arr, k):
    if k < 1 or k > len(arr):
        return None
    pivot = arr[0]
    left = [x for x in arr[1:] if x >= pivot]
    right = [x for x in arr[1:] if x < pivot]
    if len(left) == k - 1:
        return pivot
    elif len(left) >= k:
        return find_kth_largest(left, k)
    else:
        return find_kth_largest(right, k - len(left) - 1)

def find_kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        return None
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    if len(left) == k - 1:
        return pivot
    elif len(left) >= k:
        return find_kth_smallest(left, k)
    else:
        return find_kth_smallest(right, k - len(left) - 1)
#7)Move all the negative elements to one side of the array
def move_negative_elements(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] < 0:
            left += 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
    return arr
#8)Reverse a string using a stack data structure
def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_string = ''
    while len(stack) > 0:
        reversed_string += stack.pop()
    return reversed_string
#9)Evaluate a postfix expression using stack
def evaluate_postfix_expression(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(operand1, operand2, char)
            stack.append(result)
    return stack.pop()

def perform_operation(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 // operand2  

expression = '23*5+'
result = evaluate_postfix_expression(expression)
print(result)  # Output: 11
#10)Implement a queue using the stack data structure
class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
        
    def enqueue(self, element):
        self.enqueue_stack.append(element)
        
    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if not self.dequeue_stack:
            raise Exception('Queue is empty')
        return self.dequeue_stack.pop()




