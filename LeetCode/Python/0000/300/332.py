"""
Title : Reconstruct ltinerary
Link : https://leetcode.com/problems/reconstruct-itinerary/
"""

from typing import List


class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.tickets = []
        self.check = []
        self.cities = {}
        self.cities_count = 0

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.tickets = tickets
        self.check = [False] * len(tickets)
        cities = {x: [] for (x, _) in tickets}
        for i, (st, end) in enumerate(tickets):
            cities[st].append((i, end))
        for k, v in cities.items():
            cities[k] = sorted(v, key=lambda x: x[1])
        cities_count = len(tickets)
        self.cities = cities
        self.cities_count = cities_count
        self.search(0, "JFK", ["JFK"])
        return self.ans

    def search(self, count, city_now, trip):
        if count == self.cities_count:
            if not self.ans or trip < self.ans:
                self.ans = trip[::]
            return True
        if self.ans:
            return True
        if city_now not in self.cities:
            return False
        for i, next_city in self.cities[city_now]:
            if self.check[i]:
                continue
            trip.append(next_city)
            self.check[i] = True
            if self.search(count + 1, next_city, trip):
                return True
            trip.pop()
            self.check[i] = False
        return False


if __name__ == "__main__":
    tickets = [
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "JFK"],
        ["ATL", "SFO"],
    ]

    solution = Solution()
    print(solution.findItinerary(tickets))
