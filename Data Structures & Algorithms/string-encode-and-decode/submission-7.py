class Solution:

    def encode(self, strs: List[str]) -> str:
        words_len_list = [str(len(word)) for word in strs]
        ans =  ''.join(strs) + '%$%$%$%$%%$%$%$%$%$%' + ','.join(words_len_list)
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        words, lens = s.split('%$%$%$%$%%$%$%$%$%$%')
        if not lens:
            return []
        for l in lens.split(','):
            ans.append(words[:int(l)])
            words = words[int(l):]
        return ans
        