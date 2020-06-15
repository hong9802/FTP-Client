import sys
import ftplib
from helper import refector

def check_commands(command, ftp):
    command = command.split()
    try:
        if(command[0] == "ls"):
            ls_command(command, ftp)
        elif(command[0] == "cd"):
            cd_command(command, ftp)
        elif(command[0] == "exit"):
            exit_command()
        elif(command[0] == "get"):
            get_command(command, ftp)
        elif(command[0] == "upload"):
            upload_command(command, ftp)
    except IndexError as e:
        print(e)
    except ftplib.error_perm as e:
        print(e)

def ls_command(command, ftp):
    print(ftp.nlst())

def cd_command(command, ftp):
    print(ftp.cwd(command[len(command)-1]))

def exit_command():
    print("Exit...")
    sys.exit(0)

def get_command(command, ftp):
    filename = refector.get_filename(command[1])
    filepath = refector.get_filepath(command[1])
    fd = open(filename, "wb")
    ftp.retrbinary("RETR " + filepath + filename, fd.write)
    fd.close()

def upload_command(command, ftp):
    up_file = command[1]
    filename = refector.get_filename(up_file)
    path = command[2]
    fd = open(up_file, "rb")
    ftp.storbinary("STOR " + path + "/"+ filename, fd)