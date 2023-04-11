class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        if color == originalColor:
            return image
        def dfs_fill(image, r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != originalColor:
                return
            image[r][c] = color
            dfs_fill(image, r + 1, c)
            dfs_fill(image, r - 1, c)
            dfs_fill(image, r, c + 1)
            dfs_fill(image, r, c - 1)
            
        dfs_fill(image, sr, sc)
        return image