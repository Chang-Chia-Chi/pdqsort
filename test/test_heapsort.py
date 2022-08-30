import random
import unittest
from heapsort import HeapSort

INT_MAX = 128
TEST_TIMES = 1024
TEST_LENGTH_BOUND = 256

class TestHeapSort(unittest.TestCase):
  def test_pressure_heapify(self):
    for _ in range(TEST_TIMES):
      array = [random.randint(0, INT_MAX) for _ in range(random.randint(1, TEST_LENGTH_BOUND))]
      left, right = random.randint(0, len(array)//4 * 2), random.randint(len(array)//4 * 3, len(array)-1)

      HeapSort._heapify(left, right, array)

      subarray = array[left:right+1]
      for root in range(len(subarray)//2 - 1):
        left, right = root * 2 + 1, root * 2 + 2
        if left <= right: self.assertTrue(subarray[root] >= subarray[left])
        if right <= right: self.assertTrue(subarray[root] >= subarray[right])

  def test_pressure_heapsort(self):
    for _ in range(TEST_TIMES):
      array = [random.randint(0, INT_MAX) for _ in range(random.randint(1, TEST_LENGTH_BOUND))]
      left, right = random.randint(0, len(array)//4 * 2), random.randint(len(array)//4 * 3, len(array)-1)
      expect = array[:left] + sorted(array[left:right+1]) + array[right+1:]

      HeapSort.sort(left, right, array)

      self.assertEqual(array, expect)
