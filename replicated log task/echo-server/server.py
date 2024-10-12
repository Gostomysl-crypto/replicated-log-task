import socket

def start_echo_server(host='0.0.0.0', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Server started at {host}:{port}')  # Перевірка, чи сервер запущено
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received message: {data.decode()}")
                conn.sendall(data)

if __name__ == "__main__":
    start_echo_server()
