def insertion_sort(items):    
    # This has unnecessary swapping
    # for i in range(1, len(items)):
    #     index = i
    #     for j in range(i)[::-1]:
    #         if items[j] > items[index]:
    #             temp = items[j]
    #             items[j] = items[index]
    #             items[index] = temp
    #             index = j

    # Tried shifting here
    for i in range(1, len(items)):
        value = items[i]
        j = i - 1
        while(j >= 0 and value < items[j]):
            items[j + 1] = items[j]
            j -= 1

items = [5, 3, 8, 4, 2]
insertion_sort(items)
