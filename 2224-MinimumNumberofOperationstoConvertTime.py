from typing import List


class Solution:
    def addTime(self, time: str, added: int) -> str:
        pass
    
    def isTimeSmaller(self, time: str, time_to_compare_to: str) -> bool:
        pass

    def convertTime(self, current: str, correct: str) -> int:
        addition_possibilities_sorted: List[int] = [60, 15, 5, 1]
        minimum_number_of_operations: int = 0
        while current < correct:
            for addition_possibility in addition_possibilities_sorted:
                time_after_operation: str = self.addTime(current, addition_possibility)
                if self.isTimeSmaller(time_after_operation, correct):
                    current = time_after_operation
                    break
            minimum_number_of_operations += 1
        return minimum_number_of_operations 