"""
Title : 백신 개발
Link : https://www.acmicpc.net/problem/30090
"""

from itertools import permutations
from sys import stdin


class Vaccine:
    def __init__(self, N: int, viruses: list[str]) -> None:
        self.N = N
        self.viruses = viruses

    def create_vaccine(self) -> str:
        vaccine = "".join(self.viruses)
        for perm in permutations(range(self.N), self.N):
            _vaccine = self.search(perm)
            if _vaccine is None:
                continue
            if len(_vaccine) < len(vaccine):
                vaccine = _vaccine
        return vaccine

    def search(self, perm: tuple[int, ...]) -> None | str:
        _vaccine: None | str = self.viruses[perm[0]]
        for idx in perm[1:]:
            if _vaccine is None:
                return None
            _vaccine = self.check_vaccine(_vaccine, self.viruses[idx])
        return _vaccine

    def check_vaccine(self, existing_vaccine: str, new_vaccine: str) -> None | str:
        for i in range(min(len(new_vaccine), len(existing_vaccine)), 0, -1):
            if existing_vaccine[-i:] == new_vaccine[:i]:
                return existing_vaccine + new_vaccine[i:]
        return None


input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    viruses = list(input().strip() for _ in range(N))

    vaccine = Vaccine(N, viruses)
    print(len(vaccine.create_vaccine()))
