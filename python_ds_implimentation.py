from collections import deque
import heapq

# 1. Array
arr = [1, 2, 3, 4, 5]

# 2. Binary Search
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 3. Sliding Window (Maximum Sum Subarray of Size k)
def max_sum_subarray(nums, k):
    max_sum, window_sum = float('-inf'), 0
    left = 0
    for right in range(len(nums)):
        window_sum += nums[right]
        if right >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[left]
            left += 1
    return max_sum

# 4. Matrix Traversal
def traverse_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=' ')
        print()

# 5. Two Pointer Technique
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []

# 6. Intervals (Merge Intervals)
def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# 7. Hash Map
hash_map = {}
hash_map["key"] = "value"

# 8. String Manipulation
def reverse_string(s):
    return s[::-1]

# 9. Recursion (Factorial)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# 10. Dynamic Programming (Fibonacci)
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# 11. Trees (Binary Tree)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

# 12. Graph (Adjacency List)
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    def bfs(self, start):
        visited, queue = set(), deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                print(node, end=' ')
                queue.extend(self.graph.get(node, []))

# 13. Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('None')

# 14. Stack
stack = []
stack.append(1)
stack.append(2)
print(stack.pop())  # 2

# 15. Queue
queue = deque()
queue.append(1)
queue.append(2)
print(queue.popleft())  # 1

# 16. Heap (Priority Queue)
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))  # 1
