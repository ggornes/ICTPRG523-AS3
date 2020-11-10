import socket
import random

answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it',
           'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Yes Signs point to yes', 'Reply hazy, try again',
           'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
           'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print('')
print('')
print('')


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5678  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    welcome = 'Ask me a question. To finish or exit just type "bye" .'
    conn.send(welcome.encode())
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        if data[-1] != '?':
            response = "Please ask properly"
            conn.send(response.encode())
        else:
            print("from connected user: " + str(data))
            data = answers[random.randint(0, len(answers) - 1)]
            # data = input(' -> ')
            conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
