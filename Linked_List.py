class Linked_List:
  
  class __Node:

    # def __init__(self, val):
    # declares private variables for nodes
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

  # def __init__(self):
  # creates the attributes of the linked-list
  def __init__(self):
        self.__header = Linked_List.__Node(None)
        self.__header.prev = None
        self.__trailer = Linked_List.__Node(None)
        self.__trailer.next = None
        self.__length = 0

  # def __len__(self):
  # returns the length of the linked list
  def __len__(self):
    return self.__length

  # def append_element(self, val):
  # Checks to see if the list is empty.
  # If yes creates new node and links to header and trailer
  # If no, it links to nodes in end of list.
  def append_element(self, val):
    new_node = Linked_List.__Node(val)

    if (self.__length == 0):
      self.__header.next = new_node
      self.__trailer.prev = new_node
      new_node.next = self.__trailer
      new_node.prev = self.__header

    else:
      new_node.prev = self.__trailer.prev
      self.__trailer.prev.next = new_node
      self.__trailer.prev = new_node
      new_node.next = self.__trailer

    self.__length = self.__length + 1

  # def insert_element_at(self, val, index):
  # Checks to see if the position is valid.
  # If not, raises an index error.
  # If yes, goes to the position and inserts the element.
  # Increments length.
  def insert_element_at(self, val, index):
    if (index >= self.__length or index < 0):
        raise IndexError("Invalid position to insert")

    new_node = Linked_List.__Node(val)
    if (index <= len(self) // 2):
      currentNode = self.__header
      for i in range(0, index):
         currentNode = currentNode.next
    else:
      currentNode = self.__trailer
      for j in range(0, len(self) - index + 1):
        currentNode = currentNode.prev
    new_node.next = currentNode.next
    currentNode.next.prev = new_node
    new_node.prev = currentNode
    currentNode.next = new_node

    self.__length = self.__length + 1

  # def remove_element_at(self, index):
  # Checks to see if the index is valid to remove.
  # If no, raises an index error.
  # If yes, goes to position and removes index
  # returning the element stored.
  # decrements the length
  def remove_element_at(self, index):
    if (index >= self.__length or index < 0):
      raise IndexError("Invalid position to remove")

    if (index < len(self) // 2):
      currentNode = self.__header
      for i in range(0, index):
         currentNode = currentNode.next
    else:
      currentNode = self.__trailer
      for j in range(0, len(self) - index + 1):
        currentNode = currentNode.prev

    now = currentNode.next
    currentNode.next.next.prev = currentNode
    currentNode.next = currentNode.next.next
    self.__length = self.__length - 1

    return now.val

  # def get_element_at(self, index):
  # Checks to see if the index is valid.
  # if not raises an index error.
  # If yes, it goes to position and returns
  # element stored at that position.
  def get_element_at(self, index):
    if (index >= self.__length or index < 0):
        raise IndexError("Out of list range")

    if (index < len(self) // 2):
        currentNode = self.__header
        for i in range(0, index + 1):
            currentNode = currentNode.next
    else:
        currentNode = self.__trailer
        for j in range(0, len(self) - index):
            currentNode = currentNode.prev

    return currentNode.val

  # def rotate_left(self):
  # This rotates the linked list data left
  def rotate_left(self):
    if (self.__length <= 1):
      return

    else:
      back = self.__trailer.prev
      middle = self.__header.next
      front = middle.next

      self.__header.next = front
      front.prev = self.__header
      self.__trailer.prev = middle
      middle.next = self.__trailer
      back.next = middle
      middle.prev = back
        
  # def __str__(self):
  # Goes through the linked list, concatenating the
  # data stored into a "string of nodes."
  # Once all of the data has been reached, it returns the properly
  # formatted string for display.
  def __str__(self):
    if (self.__length < 1):
      return "[ ]"

    stringNode = "[ "
    for stringy in self:
        stringNode = stringNode + str(stringy) + ", "
    stringNode = stringNode[0:len(stringNode) - 2]
    stringNode = stringNode + " ]"
    return stringNode

  def __iter__(self):
    # initialize a new attribute for walking through your list
    # insert your initialization code before the return
    # statement. do not modify the return statement.
    self.__iteration = 0
    self.__current = self.__header.next
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.

    if (self.__iteration == self.__length):
      raise StopIteration
    else:
      self.__iteration = self.__iteration + 1
      tempNode = self.__current
      self.__current = self.__current.next
      return tempNode.val

#if __name__ == '__main__':
