class HeapSort:

  @classmethod
  def sort(cls, left, right, array):
    cls._heapify(left, right, array)
    for curr in range(right, left, -1):
      array[curr], array[left] = array[left], array[curr]
      cls._bubbleDown(left, left, curr-1, array)

  @classmethod
  def _heapify(cls, left, right, array):
    half = left + (right - left + 1) // 2
    for curr in range(half, left - 1, -1):
      cls._bubbleDown(left, curr, right, array)

  @classmethod
  def _bubbleDown(cls, left, curr, right, array):
    root, right, offset = curr - left, right - left, left
    while True:
      child = root * 2 + 1
      if child > right: break
      if child + 1 <= right and array[child + offset] < array[child + 1 + offset]:
        child += 1
      
      if array[root + offset] < array[child + offset]:
        array[root + offset], array[child + offset] = array[child + offset], array[root + offset]
        root = child
      else: break
