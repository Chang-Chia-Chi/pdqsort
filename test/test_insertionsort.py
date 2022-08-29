import random
import unittest
from insertionsort import InsertionSort

INT_MAX = 128
TEST_TIMES = 1024
TEST_LENGTH_BOUND = 256

class TestInsertionSort(unittest.TestCase):
  def test_pressure_insertionsort(self):
    for _ in range(TEST_TIMES):
      array = [random.randint(0, INT_MAX) for _ in range(random.randint(1, TEST_LENGTH_BOUND))]
      left, right = random.randint(0, len(array)//4 * 2), random.randint(len(array)//4 * 3, len(array)-1)
      expect = array[:left] + sorted(array[left:right+1]) + array[right+1:]

      InsertionSort.sort(left, right, array)

      self.assertEqual(array, expect)

  def test_pressure_partial_insertionsort(self):
    for _ in range(TEST_TIMES):
      array1 = [random.randint(0, INT_MAX) for _ in range(random.randint(1, TEST_LENGTH_BOUND))]
      array2 = array1.copy()
      left, right = random.randint(0, len(array1)//4 * 2), random.randint(len(array1)//4 * 3, len(array1)-1)
      expect = array1[:left] + sorted(array1[left:right+1]) + array1[right+1:]

      if InsertionSort.partial_sort(left, right, array2):
        self.assertEqual(array2, expect)
