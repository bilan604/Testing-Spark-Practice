from typing import *
from data_structures import TreeNode


class Solution:
    # 69.87% & 99.43% |  bfs of a matrix
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = []
        rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh.append((i,j))
                if grid[i][j] == 2:
                    rotten.append((i,j))
        if not fresh:
            return 0
        time = 0
        while fresh:
            pops = {}
            for i in range(len(rotten)):
                for j in range(len(fresh)):
                    if (abs(rotten[i][0]-fresh[j][0]) + abs(rotten[i][1]-fresh[j][1])) <= 1.1:
                        pops[j] = 0
            if not pops and fresh:
                return -1
            rotten += [fresh[i] for i in range(len(fresh)) if i in pops]
            fresh = [fresh[i] for i in range(len(fresh)) if i not in pops]
            time += 1            
        return time


    # 100.00% & 80.31% | Removing Minimum and Maximum From Array
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        idx_max = nums.index(max(nums))
        idx_min = nums.index(min(nums))
        if idx_min > idx_max:
            idx_min, idx_max = idx_max, idx_min
        
        cut_lr = (1 + idx_min) + (len(nums) - idx_max)
        cut_both = min(idx_max + 1, len(nums) - idx_min)
        
        return min(cut_lr, cut_both)

    # 94.90% & 26.65% | Evaluate Reverse Polish Notation
    def evalRPN(self, tokens: List[str]) -> int:
        dd = {"+": lambda a,b: a+b, "-": lambda a,b: a-b, "*": lambda a,b: a*b, "/": lambda a,b: a//b}
        nums = []
        for i in range(len(tokens)):
            if tokens[i] in dd:
                b = nums.pop()
                a = nums.pop()
                if (tokens[i] == "*" or tokens[i] == "/") and a*b < 0:
                    nums.append(-dd[tokens[i]](abs(a),abs(b)))
                else:
                    nums.append(dd[tokens[i]](a,b))
            else:
                nums.append(int(tokens[i]))
        return nums[0]

    # minimum depth of binary tree
    def recuBST(self, root):
        if not root:
            return float('inf')
        if not root.left and not root.right:  
            return 1
        return min(1 + self.recuBST(root.left), 1 + self.recuBST(root.right))


    def minDepthOfBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.recuBST(root)

    # !!
    def reverseLinkedList(self, node, new_head):
        if not node:
            return new_head
        temp = node.next
        node.next = new_head
        self.recu(temp, node)







