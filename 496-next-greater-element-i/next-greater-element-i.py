class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge_map = {}

        for num in nums2:
            while stack and num > stack[-1]:
                nge_map[stack.pop()] = num
            stack.append(num)
        while stack:
            nge_map[stack.pop()] = -1

        return [nge_map[num] for num in nums1]