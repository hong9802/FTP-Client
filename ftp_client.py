from ftplib import FTP, error_perm
from commands import commands_dispatcher
import socket
import getpass

if __name__ == "__main__":
    password_incorret = False
    commands_dispatcher = commands_dispatcher()
    ftp_server = str(input("Insert FTP Server(No Port) : "))
    ftp_port = int(input("Insert FTP Port(default : 21) : "))
    ftp = FTP()
    try:
        ftp.connect(ftp_server, ftp_port)
        user_id = input("Insert User ID : ")
        user_pw = getpass.getpass("Insert User PW : ")
        ftp.login(user_id, user_pw)
    except ConnectionRefusedError as e:
        print("FTP Server or Port Error Please check your FTP or Client")
        exit(1)
    except socket.gaierror as e:
        print("Wrong Port or Server Please check them...")
        exit(1)
    except error_perm as e:
        if(password_incorret):
            print("Please Check Password")
            exit(1)
        else:
            password_incorret = True
            print("Wrong Password... Please enter again!")
            user_pw = getpass.getpass("Insert User PW : ")
    while True:
        command = input(">>> ")
        commands_dispatcher.dispatch(command, ftp)
    ftp.close()