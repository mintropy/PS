class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_type = set(jewels)
        return sum([1 for s in stones if s in jewel_type])
