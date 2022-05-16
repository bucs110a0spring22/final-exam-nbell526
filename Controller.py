import random
from DogFactAPI import DogFactAPI
from CatFactAPI import CatFactAPI

def userActionFunction():
  x = int(random.randrange(0,2))
  temp = DogFactAPI()
  temp2 = CatFactAPI()
  
  if x == 1:
    print(temp.get())
    
  if x == 0:
    print(temp2.get())