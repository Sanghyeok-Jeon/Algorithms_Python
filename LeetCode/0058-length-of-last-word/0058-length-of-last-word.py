class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = list(s.split(' '))

        answer = 0
        for i in range(len(word_list)-1, -1, -1):
            if word_list[i] != '':
                answer = len(word_list[i])
                break

        return answer