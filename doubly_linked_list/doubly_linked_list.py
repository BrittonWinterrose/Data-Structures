"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node # Each node is a ListNode and inherits the methods from that class. 
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    # need to handle two types of activity. Adding when I have a head and when head is currently none.
    if not self.head: # Adding to head when there is no head yet. 
      self.head = ListNode(value) # Create the head node. 
      self.tail = self.head # Also set the head node as the tail address. 
    else:  # Add to head (normal)
      self.head.insert_before(value) # Select the head then insert value before.
      self.head = self.head.prev # Change the head address to the inserted value. 
    self.length +=1

  def remove_from_head(self):
    # Need to handle size Zero, size 1, and size N lists...
    removed = None # Defining a variable that will hold the ListNode.value we'll remove.
    if self.length > 0: # Checks that list is greater than 0
      removed = self.head.value # Grabs the value we're pulling out. 
      if self.length == 1: # If a size 1 DLL....
        self.head = None # Set the head to None.
        self.tail = None # Set the tail to None, we just removed the last item.
      else:
        self.head.delete()
      self.length -= 1 # Subtract one for the deleted object.
    return removed # If there is no list and we run then return none...

  def add_to_tail(self, value):
    # Need to handle size zero and size N
    if not self.tail: #Size Zero
      self.tail = ListNode(value)
      self.head = self.tail
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next # Move the tail reference to the new tail address.
    self.length +=1

  def remove_from_tail(self):
    removed = None
    if self.length > 0:
      removed = self.tail.value
      if self.length == 1:
        self.tail = None
        self.head = None
      else:
        self.tail.delete
      self.length -= 1
    return removed

  def move_to_front(self, node):
    # First need to make sure I'm not moving the head
    if self.head != node:
      node.delete() # "Delete" the node, still have the object in this function for reference.
      self.head.insert_before(node.value) # Take the node value and insert it before the head.
      self.head = self.head.prev # Same as add to head.

  def move_to_end(self, node):
    # First need to make sure I'm not moving the tail
    if self.tail != node:
      node.delete()
      self.tail.insert_after(node.value)
      self.tail = self.tail.next

  def delete(self, node):
    # Need 3 conditions, when deleting head, tail or other.
    if self.head == node:  # Head Case
      self.head = self.head.next
    elif self.tail == node: # Tail Case
      self.tail = self.tail.prev
    else: # Other case
      node.delete()
    self.length -= 1 # In all cases
    
  def get_max(self):
    cursor = self.head # Cursor starts at the head. 
    max_value = cursor.value
    while cursor != self.tail:
      cursor = cursor.next
      if max_value < cursor.value: # Check if the new cursor location value is bigger.
        max_value == cursor.value
    return max_value
    
