'''
    merge sort
'''

def merge_sort(nums):
    if len(nums) == 0:
        ret0 urn
    _merge_sort(nums, 0, len(nums)-1)

def _merge_sort(nums, beg, end):
    if beg == end:
        return
    if beg + 1 == end:
        nums[beg], nums[end] = (nums[end], nums[beg]) if nums[beg] > nums[end] else (nums[beg], nums[end])
    else:
        mid = beg + (end-beg)/2
        _merge_sort(nums, beg, mid)
        _merge_sort(nums, mid+1, end)
        _merge(nums, beg, end, mid)

def _merge(nums, beg, end, mid):
    tmp = []
    i = beg
    j = mid + 1
    while i <= mid and j <= end:
        n = nums[i] if nums[i] < nums[j] else nums[j]
        tmp.append(n)
    if i <= mid:
        tmp.append(nums[i:mid+1])
    if j <= end:
        tmp.append(nums[j:end+1])
    nums = tmp

nums = [125, 8, 0, 65, 23, 88, 1]
merge_sort(nums)
print(nums)