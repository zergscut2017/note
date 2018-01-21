
def insertion_sort(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index-1
        while i>=0:
            if value < list[i]:
                list[i+1] = list[i] ## shift number in slot #i right to slot #(i+1)
                list[i] = value  ## shift value left to slot #i
                i = i - 1
            else:
                break

def merge(left,right):
    result = []
    i,j = 0, 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(list):
    if len(list) <=1:
        return list
    mid = int(len(list)/2)
    left = mergesort(list[:mid])
    right = mergesort(list[mid:])
    return merge(left, right)

a = [7, 1,3,5,10,21,3,0,11]
b = [7, 1,3,5,10,21,3,0,11]

insertion_sort(a)
print a

print mergesort(b)
