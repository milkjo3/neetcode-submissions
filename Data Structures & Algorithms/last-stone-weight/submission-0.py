class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Build array of negative numbers, used to convert min heap
            # into max heap
        stones = [-s for s in stones]

        # create a minheap (maxheap) with the stone values
        heapq.heapify(stones)
       
        # until we smash all stones (1 left or 0 if x - y = 0)
        while len(stones) > 1:
            # pop the first greatest stone
            x = heapq.heappop(stones)

            # pop the first greatest stone
            y = heapq.heappop(stones)

            # if the second stone is greater store result (new stone)
            if y > x:
                heapq.heappush(stones, x - y)

        # add a 0 stone incase the 1 and 2 stones cancel out
        stones.append(0)

        # return the last stone
        return abs(stones[0])