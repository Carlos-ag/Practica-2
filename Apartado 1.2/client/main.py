import re
import socket
import threading

from input_ip_port import ask_ip_and_port

print_lock = threading.Lock()

already_printed_server_not_working = False

contador = 0

def send_message(server_address, port, message):
    global contador
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        with print_lock:
            contador += 1
            sock.connect((server_address, port)) 
            print(f" {contador}: Sending message: {message}")
            sock.sendall(message.encode())  
            response = sock.recv(1024).decode()  
            print(f" {contador}: Server response: {response}")
            sock.close()  
            print(f" {contador}: Connection closed\n")        
            
    except:
        if (not already_printed_server_not_working):
            print("Server not working")
            already_printed_server_not_working = True

        

def main():
    global contador
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