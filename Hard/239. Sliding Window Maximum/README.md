### 解法 
滑动窗口

### 思路
题目要求寻找滑动窗口为k，窗口内的最大值。所以可以使用滑动窗口的方法。使用deque来存储窗口内的最大值。分成两个状态，窗口未形成和窗口形成。当窗口未形成时，直接将元素加入到deque中。每次都判断当前数值是否大于deque的最后一个元素，如果大于，那么将deque的最后一个元素弹出，直到deque的最后一个元素大于当前数值，然后将deque的第一个元素加入到结果中。当窗口形成时，首先判断deque首个值是否等于当前的数值，如果等于，那么将deque的首个值弹出。然后移动窗口，每次都判断当前数值是否大于deque的最后一个元素，如果大于，那么将deque的最后一个元素弹出。最后将deque的第一个元素加入到结果中。最后返回结果。
### 复杂度
Time Complexity: O(n) 其中n为数组nums长度；线性遍历nums占用O(n)；每个元素最多仅入队和出队一次，因此单调队列deque占用O(2n)  
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Sliding window

### Approach
The question requires finding a sliding window of k and the maximum value within the window. So you can use the sliding window method. Use deque to store the maximum value within the window. Divided into two states, the window is not formed and the window is formed. When the window is not formed, add the elements directly to the deque. Each time, it is judged whether the current value is greater than the last element of deque. If it is greater, the last element of deque is popped out until the last element of deque is greater than the current value, and then the first element of deque is added to the result. When the window is formed, first determine whether the first value of deque is equal to the current value. If it is equal, then pop up the first value of deque. Then move the window, and each time it is judged whether the current value is greater than the last element of deque. If it is greater, then the last element of deque is popped out. Finally, the first element of the deque is added to the result. Finally return the result.

### Complexity
Time Complexity: O(n) where n is the length of the array nums; linear traversal of nums takes O(n); each element is only entered and dequeued once at most, so the monotonic queue deque takes O(2n)  
Space Complexity: O(1) is all constant space, so it's O(1)