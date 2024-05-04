def search(nums, size, val):
    if size==0:
        return False
    #return search(nums, size-1, val) or (nums[size-1] == val)
    return (nums[size-1] == val) or search(nums, size-1, val)
nums = [7,1,3,4,2]
print(search(nums,5,2))
