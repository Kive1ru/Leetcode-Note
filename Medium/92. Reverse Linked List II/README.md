### 解法 
列表循环遍历

### 思路
题目要求反转列表中间的一部分left到right的节点，这个题目可以用循环遍历的方法。创建dummy node指向head，然后找到left的前一个节点，然后开始反转left到right的节点（参考206反转列表），最后返回dummy.next。

### 复杂度
Time Complexity: O(n) 遍历一遍列表，所以时间复杂度是O(n)    
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Binary Search

### Approach
The question requires reversing a part of the left to right nodes in the middle of the list. This question can use the loop traversal method. Create a dummy node pointing to head, then find the previous node of left, then start to reverse the nodes from left to right (refer to 206 reversal list), and finally return to dummy.next.

### the complexity
Time Complexity: O(n) Traverse the list once, so the time complexity is O(n)  
Space Complexity: O(1) It’s all constant space, so it’s O(1)