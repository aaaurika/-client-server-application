import socket
import threading

HOST = '127.0.0.1'
PORT = 65433

def handle_client(client_socket):

    print("Новый клиент подключен.")
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Получено от клиента: {data}")
            message = input("Введите сообщение для клиента: ")
            client_socket.sendall(message.encode('utf-8'))
        except ConnectionResetError:
            print("Клиент отключился.")
            break

    client_socket.close()
    print("Соединение с клиентом закрыто.")

def start_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Сервер запущен на {HOST}:{PORT}")

        while True:
            client_socket, address = server_socket.accept()
            print(f"Новый клиент подключен: {address}")

            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()

if __name__ == '__main__':
    start_server()

