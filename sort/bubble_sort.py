def bubble_sort(list):
    # If the list contains n elements, we need to do n-1 comparisons
    # to get the largest number at the end
    # e.g. 6 elements ==> 5 comparisons
    # e.g. 5 elements ==> 4 comparisons

    # We will iterate through a range from n-1 to 0
    for i in range(len(list) - 1, 0, -1):
        # i = 5, 5 comparisons
        # i = 4, 4 comparisons
        for j in range(i):
            if list[j] > list[j+1]:
                # swap the element
                # temp = list[j]
                # list[j] = list[j+1]
                # list[j+1] = temp

                # short form
                list[j], list[j+1] = list[j+1], list[j]
    return list

my_list = [4, 2, 6, 5, 1, 3]
print(bubble_sort(my_list))     # [1, 2, 3, 4, 5, 6]