### 解法 
双指针

### 思路
可以变为有序数组，参考 Medium 167 2sum sorted，可以使用双指针的方法。此题要求三数之和为0，且不重复。nums[i] + nums[j] + nums[k] = 0 可以变为 nums[j] + nums[k] = -nums[i]。所以可以固定一个数，然后使用双指针的方法找到另外两个数。这里需要注意的是，找到一个解后，需要跳过重复的解。所以需要在找到解后，跳过重复的解。一个指针指向i+1，一个指针指向数组的尾，然后向中间移动，直到找到答案。如果两个指针指向的元素的和大于目标值，那么尾指针向前移动，如果两个指针指向的元素的和小于目标值，那么头指针向后移动。（因为两端之和如果小于目标，说明numbers[left]太小了。两端之和如果大于目标，说明numbers[right]太大了。）优化步骤在于，如果nums[i] + nums[i+1] + nums[i+2] > 0，说明后面的数都大于0，不可能有解了，直接break。如果nums[i] + nums[n-2] + nums[n-1] < 0，说明前面的数都小于0，不可能有解了，继续遍历i+1。

### 复杂度
Time Complexity: O(n^2) sort本身是O(nlogn)，一个for loop，一个while loop，两个指针向中间移动，所以是O(n^2)。 O(n^2) > O(nlogn) 所以是O(n^2)
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Two pointer

### Approach
It can be turned into an ordered array, refer to Medium 167 2sum sorted, and you can use the double pointer method. This question requires that the sum of the three numbers is 0 and must not be repeated. nums[i] + nums[j] + nums[k] = 0 can become nums[j] + nums[k] = -nums[i]. So you can fix one number and then use the double pointer method to find the other two numbers. What needs to be noted here is that after finding a solution, duplicate solutions need to be skipped. Therefore, it is necessary to skip repeated solutions after finding the solution. A pointer points to i+1, a pointer points to the end of the array, and then moves toward the middle until the answer is found. If the sum of the elements pointed to by the two pointers is greater than the target value, then the tail pointer moves forward. If the sum of the elements pointed to by the two pointers is less than the target value, then the head pointer moves backward. (Because if the sum of both ends is less than the target, it means that numbers[left] is too small. If the sum of both ends is greater than the target, it means that numbers[right] is too big.) The optimization step is that if nums[i] + nums[i +1] + nums[i+2] > 0, which means that the following numbers are all greater than 0, and there is no solution, so just break. If nums[i] + nums[n-2] + nums[n-1] < 0, it means that the previous numbers are less than 0, there is no solution, and we continue to traverse i+1.

### the complexity
Time Complexity: O(n^2) sort itself is O(nlogn), a for loop, a while loop, and two pointers move to the middle, so it is O(n^2). O(n^2) > O(nlogn) so O(n^2)
Space Complexity: O(1) It’s all constant space, so it’s O(1)