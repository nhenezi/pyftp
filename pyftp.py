#! /usr/bin/python3

import ftplib
import sys
import re
from getpass import getpass

class pyftp( ftplib.FTP ):
  def __init__( self,  srv ):
    try:
      super().__init__( srv )
    except Exception:
      print( "Uknown server" )
      sys.exit()


  def auth( self,  user, passwd ):
    try:
      self.login(  user, passwd )
    except Exception:
      print( "Bad login")
      sys.exit()
    

if __name__ == "__main__":
  if ( len(sys.argv) > 1):
    user = sys.argv[1]
  else:
    user = input( "Username: ")

  if ( len(sys.argv) > 2 ):
    srv  = sys.argv[2]
  else:
    srv = input("Server: ")
  passwd = getpass("Password: ")


  ftp = pyftp( srv )
  ftp.auth( user, passwd )
  print( ftp.getwelcome() )

  while (1):
    cmd = input( ftp.pwd()+"$ ")

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
