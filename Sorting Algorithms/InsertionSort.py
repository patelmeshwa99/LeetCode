def insertion_sort(items):    
    for i in range(1, len(items)):
        index = i
        for j in range(i)[::-1]:
            if items[j] > items[index]:
                temp = items[j]
                items[j] = items[index]
                items[index] = temp
                index = j

    print(items)
items = [5, 3, 8, 4, 2]
insertion_sort(items)
