# add linked list problem solutions and soving methods
## frequently used 
1. find the circle in a linked list: method is use fast and slow pointers to find the common part
2. find the intersection of two lists: metod iterate a + b and b + a simultaniously, stop at the comon node or null
3. reverse the linked list: metod set a new node between head and head.next;  
a. reverse: temp = head.next, head.next = new_node, new_node = head, 
b. pointer to next node: head = next
4. remove duplicates: if sorted, use compare and remove next, if not sorted, find the circle and remove one with slow and fast pointers
# leetcode problems review
1. 160, 206, 92,21,88,83
2. 19, 24, 25, 445, 234, 725, 328
