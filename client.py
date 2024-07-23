import socket

HOST = '127.0.0.1'
PORT = 65433


def start_client():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("Подключено к серверу.")

        while True:
            message = input("Введите сообщение для сервера: ")
            client_socket.sendall(message.encode('utf-8'))
            if message == "exit":
                break

            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Получено от сервера: {data}")

        client_socket.close()
        print("Соединение с сервером закрыто.")

if __name__ == '__main__':
    start_client()
