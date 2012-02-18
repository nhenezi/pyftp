#! /usr/bin/python3

from ftplib import FTP
import sys
from getpass import getpass

#read username from stdio
def get_user():
  user = input("Username: ")
  return user

#reads password from stdio
def get_passwd():
  passwd = getpass("Password: ")
  return passwd

#reads server from stdio
def get_server():
  server = input("Server: ")
  return server

if __name__ == "__main__":
  if ( len(sys.argv) > 1):
    user = sys.argv[1]
  else:
    user = get_user();

  if ( len(sys.argv) > 2 ):
    server  = sys.argv[2]
  else:
    server = get_server()
  passwd = get_passwd()

  ftp = FTP( server )
  ftp.login( user, passwd )

  ftp.retrlines('LIST')

  print ( user, passwd, server )


