import time
import random
import unittest
from pdqsort import PDQSort

INT_MAX = 24
TEST_TIMES = 2048
TEST_LENGTH_BOUND = 1024

class TestPartition(unittest.TestCase):

  def test_pressure_partition_right(self):
    for i in range(TEST_TIMES):
      array = [random.randint(0, INT_MAX) for _ in range(random.randint(1, TEST_LENGTH_BOUND))]
      pivot_idx = random.randint(0, len(array)-1)
      pivot = array[pivot_idx]
      new_pivot_idx, _ = PDQSort._partitionRight(0, len(array)-1, pivot_idx, array)

      for i in range(new_pivot_idx):
        self.assertTrue(array[i] < pivot)
      for i in range(new_pivot_idx, len(array)):
        self.assertTrue(array[i] >= pivot)


  def test_no_swap_partition_right(self):
    array = [0]
    _, no_swap = PDQSort._partitionRight(0, len(array)-1, 0, array)
    self.assertTrue(no_swap)

    array = [1,2,3,4,5]
    for p_idx in range(len(array)):
      _, no_swap = PDQSort._partitionRight(0, len(array)-1, p_idx, array)
      self.assertTrue(no_swap)

    array = [1,1,1,1]
    for p_idx in range(len(array)):
      _, no_swap = PDQSort._partitionRight(0, len(array)-1, p_idx, array)
      self.assertTrue(no_swap)


  def test_simple_partition_left(self):
    array = [1]
    pivot_idx = PDQSort._partitionLeft(0, len(array)-1, 0, array)
    self.assertEqual(pivot_idx, 1)

    array = [1,1]
    pivot_idx = PDQSort._partitionLeft(0, len(array)-1, 1, array)
    self.assertEqual(pivot_idx, 2)

    array = [2,1,3,1,4,1,1,5]
    pivot_idx = PDQSort._partitionLeft(0, len(array)-1, 1, array)
    self.assertEqual(pivot_idx, 4)
    self.assertEqual(array, [1,1,1,1,4,3,2,5])

  def test_pressure_partition_left(self):
    for _ in range(TEST_TIMES):
      array = [random.randint(0, INT_MAX) for _ in range(random.randint(1, TEST_LENGTH_BOUND))]
      left = random.randint(0, len(array)//10)
      
      min_val = min(array[left:])
      min_val_ids = [i for i, val in enumerate(array) if val == min_val and i >= left]
      pivot_idx = random.choice(min_val_ids)

      pivot_idx = PDQSort._partitionLeft(left, len(array)-1, pivot_idx, array)
      self.assertEqual(pivot_idx-left, len(min_val_ids))


  def test_pressure_pdqsort(self):
    for _ in range(TEST_TIMES):
      array = [random.randint(0, INT_MAX) for _ in range(random.randint(1, TEST_LENGTH_BOUND))]
      expect = sorted(array)

      PDQSort.sort(array)

      self.assertEqual(array, expect)

  def test_time_perf(self):
    time_qsort, time_pdqsort = [], []
    for _ in range(TEST_TIMES):
      array1 = [random.randint(0, INT_MAX) for _ in range(random.randint(1, TEST_LENGTH_BOUND))]
      array2 = array1.copy()

      s_time = time.perf_counter_ns()
      self.naive_qsort(0, len(array1)-1, array1)
      time_qsort.append(time.perf_counter_ns() - s_time)

      s_time = time.perf_counter_ns()
      PDQSort.sort(array2)
      time_pdqsort.append(time.perf_counter_ns() - s_time)
    
    print("pdqsort is {:.3f} times faster than naive quicksort.".format(sum(time_qsort) / sum(time_pdqsort)))


  def naive_qsort(self, left, right, array):
    """Ref: https://ithelp.ithome.com.tw/articles/10202330?sc=iThelpR"""
    if left >= right: return

    i = left
    j = right
    key = array[left]

    while i != j:                  
        while array[j] > key and i < j:
            j -= 1
        while array[i] <= key and i < j:
            i += 1
        if i < j:
            array[i], array[j] = array[j], array[i] 

    array[left] = array[i] 
    array[i] = key

    self.naive_qsort(left, i-1, array)
    self.naive_qsort(i+1, right, array)
