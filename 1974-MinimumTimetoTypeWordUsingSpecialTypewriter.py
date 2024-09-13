class Solution:
    def minTimeToType(self, word: str) -> int:
        current_letter: chr = 'a'
        current_number_of_steps: int = 0
        for char in word:
            forward_steps: int = abs(ord(char)-ord(current_letter))
            backward_steps: int = 26 - forward_steps
            min_steps_to_letter: int = min(forward_steps, backward_steps)
            steps_to_choose_letter: int = 1
            current_number_of_steps += min_steps_to_letter + steps_to_choose_letter
            current_letter = char
        return current_number_of_steps

print(Solution().minTimeToType("abc")==5)
print(Solution().minTimeToType("bza")==7)
print(Solution().minTimeToType("zjpc")==34)