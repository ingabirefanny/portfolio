def add(x,y):
    result = x+y
    return result 
def substract(x,y):
    result = x-y
    return result
def multiply(x,y):
    result = x*y
    return result
def divide(x,y):
    result = x/y
    return result
def remainder(x,y):
    result = x%y
    return result
def power_of(x,y):
    result = x**y
    return result

word= "helloo"
remove_Duplicate = "".join(sorted(set(word)) )
print(remove_Duplicate)  

numbers = [5, 2, 9, 1, 7]
sorted_desc = sorted(numbers, reverse=True)
print(sorted_desc)  # Output: [9, 7, 5, 2, 1]
# positional arguments // converted to a list
def sum(*numbers):
    total=0
    for number in numbers:
        total += number
    return total 

# keyword arguments // converted to a dictionary
def create_sentence(**words):
    print(words)
    sentence=" "
    for word in words.values():
        sentence += word
        sentence += " "
    return sentence 

# Both positional and keyword arguments
# by convetion we use args and kwargs as the paramenter names.

def sum_and_greet(*args,**kwargs):
    total=0
    for x in args:
        total+=x
    f=kwargs["first_name"]
    l=kwargs["last_name"]
    greeting = f"Hello {f} {l} the sum of your numbers is {total}"
    return greeting







     



    

