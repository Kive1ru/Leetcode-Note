### 解法 
快慢指针

### 思路
题目要求寻找linked list中是否有环,如果有返回入口的值，可以使用快慢指针的方法。快指针每次走两步，慢指针每次走一步，如果有环，快指针一定会追上慢指针。然后找到环的入口，可以使用数学方法证明，head到环的入口的距离等于a，环的入口到相遇点的距离等于b，相遇点到环的入口的距离等于c，那么慢指针走的距离等于a+b，快指针走的距离等于a+b+(b+c)*k，因为快指针走的距离是慢指针的两倍，所以a+b+b+c+(k-1)*(b+c)=2(a+b)，所以a-c=(k-1)*(b+c)。假设此时head与slow指针分别走c步，那么slow此时位于环的入口，而head到环的入口的距离等于a-c。a-c=(k-1)*(b+c)代表head到入口的距离相当于环长的k-1倍，所以如果head与slow继续走，最终head与slow指针会在环的入口相遇。此时返回slow指针的值即可。

### 复杂度
Time Complexity: O(n) 如果没有环，快指针会走到链表的尽头，所以时间复杂度是O(n)。如果有环，慢指针在相遇前后都走了O(n)的距离，所以时间复杂度是O(n)。  
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Slow and fast pointers

### Approach
The question requires finding whether there is a cycle in the linked list. If there is a value that returns the entry, you can use the method of fast and slow pointers. The fast pointer takes two steps at a time, and the slow pointer takes one step at a time. If there is a loop, the fast pointer will definitely catch up with the slow pointer. Then find the entrance of the ring. You can use mathematical methods to prove that the distance from the head to the entrance of the ring is equal to a, the distance from the entrance of the ring to the meeting point is equal to b, and the distance from the meeting point to the entrance of the ring is equal to c. Then the distance traveled by the slow pointer Equal to a+b, the distance traveled by the fast pointer is equal to a+b+(b+c)*k, because the distance traveled by the fast pointer is twice that of the slow pointer, so a+b+b+c+(k-1)*( b+c)=2(a+b), so a-c=(k-1)*(b+c). Assume that the head and slow pointers take c steps respectively at this time, then slow is located at the entrance of the ring, and the distance from head to the entrance of the ring is equal to a-c. a-c=(k-1)*(b+c) means that the distance from head to the entrance is equivalent to k-1 times the ring length, so if head and slow continue walking, eventually the head and slow pointers will meet at the entrance of the ring. At this time, just return the value of the slow pointer.

### the complexity
Time Complexity: O(n) If there is no cycle, the fast pointer will go to the end of the linked list, so the time complexity is O(n). If there is a loop, the slow pointer travels a distance of O(n) before and after the encounter, so the time complexity is O(n).  
Space Complexity: O(1) It’s all constant space, so it’s O(1)