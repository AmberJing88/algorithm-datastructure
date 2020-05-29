# add linked list problem solutions and soving methods
## frequently used 
1. find the circle in a linked list: method is use fast and slow pointers to find the common part
2. find the intersection of two lists: metod iterate a + b and b + a simultaniously, stop at the comon node or null
3. reverse the linked list: metod set a new node between head and head.next;  
a. reverse: temp = head.next, head.next = new_node, new_node = head, 
b. pointer to next node: head = next
