from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    return str(self.__dq)

  def __len__(self):
    return len(self.__dq)

  def enqueue(self, val):
    return self.__dq.push_back(val)
    #pushes the value from the back

  def dequeue(self):
    return self.__dq.pop_front()
    #pops the value from the front and returns

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
  
