import random

def primary():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

# Last quote line number in the .txt
  last = len(quotes) - 1

# Generate a random choice from 0th line to 13th line
  rand = random.randint(0, last)

  print(quotes[rand] + quotes[rand - 3])
  #print(quotes[rand - 2])
if __name__== "__main__":
  primary()
