# for sys.argv, the command-line arguments
import sys 
from Stack import Stack

# def delimiter_check(filename):
# Sets a constructor equal to the stack
# Has a set to check against the delimiters and creates a variable
# to open the file
# From here it goes through the file and if the characters match
# then they are popped off until the length is 0 returning True
# Otherwise it returns False
# It then closes the file (always good practice).
def delimiter_check(filename):
 
  stackInput = Stack()
  characterMap = {"]" : "[", "}" : "{", ")" : "("}
  fileToOpen = open(filename)
  
  for char in (fileToOpen):
    if (char == '(' or char == '[' or char == '{'):
      stackInput.push(char)
    elif (char ==  ')' or char == ']' or char == '}'):
      if characterMap[char] == stackInput.peek():
        stackInput.pop()
      else:
        return False
  
  if (len(stackInput) == 0):
    return True

  fileToOpen.close()
  
      

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


