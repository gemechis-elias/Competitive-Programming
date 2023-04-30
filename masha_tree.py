testcase = int(input())
for _ in range(testcase):
    size = int(input())
    array = list(map(int, input().split()))
    answer = [0]
    
    def mergeSort(left, right, array):
        if left == right:
            return [array[left]]
        mid = (left + right) // 2
        left_side = mergeSort(left, mid, array)
        right_side = mergeSort(mid + 1, right, array)
        
        return merge(left_side, right_side)
        
    def merge(left_side, right_side):
        if left_side[0] >= right_side[-1] and left_side[0] >= right_side[0]:
            if answer[-1] != -1:
                answer[-1] += 1
            return right_side + left_side
            
        if right_side[0] >= left_side[-1] and right_side[0] >= left_side[0]:
            return left_side + right_side
            
        answer[-1] = -1
        return left_side + right_side
        
    mergeSort(0, (size - 1), array)
    print(answer[-1])
