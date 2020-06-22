import sys
import ftplib
from helper import refector

class commands_dispatcher:
    def ls_command(self, command, ftp):
        print(ftp.nlst())

    def cd_command(self, command, ftp):
        print(ftp.cwd(command[len(command)-1]))

    def exit_command(self, command, ftp):
        print("Exit...")
        sys.exit(0)

    def get_command(self, command, ftp):
        filename = refector.get_filename(command[1])
        filepath = refector.get_filepath(command[1])
        if(filepath == "/"):
            filepath = ftp.pwd() + "/"
        fd = open(filename, "wb")
        ftp.retrbinary("RETR " + filepath + filename, fd.write)
        fd.close()

    def upload_command(self, command, ftp):
        if(len(command) == 2):
            path = ""
        else:
            path = command[2]
        filename = refector.get_filename(command[1])
        fd = open(command[1], "rb")
        ftp.storbinary("STOR " + path + "/" + filename, fd)

    def mkdir_command(self, command, ftp):
        ftp.mkd(command[1])

    def rmdir_command(self, command, ftp):
        ftp.rmd(command[1])

    def rm_command(self, command, ftp):
        ftp.delete(command[1])

    def dispatch(self, command, ftp):
        command = command.split()
        mname = str(command[0]) + "_command"
        if hasattr(self, mname):
            method = getattr(self, mname, ftp)
            method(command, ftp)
        else:
            self.error()