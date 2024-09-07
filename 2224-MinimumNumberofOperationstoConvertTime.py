from typing import List

class Time:
    @classmethod
    def from_string(cls, time: str):
        time_parts: List[str] = time.split(':')
        return Time(int(time_parts[0]), int(time_parts[1]))

    def __init__(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes

    def __le__(self, other: 'Time') -> bool:
        if self.hours < other.hours:
            return True
        
        if self.hours == other.hours and self.minutes <= other.minutes:
            return True
        
        return False
    
    def __lt__(self, other: 'Time') -> bool:
        if self.hours < other.hours:
            return True
        
        if self.hours == other.hours and self.minutes < other.minutes:
            return True
        
        return False
    
    def __add__(self, other_in_minutes: int) -> tuple['Time', bool]:
        if other_in_minutes > 60:
            raise Exception
        
        time: Time = Time(self.hours, self.minutes)
        time.minutes += other_in_minutes
        if time.minutes >= 60:
            time.minutes -= 60
            time.hours += 1
        
        if time.hours >= 24:
            return time, False

        return time, True


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_time: Time = Time.from_string(current)
        correct_time: Time = Time.from_string(correct)
        addition_possibilities_sorted: List[int] = [60, 15, 5, 1]
        minimum_number_of_operations: int = 0

        while current_time < correct_time:
            for addition_possibility in addition_possibilities_sorted:
                time_after_operation, is_ok = current_time + addition_possibility
                if time_after_operation <= correct_time and is_ok:
                    current_time = time_after_operation
                    break

            minimum_number_of_operations += 1
        return minimum_number_of_operations 
    
#print(Solution().convertTime("02:30", "04:35"))
#print(Solution().convertTime("23:55", "23:59"))
print(Solution().convertTime("12:24", "12:50"))