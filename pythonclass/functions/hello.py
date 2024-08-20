def hello(name):
    print(f"Hello {name}")

#def year_of_birth(name,age):
   # print(f"Hello {name} , you were born in {2024-age}")

#def year_of_birth(name="fanny",age=23):
   # print(f"Hello {name} , you were born in {2024-age}")

def my_country(country = "Uganda"):
    print(f"Hello A kiraChix from {country}")


def greet(*names):
    for name in names:
      print(f"Hello {name}")

def insert_At(arr, index, value):
    arr.insert(index, value)


def datetime(now):
    now=datetime.now()
    return now  
 