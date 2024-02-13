import re

def is_valid_ip(ip):
    # Regular expression to validate an IPv4 address
    if ip == "localhost":
        return True
    regex = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(regex, ip):
        parts = ip.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    return False

def is_valid_port(port):
    try:
        port = int(port)
        return 1 <= port <= 65535
    except ValueError:
        return False

def ask_ip_and_port():
    # For IP address validation
    is_valid = False
    while not is_valid:
        user_ip = input("Please enter an IP address: ")
        is_valid = is_valid_ip(user_ip)
        if is_valid:
            print(f"The IP address {user_ip} is valid.")
        else:
            print("Invalid IP address, please try again.")

    if user_ip != "localhost":
        user_ip = int(user_ip)

    # For port validation
    is_valid = False  # Reset for port validation
    while not is_valid:
        user_port = input("Please enter a port number: ")
        is_valid = is_valid_port(user_port)
        if is_valid:
            print(f"The port number {user_port} is valid.")
        else:
            print("Invalid port number, please try again.")
        
    user_port = int(user_port)
    return user_ip, user_port
