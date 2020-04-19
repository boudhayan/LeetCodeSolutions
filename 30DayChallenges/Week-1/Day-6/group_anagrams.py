class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            s_key = "".join(sorted(word))
            if not s_key in dict:
                dict[s_key] = [word]
            else:
                dict[s_key].append(word)
        return list(dict.values())