class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s
        
        # Step 1: Frequency count
        freq = Counter(s)
        
        # Step 2: Max heap (use negative freq for max behavior)
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        # Step 3: Queue to hold characters waiting for k distance
        wait_queue = deque()  # (available_time, count, char)
        
        result = []
        time = 0
        
        while max_heap or wait_queue:
            time += 1
            
            if max_heap:
                count, char = heapq.heappop(max_heap)
                result.append(char)
                
                # Decrease count (since negative)
                count += 1  
                
                if count < 0:
                    wait_queue.append((time + k - 1, count, char))
            else:
                return ""  # Not possible
            
            # Check if any character is ready to be reused
            if wait_queue and wait_queue[0][0] == time:
                _, count, char = wait_queue.popleft()
                heapq.heappush(max_heap, (count, char))
        
        return "".join(result)
