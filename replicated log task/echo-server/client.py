import socket

def echo_client(host='echo_server', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        message = "Hello from Docker!"
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f'Received echo: {data.decode()}')

if __name__ == "__main__":
    echo_client()