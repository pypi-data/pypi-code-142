from jsonwhatever import JsonWhatEver

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

class Dog:
  def __init__(self) -> None:
    self.id = 0
    self.name = 'fido'
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
class_example = Person(9,'john',dog_a)
bytes_example = bytes(4)
bytearray_example = bytearray(4)

#########################
jsonwe = JsonWhatEver()
#########################

#prints {"list_example":[4,5,6,8]}
print(jsonwe.jsonwhatever('list_example',list_b))

#prints {"name":"john"}
print(jsonwe.jsonwhatever('name','john'))

#prints {"size":1.7}
print(jsonwe.jsonwhatever('size',1.7))

#prints {"empty_list":[]}
print(jsonwe.jsonwhatever('empty_list',empty_list))

#prints {"none_example":null}
print(jsonwe.jsonwhatever('none_example',none_var))

#prints {"boolean":True}
print(jsonwe.jsonwhatever('boolean',bool_var))

#prints {"empty_set":[]}
print(jsonwe.jsonwhatever('empty_set',set_example_empty))

#prints {"set_example":[1,2,3,4]}
print(jsonwe.jsonwhatever('set_example',set_example))

#prints {"brand":"Ford","model":"Mustang","year":1964}
print(jsonwe.jsonwhatever('thisdict',thisdict))

#prints {"id":9,"name":"juan",{"id":0,"name":"perro","size":5.3}}
print(jsonwe.jsonwhatever('person_class',class_example))

#prints {"bytes_example":"b'\x00\x00\x00\x00'"}
print(jsonwe.jsonwhatever('bytes_example',bytes_example))

#prints {"bytearray_example":"b'\x00\x00\x00\x00'"}
print(jsonwe.jsonwhatever('bytearray_example',bytearray_example))

#prints {"crazy_list":[4,5,{"brand":"Ford","model":"Mustang","year":1964},8,"(5+9j)"]}
print(jsonwe.jsonwhatever('crazy_list',list_c))
