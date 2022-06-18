from collections import defaultdict
from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        """
        Ý tưởng:
        1. Dùng dict để group các index có cùng value với value là key, group index là list
        2. Duyệt từng group index là list các index
        3. Trong mỗi list sẽ tính dựa theo công thức sau để thoả bài toán
        Công thức: idx * (số lượng index bên trai idx đang xét) - prefixSum
        + postSum - idx * (số lượng index bên phải idx đang xét)

        """

        hash_map = defaultdict(list)
        for idx, val in enumerate(arr):
            hash_map[val].append(idx)

        ans = [0] * len(arr)
        for key in list(hash_map):
            size = len(hash_map[key])

            sum_indices = 0
            for val in hash_map[key]:
                sum_indices += val

            prefixSum = 0
            for i in range(size):
                index = hash_map[key][i]
                ans[index] = index * i - prefixSum + (sum_indices - prefixSum - index) - (size - i - 1) * index
                prefixSum += index

        return ans