class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isUnique = {}
        flag = False

        while nums and not flag:
            current_number = nums.pop()

            if current_number in isUnique:
                flag = True
            else:
                isUnique[current_number] = current_number


        return flag

            
        