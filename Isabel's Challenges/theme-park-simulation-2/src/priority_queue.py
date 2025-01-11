import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, event_time, ride_id):
        heapq.heappush(self.queue, (event_time, ride_id))

    def popleft(self):
        return heapq.heappop(self.queue)

    def __len__(self):
        return len(self.queue)