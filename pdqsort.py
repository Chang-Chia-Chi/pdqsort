from multiprocessing.heap import Heap
from insertionsort import InsertionSort
from heapsort import HeapSort

class PDQSort:

  INSERTION_SORT_THRESHOLD = 24
  NINTHER_THRESHOLD = 128

  @classmethod
  def sort(cls, array):
    bad_limit = len(array).bit_length()
    cls._pdqsortLoop(0, len(array)-1, bad_limit, array, prev_pivot=None)

  @classmethod
  def _pdqsortLoop(cls, left, right, bad_limit, array, prev_pivot):
    while True:
      size = right - left + 1

      # Using insertion sort when array is small
      if size <= cls.INSERTION_SORT_THRESHOLD:
        InsertionSort.sort(left, right, array)
        return
      
      # choose a pivot with median of 3 ninether
      pivot_idx = cls._choosePivot(left, right, size, array)

      # if we choose the same pivot again, use partition_left
      if prev_pivot and prev_pivot == array[pivot_idx]:
        left = cls._partitionLeft(left, right, pivot_idx, array)
        continue
      
      # partition_right and check is partition good or not
      pivot_new_idx, no_swap = cls._partitionRight(left, right, pivot_idx, array)
      left_size, right_size = pivot_new_idx - left + 1, right - pivot_new_idx
      unbalanced = left_size < size / 8 or right_size < size / 8

      # if partition is bad, we shuffle the pattern
      if unbalanced:
        bad_limit -= 1
              
        # Fall back to heap sort when too many bad pivot pick were made
        if bad_limit == 0:
          HeapSort.sort(left, right, array)
          return
        
        cls._shufflePattern(left, right, pivot_new_idx, array)
      else:
        # if no swap at this partition, try to use partial insertion sort
        # return immediately if both side are already sorted
        if (no_swap and
            InsertionSort.partial_sort(left, pivot_new_idx-1, array) and
            InsertionSort.partial_sort(pivot_new_idx+1, right, array)): return
      
      # recurse left-hand side first, be care that predecessor of left-hand side
      # is it's parent predecessor
      cls._pdqsortLoop(left, pivot_new_idx, bad_limit, array, prev_pivot)
      prev_pivot = array[pivot_new_idx]
      left = pivot_new_idx + 1

  @classmethod
  def _partitionRight(cls, left, right, pivot_idx, array):
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
    
    # no swap needed because we know all the elements
    # on left-hand side are equal to pivot
    return i

  @classmethod
  def _shufflePattern(cls, left, right, pivot_idx, array):
    left_size, right_size = pivot_idx - left, right - (pivot_idx + 1)
    cls._shuffle(left, pivot_idx, left_size, array)
    cls._shuffle(pivot_idx + 1, right, right_size, array)

  @classmethod
  def _shuffle(cls, left, right, size, array):
    if size >= PDQSort.INSERTION_SORT_THRESHOLD:
      array[left], array[left + size//4] = array[left + size//4], array[left]
      array[right], array[right - size//4] = array[right - size//4], array[right]

      if size > cls.NINTHER_THRESHOLD:
        array[left + 1], array[left + (size//4 + 1)] = array[left + (size//4 + 1)], array[left + 1]
        array[left + 2], array[left + (size//4 + 2)] = array[left + (size//4 + 2)], array[left + 2]
        array[right - 1], array[right - size//4 - 1] = array[right - size//4 - 1], array[right - 1]
        array[right - 2], array[right - size//4 - 2] = array[right - size//4 - 2], array[right - 2]

  @classmethod
  def _choosePivot(cls, left, right, size, array):
    def sort3(a, b, c):
      if array[b] < array[a]: a, b = b, a
      if array[c] < array[b]: b, c = c, b
      if array[b] < array[a]: a, b = b, a
      return b

    half = size // 2
    if size > cls.NINTHER_THRESHOLD:
      a = sort3(left + 1, left + half - 1, right - 1)
      b = sort3(left, left + half, right)
      c = sort3(left + 2, left + half + 2, right - 2)
      return sort3(a, b, c)
    else:
      return sort3(left + half, left, right)
