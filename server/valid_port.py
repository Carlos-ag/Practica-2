def is_valid_port(port):
    try:
        port = int(port)
        return 1 <= port <= 65535
    except ValueError:
        return False