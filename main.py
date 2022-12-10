# write your code here
person= [{'name': 'athba',
'age': '21',
'hobbies': ['reading','sleeping']}]

name=person[0].get('name')
print(name)

age=person[0].get('age')
print(age)

person[0]['age']=22
person[0]['country']='kuwait'

print(person)

print(len(person[0]))

person[0]['hobbies'].append('eating')

def check_hobbies(person):
    if len(person[0]['hobbies'])>=3:
        print(f'wow you are amazing')

check_hobbies(person)
