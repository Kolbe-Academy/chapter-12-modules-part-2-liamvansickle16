current_room = 1

def help():
	# Help function here
	print("Show some help text")
	print("For example type 'help' to get to this menu")

def room_one(in_list):
	global current_room
	print("Some friendly text here explaning as much as you want about this room")
	print("I have split your commands into a list of words.")
	list_length = len(in_list)
	print("You typed", list_length, "words.")
	if in_list[0] == "examine":
		print("You examine the", in_list[1])
	if "candle" in in_list:
			print("got candle")
			current_room = 2

	
def room_two(in_list):
	# Get creative! New win condition
	print("room two stuff")

def input_loop():
	while True:
		in_list = input("> ").lower().strip().split()
		if in_list[0] == "quit":
			break
		elif in_list[0] == "help":
			help()
		elif current_room == 1:
			room_one(in_list)
		elif current_room == 2:
			room_two(in_list)
		else:
			handle_input(in_list)
		print()



print("Welcome to <insert your game title here>!")
print("<add instructions for how to play here>")
input_loop()


