from insertionsort import InsertionSort
from heapsort import HeapSort

class PDQSort:

  INSERTION_SORT_THRESHOLD = 24
  NINTHER_THRESHOLD = 128

  @classmethod
  def sort(cls, array):
    pass
  

  @classmethod
  def _partitionRight(cls, left, right, pivot_idx, array):
    """
    Partitions array within [left, right] with array[pivotIdx].
    Elements larger or equal to pivot will be put on the right-hand
    side of the array.

    @params left: left bound of partition
    @params right: right bound of partition
    @params pivot_idx: index of pivot in array
    @params array: array to be sorted

    @return (next_pivot_idx, no_swap): (next pivot index, true if range [left, right] of array is already partitioned)
    """
    pivot = array[pivot_idx]
    array[left], array[pivot_idx] = array[pivot_idx], array[left]

    i, j = left + 1, right
    while i <= j and array[i]  < pivot: i += 1
    while i <= j and array[j] >= pivot: j -= 1

    no_swap = i > j

    while i <= j:
      array[i], array[j] = array[j], array[i]
      while array[i]  < pivot: i += 1
      while array[j] >= pivot: j -= 1
    
    array[left], array[j] = array[j], array[left]
    return j, no_swap

  @classmethod
  def _partitionLeft(cls, left, right, pivot_idx, array):
    pivot = array[pivot_idx]
    array[left], array[pivot_idx] = array[pivot_idx], array[left]

    i, j = left + 1, right
    while i <= j and array[i] <= pivot: i += 1
    while i <= j and array[j]  > pivot: j -= 1

    while i <= j:
      array[i], array[j] = array[j], array[i]
      while array[i] <= pivot: i += 1
      while array[j]  > pivot: j -= 1
    
    # no swap needed because we know all the elements on left-hand side are equal to pivot
    # i - left is number of elements equals to pivot, including pivot itself
    return i - left

  @classmethod
  def _shufflePattern(cls, left, right, pivot_idx, arr):
    left_size, right_size = pivot_idx - left, right - (pivot_idx + 1)
    cls._shuffle(left, pivot_idx, left_size, arr)
    cls._shuffle(pivot_idx + 1, right, right_size, arr)

  @classmethod
  def _shuffle(cls, left, right, size, arr):
    if size >= PDQSort.INSERTION_SORT_THRESHOLD:
      arr[left], arr[left + size//4] = arr[left + size//4], arr[left]
      arr[right], arr[right - size//4] = arr[right - size//4], arr[right]

      if size > PDQSort.NINTHER_THRESHOLD:
        arr[left + 1], arr[left + (size//4 + 1)] = arr[left + (size//4 + 1)], arr[left + 1]
        arr[left + 2], arr[left + (size//4 + 2)] = arr[left + (size//4 + 2)], arr[left + 2]
        arr[right - 1], arr[right - size//4 - 1] = arr[right - size//4 - 1], arr[right - 1]
        arr[right - 2], arr[right - size//4 - 2] = arr[right - size//4 - 2], arr[right - 2]

  @classmethod
  def _choosePivot(cls, left, right, size, arr):
    def sort3(a, b, c):
      if arr[b] < arr[a]: a, b = b, a
      if arr[c] < arr[b]: b, c = c, b
      if arr[b] < arr[a]: a, b = b, a
      return b

    half = size // 2
    if size > PDQSort.NINTHER_THRESHOLD:
      a = sort3(left + 1, left + half - 1, right - 1)
      b = sort3(left, left + half, right)
      c = sort3(left + 2, left + half + 2, right - 2)
      return sort3(a, b, c)
    else:
      return sort3(left + half, left, right)



