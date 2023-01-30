class Solution(object):
    def compress(self, chars):
        length = len(chars)
        if length < 2:
            return length
        anchor = 0
        write = 0
        for pos, char in enumerate(chars):
            if (pos + 1) == length or char != chars[pos+1]:
                chars[write] = char
                write += 1
                if pos > anchor:
                    repeated_times = pos - anchor + 1
                    for num in str(repeated_times):
                        chars[write] = num
                        write += 1
                anchor = pos + 1

        return write
