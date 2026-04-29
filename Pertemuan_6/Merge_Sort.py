'''
[38,27,43,3,9,82,10]

→ [38,27,43,3]     [9,82,10]

→ [38,27] [43,3]   [9,82] [10]

→ [38] [27] [43] [3] [9] [82] [10]

→ [27,38] [3,43] [9,82] [10]

→ [3,27,38,43] [9,10,82]

→ [3,9,10,27,38,43,82]
'''

def merge_sort (data):
    if len(data) > 1:
        mid = len(data) //2
        Left = data[:mid]
        Right = data[mid:]
        
        merge_sort(Left)
        merge_sort(Right)
        
        i = j = k = 0 
        
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                data[k] = Left[i]
                i += 1
            else:
                data[k] = Right[j]
                j += 1
            k += 1
        while i < len(Left):
            data[k] = Left[i]
            i += 1
            k += 1
        while j < len(Right):
            data[k] = Right[j]
            j += 1
            k += 1
    return data

data = [38,27,43,3,9,82,10]

print (f"Data Sebelum di sorting {data}")

merge_sort(data)

print (f"Data Sesudah di sorting {data}")



