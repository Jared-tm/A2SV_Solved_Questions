#peak or Valley
        if (arr[i] > arr[i-1] and arr[i] > arr[i+1])  or  (arr[i] < arr[i-1]  and arr[i] < arr[i+1]) :
            res.append(arr[i])
    
    res.append(arr[-1])
    print(len(res))
    print(*res)