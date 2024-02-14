import socket
import threading
from valid_port import ask_valid_port
import time
import os

ip = "localhost"
lock = threading.Lock()
# should_continue = True 
# has_analyzed_message = True

def kill_server():
    # time.sleep(0)
    print("Server shutting down...")
    os._exit(0)


def handle_client_connection(client_socket):
    with client_socket:
        data = client_socket.recv(1024)
        data_decoded = data.decode()
        # if data_decoded == "exit":
        #     print("Server shutting down...")
        #     should_continue = False 
        #     has_analyzed_message = True
        # else:
                
        if data_decoded != "exit":
            has_analyzed_message = True
            print(f"\nReceived:")
            with lock:
                for m in data_decoded.split(" "):
                    print(m, end=" \n\n")
            client_socket.sendall(data)
        else:
            kill_server_thread = threading.Thread(target=kill_server)
            kill_server_thread.start()

def start_server(port):
    global should_continue
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()
    server.settimeout(1)  # Set a timeout of 1 second
    print(f"Listening on port {port}...")
    while True:
        try:
            client_sock, address = server.accept()
            print(f"Accepted connection from {address}")
            client_handler = threading.Thread(
                target=handle_client_connection,
                args=(client_sock,)
            )
            client_handler.start()
        except socket.timeout:
            continue  # Continue checking the flag if accept times out
        except KeyboardInterrupt:
            break  # Allow server to be stopped with Ctrl+C


def main():
    # port = ask_valid_port()
    port = 6968
    start_server(port)

if __name__ == "__main__":
    main()
