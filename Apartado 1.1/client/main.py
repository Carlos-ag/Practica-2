import re
import socket
import threading

from input_ip_port import ask_ip_and_port

print_lock = threading.Lock()

already_printed_server_not_working = False

def send_message(server_address, port, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((server_address, port))
            sock.sendall(message.encode())
            response = sock.recv(1024).decode()
            # with print_lock:
            print(f"Server response: {response}")
    except:
        if (not already_printed_server_not_working):
            print("Server not working")
            already_printed_server_not_working = True
        

def main():
    server_ip, server_port = ask_ip_and_port()
    messages = []
    message = ""
    while message != "exit":
        message = input("Enter message (type 'exit' to finish): ")
        messages.append(message)
    
    threads = []
    for message in messages[:-1]: 
        thread = threading.Thread(target=send_message, args=(server_ip, server_port, message))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()


    
if __name__ == '__main__':
    main()