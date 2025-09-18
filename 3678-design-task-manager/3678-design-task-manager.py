class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_to_user = {}
        self.task_to_pri = {}
        self.heap = []

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)   

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_to_user[taskId] = userId
        self.task_to_pri[taskId] = priority
        heapq.heappush(self.heap, (-priority,-taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.task_to_user[taskId]  
        self.task_to_pri[taskId] = newPriority
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))      

    def rmv(self, taskId: int) -> None:
        self.task_to_user.pop(taskId, None)
        self.task_to_pri.pop(taskId, None)      

    def execTop(self) -> int:
        while self.heap:
            neg_pri, neg_tid, tid = heapq.heappop(self.heap)
            pri = -neg_pri
            cur_pri = self.task_to_pri.get(tid)
            if cur_pri is None:
                continue
            if cur_pri != pri:
                continue
            userId = self.task_to_user.pop(tid)
            self.task_to_pri.pop(tid)
            return userId
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()