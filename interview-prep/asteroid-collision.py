class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        def pos_size(num):
            return 1 if num > 0 else -1, abs(num)

        for i in range(len(asteroids)):
            curr_pos, curr_size = pos_size(asteroids[i])
            equal = False

            if not stack or curr_pos == 1:
                stack.append(asteroids[i])
                continue

            while stack and stack[-1] > 0 and stack[-1] < curr_size:
                stack.pop()

            if stack and stack[-1] == curr_size:
                stack.pop()
            else:
                if not stack or stack[-1] < 0:
                    stack.append(asteroids[i])

        return stack