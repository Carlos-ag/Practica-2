def is_valid_port(port):
    try:
        port = int(port)
        return 1 <= port <= 65535
    except ValueError:
        return False




def ask_valid_port():
    is_valid = False  
    while not is_valid:
        user_port = input("Please enter a port number: ")
        is_valid = is_valid_port(user_port)
        if is_valid:
            print(f"The port number {user_port} is valid.")
            return int(user_port)
        else:
            print("Invalid port number, please try again.")