def bsearchR(nums, li, hi, val):
    if (li > hi):
        return 1 # better to raise exception
    mi = int((li + hi ) / 2)
    if (nums[mi] == val):
        return mi
    if (val < nums[mi]):
        return bsearchR(nums, li, mi, val)
    if (val < nums[mi]):
        return bsearchR(nums, mi, hi, val)
def main():
    nums = [3,4,5,2]
    print(bsearchR(nums,5,3,2))
main()
