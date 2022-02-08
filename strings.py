some_string = 'an_example_of_some_string'
print(some_string[0])
print(some_string[-2])
print(some_string[:2])
print(some_string[5:7])
print(some_string[::-2])

print(len('one string'))

a = 'here you can find text'
print(a.find("text"))

print(a.replace(" ", "-"))

string = "some new text"
strings = string.split()
print(strings)

string = "   some new text   "
newString = string.strip()
print(newString)

student_name = 'Kate'
student_score = 73.916732
print('Hello, %s' % student_name)
print('Hey %s, you have %.2f%% score!' % (student_name, student_score))

print('Hello, {}'.format(student_name))
print(
    'Hey {name}, you got {score:.2f}%!'.format(
        name=student_name, score=student_score
    )
)

student_name = 'Kate'
print(f'Hello, {student_name}!')
a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')

print(f"Hey {student_name}, you got {student_score:.2f}%!")