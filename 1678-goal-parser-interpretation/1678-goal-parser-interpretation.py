class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        i = 0
        while len(command) > i:
            if command[i] == "(":
                if len(command) > i+1 and command[i+1] == ")":
                    res+="o"
                    i+=1
            elif command[i] != ")":
                res+= command[i]
            i+=1
        return res