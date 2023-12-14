test_string = 'Sample string'
test_int = 4
test_list = [1,2,'string1',(1,2,'fe'),{2.2,"hehe"},True,{'yes':5,6:'value2'}]
test_set = {1,5,"fefe","tehu",2,2,5,'fefe'}
test_tuple = (4,2,"fefe",[4,5,7])
test_dict = {1:'apple',2:"ball",3:'cat'}

# Print Hello World
print("helloworld")
print(dir(str))

# print 'My name is Sample string and my age is 4' using string formatting
print('My name is {} and my age is {}'.format(test_string,test_int))

# print 'My name is Sample string and my age is 4' using string formatting
print(f'My name is {test_string} and my age is {test_int}')


# fetch tring  from test_string using slicing
print(test_string[8::])

# fetch ring  from test_string using negative indexing in slicing

print(test_string[-4::])
print(test_string[-1:-5:-1])

# Replace the 'string' word in the test_string with Tushar using string methods and assign back to test_string
test_string = test_string.replace('string','tushar')
print(test_string)

# Split test_string where there is ' ' and create a list of it
r_list=test_string.split()
print(r_list)

# Replace all the occurances of 'string' word in the test_string1 with Tushar
# using string methods and assign back to test_string1
test_string1 = 'Sample string wing string'
test_string1 = test_string1.replace('string','tushar')
print(test_string1)

# Replace 1st occurance of 'string' word in the test_string1 with
# Tushar using string methods and assign back to test_string1
test_string1 = 'Sample string wing string'
test_string1 = test_string1.replace('string','tushar',1)
print(test_string1)

# Concat test_string anf test_string1; put it to test_string1
test_string1 = test_string1 + " " + test_string
print(f"concatinated string is {test_string1}")

# Split test_string where there is '*' and create a list of it and fetch wandkar
str2 = 'Tushar*Wandkar*Prakash*45'
print(str2.split("*")[1])

# Split test_string where there is '*'  stop after wandkar
str2 = 'Tushar*Wandkar*Prakash*45'
print(str2.split("*",2))
print(str2.split("*",2)[:2])

# Convert the test_int to string
print(type(test_int))
print(type(str(test_int)))

# fetch 'fe' from the list test_list using indexing
print(test_list[3][2])

# fetch 5 (value) from the list test_list using indexing
print(test_list[6]['yes'])

# fetch 'value2' from the list test_list using indexing
print(test_list[6][6])

# Change the value of value2 to samplevalue
test_list[6][6]='samplevalue'
print(test_list[6])

# replace 2 in tuple to 7 -- not possible bcoz tuples are immutable

# test_list[3][1] = 7
# print(test_list[3][1])

# replace 5 in test_tuple to 'val1'

test_tuple[3][2]="val1"
print(test_tuple)


# print test_set
print(f'Test set is {test_set}')

# add an element 10 to test_list,test_tuple and test_set
test_list.append(10)
print(test_list)

test_set.add(10)
print(test_set)

# join two lists and put it to 1st list
l1=[1,2,3,4,5]
l2=[6,7,'tej']
l1 = l1+l2
print(f'Joined list is {l1}')
l3=[6,9,10,'tush',7,'tej']
l1.extend(l3)
print(f'Joined list using extend is {l1}')
