# O(n^2) due to 2 for loops - not ideal
def longest_subarray(nums):
    max_len = -1
    for i in range(len(nums) - 1):
        max_local = 1
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[j - 1]:
                max_local += 1
            else:
                print(max_local)
                if max_local > max_len:
                    max_len = max_local
    return max_len


# O(n) for first traversal and O(n) for getting max value of max_till_now - Overall O(n)
def longest_subarray_dp(nums):
    max_till_now = [1 for _ in range(len(nums))]
    for i in range(0, len(nums) - 1):
        if nums[i + 1] > nums[i]:
            max_till_now[i + 1] = max_till_now[i] + 1
        else:
            max_till_now[i + 1] = 1
    print(max_till_now)
    return max(max_till_now)


if __name__ == '__main__':
    nums = [1, 5, 6, 3, 9]
    print(longest_subarray_dp(nums))
