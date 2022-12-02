from jsonwhatever import jsonwhatever

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

class Dog:
  def __init__(self) -> None:
    self.id = 0
    self.name = 'perro'
    self.size = 5.3

class Person:
  def __init__(self, id, name, dog) -> None:
    self.id = id
    self.name = name
    self.dog = dog

dog_a = Dog()

complex_number = 5+9j
list_b = [4,5,6,8]
list_a = [2,3,'hello',7,list_b]
list_c = [4,5,thisdict,8,complex_number]
empty_list = []
none_var = None
bool_var = True
set_example_empty = set()
set_example = {1,2,3,4}
class_example = Person(9,'juan',dog_a)
bytes_example = bytes(4)
bytearray_example = bytearray(4)

print(jsonwhatever('list_example',list_b))
print(jsonwhatever('name','john'))
print(jsonwhatever('size',1.7))
print(jsonwhatever('empty_list',empty_list))
print(jsonwhatever('none_example',none_var))
print(jsonwhatever('boolean',bool_var))
print(jsonwhatever('empty_set',set_example_empty))
print(jsonwhatever('set_example',set_example))
print(jsonwhatever('thisdict',thisdict))
print(jsonwhatever('person_class',class_example))
print(jsonwhatever('bytes_example',bytes_example))
print(jsonwhatever('bytearray_example',bytearray_example))
print(jsonwhatever('crazy_list',list_c))
