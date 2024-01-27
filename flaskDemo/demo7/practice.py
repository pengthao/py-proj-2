input = [4,7,8,45,21,8,3,17,2] 

def biggest_num(input):
    input.sort()
    return input[-1]


print(biggest_num(input))

def big_num_two(input):
    big_num = max(input)
    return big_num

print(big_num_two(input))

def big_num_three(arr):
    max_value = 0
    left, right = 0, len(arr)-1
    while left <= right:
        if arr[left] > arr[right]:
            max_value=max(max_value, arr[left])
            left += 1
        else: max_value = max(max_value, arr[right])
        right -= 1
    return max_value



print(big_num_three(input))