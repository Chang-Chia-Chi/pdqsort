import bisect

class InsertionSort:

  PARTIAL_INSERTION_SORT_LIMIT = 8

  @classmethod
  def sort(cls, left, right, array):
    for i in range(left + 1, right + 1):
      if array[i] < array[i - 1]:
        tmp = array[i]
        insert_idx = bisect.bisect_right(array, array[i], left, i)

        j = i
        while j >= insert_idx:
          array[j] = array[j - 1]
          j -= 1
        array[insert_idx] = tmp

  @classmethod
  def partial_sort(cls, left, right, array):
    limit = 0
    for i in range(left + 1, right + 1):
      if array[i] < array[i - 1]:
        tmp = array[i]
        insert_idx = bisect.bisect_right(array, array[i], left, i)

        j = i
        while j >= insert_idx:
          array[j] = array[j - 1]
          j -= 1
        array[insert_idx] = tmp
        limit += i - insert_idx

      if limit > cls.PARTIAL_INSERTION_SORT_LIMIT: return False
    return True
