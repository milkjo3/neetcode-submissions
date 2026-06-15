class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # TC: O(nlogk) - For each element (n), we perform atmost one heappush,
            # and one heappop. Which both cost O(logk) operations.
        # SC: O(k) - We use extra space to store atmost k elements (max heap)

        # Maintain a max heap of atmost k elements. 
        max_heap = []

        # For each point:
        for pt in points:

            # Calculate the distance (negate it since we are using max heap, 
            # greater distances are smaller).
            dist = -(pt[0]**2 + pt[1]**2)

            # Push onto the max heap.
            heapq.heappush(max_heap, (dist, pt))

            # Pop the top-most element (greatest distance).
            # Ensuring we only maintain atmost k elements.
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        sol = []

        # Pop all elements from the heap. They are the k-closest points to the origin.
        while max_heap:
            _, pt = heapq.heappop(max_heap)
            sol.append(pt)
        
        return sol