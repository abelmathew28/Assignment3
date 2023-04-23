import socket
CARD_VALUES = {1: 'Ace', 2: '2', 3: '3', 4: '4', 5 : '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 13: 'King', 12: 'Queen', 11: 'Jack'}


def client_program():
    #host = socket.gethostname()  # as both code is running on same pc
    host = '127.0.0.1'  # as both code is running on same pc
    port = 5041
     # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = "Hello"

    player_name = client_socket.recv(1024).decode()
    print('Player Card: ', player_name)

    while message.lower().strip() != 'bye':
        # send message
        data = client_socket.recv(1024).decode()  # receive response
        if 'Over' in data:
            print(data)
            break
        elif "Error" not in data:
            print('Server Card: ' + CARD_VALUES[int(data)])  # show in terminal
            print('Please choose a card')
            while True:
                message = input(" -> ")  # again take input
                if message in CARD_VALUES.values():
                    key = list(filter(lambda x: CARD_VALUES[x] == message, CARD_VALUES))[0]
                    message = player_name + "|" + str(key)
                    client_socket.send(message.encode())
                    break
                else:
                    print('Please select a valid card') 
        elif 'Over' in data:
            print(data)
            break
        else:
            print(data)
            message = input(" -> ")  # again take input
            if message in CARD_VALUES.values():
                key = list(filter(lambda x: CARD_VALUES[x] == message, CARD_VALUES))[0]
                message = player_name + "|" + str(key)
                client_socket.send(message.encode())
                continue
            else:
                    print('Please select a valid card') 

    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()
