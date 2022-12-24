class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        
        for i in range(0, len(command)):
            if command[i] == "(":
                if len(command) > i+1 and command[i+1] == ")":
                    res +="o"
            elif command[i] != ")":
                res += command[i]
        return res