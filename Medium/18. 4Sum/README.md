### 解法 
双指针

### 思路
可以变为有序数组，参考 Medium 15 3sum。一模一样的方法唯一区别就是多了个数，修改方法就是在第一个数的for loop里面嵌入另外一个for loop去遍历第二个数。按照3Sum同样的做法去处理后面两个数字。（双指针）

### 复杂度
Time Complexity: O(n^3) sort本身是O(nlogn)，两个for loop，一个while loop，两个指针向中间移动，所以是O(n^3)。 O(n^3) > O(nlogn) 所以是O(n^3)  
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Two pointer

### Approach
Can be turned into an ordered array, refer to Medium 15 3sum. The method is exactly the same. The only difference is that there are more numbers. The modification method is to embed another for loop in the for loop of the first number to traverse the second number. Follow the same approach as 3Sum to process the next two numbers. (two pointer)

### the complexity
Time Complexity: O(n^3) sort itself is O(nlogn), two for loop, a while loop, and two pointers move to the middle, so it is O(n^3). O(n^3) > O(nlogn) so O(n^3)  
Space Complexity: O(1) It’s all constant space, so it’s O(1)