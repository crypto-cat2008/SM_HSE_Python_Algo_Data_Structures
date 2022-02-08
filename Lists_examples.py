empty_list = []
square_brackets_list = ["Hello",",","World","!"]
list_comprehension = [letter for letter in "some_string"]
with_type_constructor_list = list("some_string_2")

print(square_brackets_list[0])
print(square_brackets_list[1:3])

square_brackets_list[2] = "HSE"
square_brackets_list

print(square_brackets_list)

empty_list.append("new_item")
empty_list

print(empty_list)

square_brackets_list.insert(1,"INSERTION_AT_1")

print(square_brackets_list)

square_brackets_list.remove("INSERTION_AT_1")
print(square_brackets_list)
square_brackets_list.pop(1)
print(square_brackets_list)

list_of_letters = [letter for letter in "qwertyuiopasdfghjklzxcvbnm"]
print("LIST WITH LETTERS:",list_of_letters,sep='\n')
# list_of_letters.clear()
# print("EMPTY LIST:",list_of_letters,sep='\n')

list_of_letters.reverse()
print(list_of_letters)  # reversing list

m_ind = list_of_letters.index('m')  # find the first item whose value is equal to target
print(list_of_letters[m_ind], m_ind)

print("LIST SIZE:", len(list_of_letters))  # list length

squares = [i * i for i in range(10)]
print(squares)

NewList = [[j for j in range(i)] for i in range(10)]
print(NewList)

