class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_list = []
        for word in strs:
            list_word = sorted(list(word))
            if not res_list:
                res_list.append(
                    {'templ':list_word.copy(),
                    'word_bag':(word,)
                })
            else:
                for group in res_list:
                    if group['templ'] == list_word:
                        group['word_bag'] = group['word_bag'] + (word, )
                        break
                else:
                    res_list.append(
                        {'templ':list_word.copy(),
                        'word_bag':(word,)
                        })
        return [list(x['word_bag']) for x in res_list]