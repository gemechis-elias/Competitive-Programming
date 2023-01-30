class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res = 0
        left, right = 0, 0
        while left < len(players) and right < len(trainers):
            if players[left] <= trainers[right]:
                res += 1
                left += 1
            right += 1
        return res
