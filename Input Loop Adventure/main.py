def handle_input(in_list):
  print("I have split your commands into a list of words.")
  list_length = len(in_list)
  print("You typed", list_length, "words.")
  print("The first word was:", in_list[0])
  if list_length > 1:
    print("The second word was:", in_list[1])

def input_loop():
  while True:
    in_list = input("> ").lower().strip().split()
    if in_list[0] == "quit":
      break
    else:
      handle_input(in_list)
    print()


print("Welcome to <insert your game title here>!")
print("<add instructions for how to play here>")
input_loop()
