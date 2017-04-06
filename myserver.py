#! /usr/bin/python3

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)



firstPetition = True


try:
    while True:
        print('Waiting for connections...')
        (recvSocket, address) = mySocket.accept()
        petition = recvSocket.recv(2048).decode('utf-8')
        print(petition)
        try:
            recvOperand = int(petition.split()[1][1:])
        except ValueError:
            respuesta = "<html><h1> Introduce un operando, bro</h1></html>"
            recvSocket.send(bytes("HTTP/1.1 200 OK \r\n\r\n" + respuesta, 'utf-8'))
            recvSocket.close()
            continue
        if firstPetition:
            firstOperand = recvOperand
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
            "<html><h1>He recibido un " + str(firstOperand) +
            ".\r\nDame mas de esos numeros que tu me das <3</h1></html>", 'utf-8'))
        else:
            result = firstOperand + recvOperand
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
            "<html><h2>Muchas gracias. \r\n" +
            str(firstOperand) + " + " + str(recvOperand) +
            " = " + str(result) +"</h2></html>", 'utf-8'))

        recvSocket.close()
        firstPetition = not firstPetition

except KeyboardInterrupt:
    print('Closing binded socket')
mySocket.close()
