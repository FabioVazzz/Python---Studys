# colletion = single "variable" used to store multiple value
# list = [] ordered and changleable. Duplicates OK
# set = {} unordered and immutable, but add/remove OK. NO duplicates
# ruple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut"]

# print(help(fruits))
# append(self, object, /)
#  |      Append object to the end of the list.
#  |
#  |  clear(self, /)
#  |      Remove all items from list.
#  |
#  |  copy(self, /)
#  |      Return a shallow copy of the list.
#  |
#  |  count(self, value, /)
#  |      Return number of occurrences of value.
#  |
#  |  extend(self, iterable, /)
#  |      Extend list by appending elements from the iterable.
#  |
#  |  index(self, value, start=0, stop=9223372036854775807, /)
#  |      Return first index of value.
#  |
#  |      Raises ValueError if the value is not present.
#  |
#  |  insert(self, index, object, /)
#  |      Insert object before index.
#  |
#  |  pop(self, index=-1, /)
#  |      Remove and return item at index (default last).
#  |
#  |      Raises IndexError if list is empty or index is out of range.
#  |
#  |  remove(self, value, /)
#  |      Remove first occurrence of value.
#  |
#  |      Raises ValueError if the value is not present.
#  |
#  |  reverse(self, /)
#  |      Reverse *IN PLACE*.
#  |
#  |  sort(self, /, *, key=None, reverse=False)
#  |      Sort the list in ascending order and return None.