import random
import unittest
from pdqsort import PDQSort

INT_MAX = 128
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
    num = PDQSort._partitionLeft(0, len(array)-1, 0, array)
    self.assertEqual(num, 1)

    array = [1,1]
    num = PDQSort._partitionLeft(0, len(array)-1, 1, array)
    self.assertEqual(num, 2)

    array = [2,1,3,1,4,1,1,5]
    num = PDQSort._partitionLeft(0, len(array)-1, 1, array)
    self.assertEqual(num, 4)
    self.assertEqual(array, [1,1,1,1,4,3,2,5])

  def test_pressure_partition_left(self):
    for _ in range(TEST_TIMES):
      array = [random.randint(0, INT_MAX) for _ in range(random.randint(1, TEST_LENGTH_BOUND))]
      left = random.randint(0, len(array)//10)
      
      min_val = min(array[left:])
      min_val_ids = [i for i, val in enumerate(array) if val == min_val and i >= left]
      pivot_idx = random.choice(min_val_ids)

      num = PDQSort._partitionLeft(left, len(array)-1, pivot_idx, array)
      self.assertEqual(num, len(min_val_ids))


  if __name__ == "__main__":
    unittest.main()