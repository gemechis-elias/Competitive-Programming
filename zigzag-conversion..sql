class Solution:
    def convert(self, s: str, numRows: int) -> str:
### Calculate how many time the sigzag repeats(steps).
    def calculate_steps(length, numRows):
            if (numRows * 2 - 2) > 0:
                steps = length // (numRows * 2 - 2)
                mod = length % (numRows * 2 - 2)
            else: 
                steps = 0
                mod = length
            if mod > 0:
                steps += 1
            return steps

        if len(s) <= numRows or numRows == 1:
            return(s)

        steps = calculate_steps(len(s), numRows)
        res = ""

        pack = 2 * numRows - 2 #How many characters in a single sigzag

### Generate result string from the characters in the first row.
        for step in range(steps):
            if pack * step < len(s):
                res += s[pack * step]
        
### Generate result string from the characters from the 2nd to second last rows.
        for row in range(1, numRows-1):
            for step in range(steps):
                position1 = pack * step + row
                if position1 < len(s):
                    res += s[position1]
                position2 = pack - row + pack * step
                if position2 <len(s):
                    res += s[position2]
###  Genertate result string from the characters in the last row.
        for step in range(steps):
            position = pack * step + numRows - 1
            if position < len(s):
                res += s[position]
        return res