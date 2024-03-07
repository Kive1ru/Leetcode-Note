### 解法 
设计+double linked list+hashmap

### 思路
这题是设计题，需要设计一个数据结构，要求get和put的时间复杂度都是O(1)。可以使用双向链表+hashmap来实现。双向链表用来存储数据，hashmap用来存储key和对应的节点。当put时，如果key存在，那么更新value，然后将节点移到链表头部。如果key不存在，那么新建一个节点，然后将节点加入到链表头部，然后将key和节点加入到hashmap。当get时，如果key存在，那么返回value，并将节点移到链表头部。如果key不存在，那么返回-1。当链表满了，那么删除链表尾部的节点，然后将key从hashmap中删除。
### 复杂度
Time Complexity: O(1) get和put的时间复杂度都是O(1)  
Space Complexity: O(n) n是链表的长度，所以是O(n) hashmap的空间复杂度是O(n)


### Solution
Design+double linked list+hashmap

### Approach
This question is a design question. You need to design a data structure, and the time complexity of get and put is required to be O(1). This can be achieved using a doubly linked list + hashmap. Doubly linked lists are used to store data, and hashmaps are used to store keys and corresponding nodes. When put, if the key exists, then the value is updated, and then the node is moved to the head of the linked list. If the key does not exist, create a new node, add the node to the head of the linked list, and then add the key and node to the hashmap. When getting, if the key exists, then the value is returned and the node is moved to the head of the linked list. If the key does not exist, then -1 is returned. When the linked list is full, delete the node at the end of the linked list, and then delete the key from the hashmap.

### Complexity
Time Complexity: O(1) The time complexity of get and put is both O(1)  
Space Complexity: O(n) n is the length of the linked list, so it is O(n) The space complexity of hashmap is O(n)