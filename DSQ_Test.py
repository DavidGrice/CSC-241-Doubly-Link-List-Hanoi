import unittest
from Deque_Generator import get_deque, LL_DEQUE_TYPE, ARR_DEQUE_TYPE
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__arrayDeque = get_deque(ARR_DEQUE_TYPE)
    self.__arrayStack = Stack()
    self.__arrayQueue = Queue()

    self.__linkedDeque = get_deque(LL_DEQUE_TYPE)
    self.__linkedStack = Stack()
    self.__linkedQueue = Queue()

  def test_emptyQueues(self):
    self.assertEqual('[ ]', str(self.__arrayQueue), 'Empty array queue should print as "[ ]"')
    self.assertEqual('[ ]', str(self.__linkedQueue), 'Empty list queue should print as "[ ]"')

  def test_emptyStacks(self):
    self.assertEqual('[ ]', str(self.__arrayStack), 'Empty array stack should print as "[ ]"')
    self.assertEqual('[ ]', str(self.__linkedStack), 'Empty list stack should print as "[ ]"')

  def test_add_stack_empty(self):
    self.__arrayStack.push('Victory')
    self.assertEqual('[ Victory ]', str(self.__arrayStack), 'Stack should print as "[ Victory ]"')

    self.__linkedStack.push('Always')
    self.assertEqual('[ Always ]', str(self.__linkedStack), 'Stack should print as "[ Always ]"')

  def test_add_queue_empty(self):
    self.__arrayQueue.enqueue('Victory')
    self.assertEqual('[ Victory ]', str(self.__arrayQueue), 'Queue should print as "[ Victory ]"')

    self.__linkedQueue.enqueue('Always')
    self.assertEqual('[ Always ]', str(self.__linkedQueue), 'Queue should print as "[ Always ]"')

  def test_push_three_pop_two(self):
    self.__arrayStack.push('Victory')
    self.__arrayStack.push('Is')
    self.__arrayStack.push('Certain')
    self.__arrayStack.pop()
    self.__arrayStack.pop()
    self.assertEqual('[ Victory ]', str(self.__arrayStack), 'Stack should print as "[ Victory ]"')

    self.__linkedStack.push('Always')
    self.__linkedStack.push('And')
    self.__linkedStack.push('Forever')
    self.__linkedStack.pop()
    self.__linkedStack.pop()
    self.assertEqual('[ Always ]', str(self.__linkedStack), 'Stack should print as "[ Always ]"')

  def test_enqueue_three_dequeue_two(self):
    self.__arrayQueue.enqueue('Victory')
    self.__arrayQueue.enqueue('Is')
    self.__arrayQueue.enqueue('Certain')
    self.__arrayQueue.dequeue()
    self.__arrayQueue.dequeue()
    self.assertEqual('[ Certain ]', str(self.__arrayQueue), 'Queue should print as "[ Certain ]"')

    self.__linkedQueue.enqueue('Always')
    self.__linkedQueue.enqueue('And')
    self.__linkedQueue.enqueue('Forever')
    self.__linkedQueue.dequeue()
    self.__linkedQueue.dequeue()
    self.assertEqual('[ Forever ]', str(self.__linkedQueue), 'Queue should print as "[ Forever ]"')

  def test_pop_three_from_empty_stacks(self):
    with self.assertRaises(IndexError):
      self.__arrayStack.pop()
      self.__arrayStack.pop()
      self.__arrayStack.pop()
      self.__linkedStack.pop()
      self.__linkedStack.pop()
      self.__linkedStack.pop()
    self.assertEqual('[ ]', str(self.__arrayStack), 'Should raise an Index Error')
    self.assertEqual('[ ]', str(self.__linkedStack), 'Should raise an Index Error')

  def test_dequeue_three_from_empty_queues(self):
    with self.assertRaises(IndexError):
      self.__arrayQueue.dequeue()
      self.__arrayQueue.dequeue()
      self.__arrayQueue.dequeue()

      self.__linkedQueue.dequeue()
      self.__linkedQueue.dequeue()
      self.__linkedQueue.dequeue()
    self.assertEqual('[ ]', str(self.__arrayQueue), 'Should raise an Index Error')
    self.assertEqual('[ ]', str(self.__linkedQueue), 'Should raise an Index Error')

  def test_length_of_stacks(self):
    for i in range(1000):
      self.__arrayStack.push(i)
      self.__linkedStack.push(i)
    self.assertEqual(1000, len(self.__arrayStack), 'Length should be 1000')
    self.assertEqual(1000, len(self.__linkedStack), 'Length should be 1000')
  
  def test_length_of_queues(self):
    for i in range(1000):
      self.__arrayQueue.enqueue(i)
      self.__linkedQueue.enqueue(i)
    self.assertEqual(1000, len(self.__arrayQueue), 'Length should be 1000')
    self.assertEqual(1000, len(self.__linkedQueue), 'Length should be 1000')
  
  def test_peek_of_stacks(self):
    for k in range(100):
      self.__arrayStack.push(k)
      self.__linkedStack.push(k)

    for _ in range(10):
      self.__arrayStack.pop()
      self.__linkedStack.pop()

    self.assertEqual(89, self.__arrayStack.peek(), 'Top should be 89')
    self.assertEqual(89, self.__linkedStack.peek(), 'Top should be 89')


if __name__ == '__main__':
  unittest.main()

