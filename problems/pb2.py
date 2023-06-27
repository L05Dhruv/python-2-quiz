def max_values(nums):
  two_indices = []
  min_val = min(nums)

  for i in range(2):
    idx = nums.index(max(nums)) # get max value and extract index
    two_indices.append(idx)     # append that index to our returned list
    nums[idx] = min_val         #  marks index as used
    # print(nums)

  return two_indices





def max_values2(nums):
  two_indices = [0, 0]
  p1 = nums[0]
  p2 = nums[0]

  for i in range(len(nums)):
    if nums[i] > p1:
      p1 = nums[i]
      two_indices[0] = i
  # nums[two_indices[0]] = float('-inf')
  
  for i in range(len(nums)):
    if nums[i] > p2 and nums[i] != p1:
      p2 = nums[i]
      two_indices[1] = i
  
  return two_indices


# print(max_values2([4, 7, 2, 8, 10, 9])) # -> [4, 5]
print(max_values2([-5, -2, -1, -11])) # -> [1, 2]
