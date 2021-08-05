# p504
# No. 61


class sol:
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largest(self, nums: list) -> str:
        i = 1
        while i < len(nums):
            j = 1
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1
        return str(int(''.join(map(str, nums))))


sol = sol()
print(sol.largest([10, 2]))
