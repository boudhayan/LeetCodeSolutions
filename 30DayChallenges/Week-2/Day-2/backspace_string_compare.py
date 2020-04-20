class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.performBackspace(S) == self.performBackspace(T)

    def performBackspace(self, str):
        r_value = list(str[::-1])
        d_count = 0
        for i in range(len(r_value)):
            if r_value[i] == "#":
                d_count += 1
                r_value[i] = "*"
            else:
                if d_count > 0:
                    r_value[i] = "*"
                    d_count -= 1
        return "".join(reversed(r_value)).replace("*","")
        