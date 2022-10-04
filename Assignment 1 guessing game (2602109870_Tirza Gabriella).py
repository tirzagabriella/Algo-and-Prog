
number = random.randint(1, 100)

user_input = 0

while user_input != number:
  user_input = int(input("Masukkan number : "))

  if user_input > number:
    print("too high")
  elif user_input < number:
    print("too low")
  else:
    print("You got it")