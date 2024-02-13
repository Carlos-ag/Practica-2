import socket
import threading
from valid_port import is_valid_port

ip = "localhost"
lock = threading.Lock()

def handle_client_connection(client_socket):
    with client_socket:
        with lock:
            data = client_socket.recv(1024)
            data_decoded = data.decode()
            print(f"\nReceived:")
            for m in data_decoded.split(" "):
                print(m, sep="")
            client_socket.sendall(data)

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()
    print(f"Listening on port {port}...")
    while True:
        client_sock, address = server.accept()
        print(f"Accepted connection from {address}")
        client_handler = threading.Thread(
            target=handle_client_connection,
            args=(client_sock,)
        )
        client_handler.start()

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

def main():
    port = ask_valid_port()
    start_server(port)

if __name__ == "__main__":
    main()
