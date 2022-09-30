def countSwaps(a):
    swap=0
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swap+=1
    print("Array is sorted in {} swaps.".format(swap))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
