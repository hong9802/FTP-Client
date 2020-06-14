from ftplib import FTP
from commands import check_commands

if __name__ == "__main__":
    ftp_server = str(input("Insert FTP Server(No Port) : "))
    ftp_port = int(input("Insert FTP Port(default : 21) : "))
    ftp = FTP()
    try:
        ftp.connect(ftp_server, ftp_port)
        user_id = input("Insert User ID : ")
        user_pw = input("Insert User PW : ")
        ftp.login(user_id, user_pw)
    except ConnectionRefusedError as e:
        print("FTP Server or Port Error Please check your FTP or Client")
    while True:
        command = input(">>> ")
        check_commands(command, ftp)
    ftp.close()