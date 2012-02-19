#! /usr/bin/python3

import ftplib
import sys
import re
from getpass import getpass

class FTP( ftplib.FTP ):
  user = "a"

if __name__ == "__main__":
  if ( len(sys.argv) > 1):
    FTP.user = sys.argv[1]
  else:
    FTP.user = input( "Username: ")

  if ( len(sys.argv) > 2 ):
    FTP.server  = sys.argv[2]
  else:
    FTP.server = input("Server: ")
  FTP.passwd = getpass("Password: ")

  ftp = FTP( FTP.server )
  ftp.login( FTP.user, FTP.passwd )

  print( ftp.getwelcome() )

  while (1):
    cmd = input("> ")
    if ( cmd == "quit" or cmd == "exit"):
      break;
    elif ( cmd == "ls" ):
      ftp.retrlines('LIST');
    elif ( cmd == "pwd" ):
      print( ftp.pwd() )
    elif ( re.search('mkdir .+', cmd ) ):
      st = cmd.split(' ', 1)
      ftp.mkd( st[1] )
    elif ( re.search('cd .+', cmd) ):
      st = cmd.split(' ', 1)
      ftp.cwd( st[1] )
  if ( ftp.quit() ):
    print( "Connection Closed" )
