### 解法 
列表循环遍历

### 思路
题目要求反转列表，可以用循环遍历的方法。用三个指针分别指向当前节点，前一个节点和后一个节点。每次循环都把当前节点的next指向前一个节点，然后把三个指针都往后移动一位。最后返回前一个节点。

### 复杂度
Time Complexity: O(n) 遍历一遍列表，所以时间复杂度是O(n)    
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Binary Search

### Approach
The question requires reversing the list, and you can use loop traversal. Use three pointers to point to the current node, the previous node and the next node respectively. Each loop points the next node of the current node to the previous node, and then moves all three pointers back one bit. Finally return to the previous node.

### the complexity
Time Complexity: O(n) Traverse the list once, so the time complexity is O(n)  
Space Complexity: O(1) It’s all constant space, so it’s O(1)