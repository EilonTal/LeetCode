from typing import List

class Time:
    @classmethod
    def from_string(cls, time: str):
        time_parts: List[str] = time.split(':')
        return Time(int(time_parts[0]), int(time_parts[1]))

    def __init__(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes

    def __lt__(self, other: 'Time') -> bool:
        if self.hours < other.hours:
            return True
        
        if self.hours == other.hours and self.minutes < other.minutes:
            return True
        
        return False
    
    def __add__(self, other_in_minutes: int) -> 'Time':
        if other_in_minutes > 60:
            raise Exception
        
        self.minutes += other_in_minutes
        if self.minutes > 60:
            self.minutes -= 60
            self.hours += 1
        
        if self.hours > 24:
            LATEST_TIME = Time(23, 59)
            self = LATEST_TIME

        return self


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_time: Time = Time.from_string(current)
        correct_time: Time = Time.from_string(correct)
        addition_possibilities_sorted: List[int] = [60, 15, 5, 1]
        minimum_number_of_operations: int = 0

        while current_time < correct_time:
            for addition_possibility in addition_possibilities_sorted:
                time_after_operation: Time = current_time + addition_possibility
                if time_after_operation < correct_time:
                    current_time = time_after_operation
                    break

            minimum_number_of_operations += 1
        return minimum_number_of_operations 
    
print(Solution().convertTime("11:00", "11:01"))