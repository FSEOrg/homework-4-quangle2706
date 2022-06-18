from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Ý tưởng:
        Dùng hash map để lưu prefix
        Vì có trường hợp 1 phần tử trong arr = k -> khởi tạo hashmap với (0, 1)
        (sum, số lần trùng hợp có cùng sum khi + chuỗi)
        ví dụ
        từ vị trí idx 0 tới 3 có sum = 10 và từ 0 tới 7 cũng có sum = 10
        thì ta sẽ có 2 path để mà xuất phát từ 3 hoặc 7 tới j sao cho 3 -> j = k
        và 7 -> j = k
        prefixSum[j] - prefixSum[3] = k = prefixSum[j] - prefixSum[7]
        """
        prefixSum = 0
        count = 0
        hash_map = defaultdict()
        hash_map[0] = 1
        for num in nums:
            prefixSum += num
            if (hash_map.get((prefixSum - k), -1) != -1):
                count += hash_map.get(prefixSum - k)

            if hash_map.get(prefixSum, -1) != -1:
                hash_map[prefixSum] += 1 # case tồn tại 1 path khác cũng có prefixSum giống nhau
            else:
                hash_map[prefixSum] = 1

        return count

