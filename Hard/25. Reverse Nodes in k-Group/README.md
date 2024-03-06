### 解法 
列表循环遍历

### 思路
题目要求列表每k个nodes为一组反转，这个题目可以用循环遍历的方法。找到列表长度，创建dummy node指向head，每k个nodes为一组，让p0.next指向本组的第一个节点（参考92题）。然后开始反转本组的节点，nxt保存下一组的第一个节点的上一个节点p0.next，重复反转操作，最后返回dummy.next。
### 复杂度
Time Complexity: O(n) 遍历一遍列表，所以时间复杂度是O(n)    
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Binary Search

### Approach
The question requires that every k nodes in the list be reversed as a group. This question can use the loop traversal method. Find the length of the list, create a dummy node pointing to the head, each k nodes are a group, and let p0.next point to the first node of this group (refer to question 92). Then start to reverse the nodes of this group, nxt saves the previous node p0.next of the first node of the next group, repeats the reversal operation, and finally returns dummy.next.

### the complexity
Time Complexity: O(n) Traverse the list once, so the time complexity is O(n)  
Space Complexity: O(1) It’s all constant space, so it’s O(1)