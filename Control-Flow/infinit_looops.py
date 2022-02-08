command = ""
while True:
    command = input(">")
    print("Echo", command)
    if command.lower() == "quit":
        break

