def hello(name):
        print(f"Hello {name}")

def year_of_birth(name,age
                  ):
        print(f"Hello {name}, you were born in {2024-age}")

# default key values,
def my_country(country = "Uganda"):
        print(f"Hello Akirachix from {country}")


 #creating a function that accepts more than one or any number of  argument.

def greet(*names):
 for name in names:
        print(f"Hello {name}")



#Creating a function that accepts more than one argument.
def create_sentence(**words):
      print(words)
      sentence = ""
      for word in words.values():
            sentence+=word
            sentence += " "
      return sentence



# def func_name(*args, **kwergs):

def student_score(**scores):
      sum = 0
      for score in scores.values:
            sum += score
            average_score = sum/len(scores.values)
            print (average_score)
            

