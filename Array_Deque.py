from Deque import Deque

class Array_Deque(Deque):
  # def __init__(self):
  # Initializes the attributes of the deque.
  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__length = 0
    self.__front = 0

  # def __str__(self):
  # Checks to see if the length is 0
  # if yes, returns empty string otherwise
  # sets a pointer to the contents and walks through
  # until the length of the array is reached and returns the result
  def __str__(self):

    if (self.__length == 0):
      return "[ ]"
    
    previousArray = self.__contents
    front = self.__front
    stringArray = "[ "
    for i in range(self.__length):
      stringArray = stringArray + str(previousArray[front]) + ", "
      front = (front + 1) % len(previousArray)
    stringArray = stringArray[0:len(stringArray) - 2]
    stringArray = stringArray + " ]"

    return stringArray
  
  # def __len__(self): 
  # Returns the length of the array
  def __len__(self):
    return self.__length

  # def __grow(self):
  # Creates a pointer to the current contents
  # puts a pointer to the front
  # increases the capacity by mulitplicity of 2
  # does a current walk and adds the old contents to the newly
  # created array and places the front back at index 0
  def __grow(self):

    oldArray = self.__contents
    front = self.__front
    self.__capacity = self.__capacity * 2
    self.__contents = ([None] * self.__capacity)
    
    for current in range (self.__length):
      self.__contents[current] = oldArray[front]
      front = (front + 1) % len(oldArray)
      current = current + 1
    self.__front = 0
    
  # def push_front(self, val):
  # Checks to see if the array is full
  # if yes, it grows it, otherwise
  # finds the new position for the front
  # places the contents into the array and increments size
  def push_front(self, val):

    if (self.__length == self.__capacity):
      self.__grow()
    
    newPosition = ((self.__front - 1) % len(self.__contents))
    self.__front = newPosition
    self.__contents[newPosition] = val
    self.__length = self.__length + 1

  # def pop_front(self):
  # If the length of array is 0 return
  # Otherwise uses a pointer to the location of front
  # sets the contents to None and decrements the count
  # returning the value which was removed
  def pop_front(self):

    if (self.__length == 0):
      return None
    
    popFront = self.__contents[self.__front]
    self.__contents[self.__front] = None
    self.__front = ((self.__front + 1) % len(self.__contents))
    self.__length = self.__length - 1
    
    return popFront

  # def peek_front(self):
  # Checks if the array is empty
  # If so returns None, otherwise returns the contents
  # located at the front
  def peek_front(self):

    
    if (self.__length==0):
      return None

    return self.__contents[self.__front]
    
  # def push_back(self, val):
  # Checks to see if array is full
  # If yes then grows it, otherwise
  # finds and sets the contents of the back position
  # incrementing the length
  def push_back(self, val):

    if (self.__length == self.__capacity):
        self.__grow()
    
    newPosition = ((self.__front + self.__length) % len(self.__contents))
    self.__contents[newPosition] = val
    self.__length = self.__length + 1
  
  # def pop_back(self):
  # If the array has a size of 0
  # returns None, otherwise gets position
  # sets pointer to that contents, removes that value
  # decrements the count and returns that value
  def pop_back(self):

    if (self.__length == 0):
      return None
    
    getPosition = ((self.__front + self.__length - 1) % (len(self.__contents)))
    popBack = self.__contents[getPosition]
    self.__contents[self.__front] = None
    self.__length = self.__length - 1
    
    return popBack

  # def peek_back(self):
  # Checks to see if array is size 0
  # if yes returns None, otherwise
  # has a pointer set to the back content
  # and returns that value
  def peek_back(self):

    if (self.__length==0):
      return None
    
    getPosition = ((self.__front + self.__length - 1) % len(self.__contents))
    peekBack = self.__contents[getPosition]
    
    return peekBack

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
