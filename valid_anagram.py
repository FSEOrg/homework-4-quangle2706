from collections import defaultdict


class Solution:
    """
    Ý tưởng dựa theo bài livecoding group anagram:
    thì mình sẽ dùng kỹ thuật check 2 chuỗi có là anagram không
    bằng cách check số lượng từng kí tự chữ dùng list rồi chuyển sang tuple để so sánh

    mình có thể return self.get_key(s) == self.get_key(t)

    nhưng nếu dùng dict thì sẽ check nếu chỉ có duy nhất 1 list trong values thì là
    2 str đó cùng 1 nhóm
    """
    def isAnagram(self, s: str, t: str) -> bool:
        ans = defaultdict(list)
        ans[self.get_key(s)].append(s)
        ans[self.get_key(t)].append(t)

        return len(ans) == 1

    def get_key(self, s):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        return tuple(count)