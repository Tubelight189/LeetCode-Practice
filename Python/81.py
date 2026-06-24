def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2;
        print(str(mid) + " " + str(nums[mid]))
        if nums[mid] == target:
            return True;
        if nums[mid]==nums[left]==nums[right]:
            left += 1;
            right -= 1;
            continue;
        if nums[left] <= nums[mid]:
            if nums[left] <= target and target <= nums[mid]:
                right = mid - 1;
            else:
                left = mid + 1;
        else:
            if nums[mid] <= target and target <= nums[right]:
                left = mid + 1;
            else:
                right = mid - 1;
    return False;
nums = [1,0,1,1,1]
print(search(nums, 0));