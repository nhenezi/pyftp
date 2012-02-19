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

  try:
    ftp = FTP( FTP.server )
  except Exception:
    print("Unknown server" )
    sys.exit()

  try:
    ftp.login( FTP.user, FTP.passwd )
  except Exception:
    print("Bad login" )
    sys.exit()

  try:
    print( ftp.getwelcome() )
  except Exception as e:
    print( e )
    sys.exit()
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
      try:
        print( "Creating {}{}".format( ftp.pwd(), st[1]) )
        ftp.mkd( st[1] )
      except Exception as e:
        print ( e )

    elif ( re.search('cd .+', cmd) ):
      st = cmd.split(' ', 1)
      try:
        print( "Changing to {}".format( st[1] ) )
        ftp.cwd( st[1] )
      except Exception as e:
        print( e )
    elif ( re.search('rm .+', cmd) ):
      st = cmd.split(' ', 1)
      if ( re.search('\*', st[1] ) ):
        print("resursive")
      else:
        try:
          ftp.delete( st[1] )
        except Exception as e:
          print ( e )
  try:
    ftp.quit()
  except Exception as e:
    print(e)
