import socket

def server():
    # Obtener el hostname
    host = socket.gethostname()

    # Especificar el puerto para escuchar
    port = 21042  # TO DO: Puedes cambiar el puerto si lo deseas

    # Crear un objeto socket
    s = socket.socket()

    # Bindear el socket al host y al puerto
    s.bind((host, port))

    # Escuchar conexiones ingresantes
    s.listen(1)  # TO DO: Puedes especificar el número de conexiones máximas en cola

    print(f"Servidor escuchando en {host}:{port}")

    # Aceptar conexiones entrantes
    c, address = s.accept()
    print(f"Connected to: {address}")

    newMsg = True
    while newMsg:
        # Recibir datos del cliente (hasta 1024 bytes)
        data = c.recv(1024).decode()

        # setear en newMsg si hay data nueva (si no, rompe el ciclo)
        if data:
            print(f"Recibido de cliente: {data}")

            # Obtener el input de usuario y enviar al cliente (usar response.encode())
            response = input("Enter response to send to client: ")
            c.send(response.encode())  # TO DO
        else:
            newMsg = False

    # Cerrar la conexión con el cliente
    c.close()  # TO DO

if __name__ == "__main__":
    # Start the server
    server()
