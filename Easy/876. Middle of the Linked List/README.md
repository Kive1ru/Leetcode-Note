### 解法 
快慢指针

### 思路
题目要求寻找linked list的中间节点，可以使用快慢指针的方法。快指针每次走两步，慢指针每次走一步，如果快指针走到链表的尽头，慢指针就会走到链表的中间。

### 复杂度
Time Complexity: O(n) 如果没有环，快指针会走到链表的尽头，所以时间复杂度是O(n)。如果有环，快指针会在环里走k步，k是环的长度，所以时间复杂度是O(n+k)。  
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Slow and fast pointers

### Approach
The question requires finding the intermediate node of the linked list. You can use the fast and slow pointer method. The fast pointer takes two steps at a time, and the slow pointer takes one step at a time. If the fast pointer goes to the end of the linked list, the slow pointer will go to the middle of the linked list.

### the complexity
Time Complexity: O(n) If there is no cycle, the fast pointer will go to the end of the linked list, so the time complexity is O(n). If there is a ring, the fast pointer will take k steps in the ring, where k is the length of the ring, so the time complexity is O(n+k).  
Space Complexity: O(1) It’s all constant space, so it’s O(1)