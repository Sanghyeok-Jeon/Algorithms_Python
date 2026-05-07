class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        ten_x = 1
        for i in range(len(digits) - 1, -1, -1):
            num += digits[i] * ten_x
            ten_x *= 10

        num += 1

        new_digits = []
        while num >= 10:
            digit = num % 10
            new_digits.append(digit)
            num //= 10

        new_digits.append(num)

        return new_digits[::-1]