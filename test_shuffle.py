import random
from pdqsort import PDQSort

TOSHUFFLE = True

res = []
nums = [0, 1, 2, 3]
for i in range(2048):
  arr = [nums[i % 4]] * random.randint(4, 36) + \
        [nums[(i+1) % 4]] * random.randint(36, 128) + \
        [nums[(i+2) % 4]] * random.randint(36, 128) + \
        [nums[(i+3) % 4]] * random.randint(4, 36)
  
  pivot_idx = PDQSort._choosePivot(0, len(arr)-1, len(arr), arr)
  mid, _ = PDQSort._partitionRight(0, len(arr)-1, pivot_idx, arr)
  left_size = mid + 1
  right_size = (len(arr)-1) - (mid+1) + 1
  if right_size <= left_size // 8:
    size = mid + 1
    if size >= PDQSort.INSERTION_SORT_THRESHOLD:
      if TOSHUFFLE: PDQSort._shufflePattern(0, len(arr)-1, mid, arr)
      pivot_idx = PDQSort._choosePivot(0, mid, size, arr)
      new_mid, _ = PDQSort._partitionRight(0, mid, pivot_idx, arr)
      res.append(min(new_mid/size, 1 - new_mid/size))
  elif left_size <= right_size // 8:
    size = len(arr) - mid - 1
    if size >= PDQSort.INSERTION_SORT_THRESHOLD:
      if TOSHUFFLE: PDQSort._shufflePattern(0, len(arr)-1, mid, arr)
      pivot_idx = PDQSort._choosePivot(mid+1, len(arr)-1, size, arr)
      new_mid, _ = PDQSort._partitionRight(mid+1, len(arr)-1, pivot_idx, arr)
      res.append(min((new_mid-mid-1) / size, 1 - (new_mid-mid-1) // size))
  else: continue

print("Average Partition Score: {:.4f}".format(sum(res)/len(res)))