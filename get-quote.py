import random
def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close() 

  #last = 13
  last = len(quotes) - 1
  #for i in range(0,last) 
  #rnd = random.randint(0, last)
  print (quotes[random.randint(0, last)])
  print (quotes[random.randint(1, last)])
    #print (quotes[rnd]) 

if __name__== "__main__":
  main()