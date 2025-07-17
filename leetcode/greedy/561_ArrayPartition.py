nums = list(map(int, input().split()))

def arrayPairSum(nums):
    nums.sort()
    output = 0

    for k in range(0, len(nums), 2):
        output += nums[k]

    return output

print(arrayPairSum(nums))