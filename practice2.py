class Solution(object):
for i in range (len(nums)):
    temp_num = nums[i]
    nums.remove(nums[i])
    nums.insert(i, temp_num)
    temp_list = nums[:]
    temp_list.pop(i)
    temp_list.insert(i, "empty")
    if (target - nums[i]) in temp_list:
        print ("found", [i, temp_list.index(target - nums[i])])
        break
    else:
        
        continue


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        