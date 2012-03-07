#! /usr/bin/python

import ftplib
import sys
import re
from getpass import getpass

class directory:
  def getNext( name ):
    if ( re.search( '\/', name ) ):
      path = name.split( '/', 1 )
      path = path[0]
    else:
      path = name
    
    return path[:-1]

class pyftp( ftplib.FTP ):
  def __init__( self,  srv ):
    try:
      ftplib.FTP.__init__(self, srv )
    except Exception as e:
      print e
      sys.exit()

  # logins user
  def auth( self,  user, passwd ):
    try:
      self.login(  user, passwd )
    except Exception:
      print "Bad login"
      sys.exit()
  
  #creates a new directory
  def mkdir( self, name ):
    try:
      print "Creating {0}{1}".format( ftp.pwd(), name ) 
      self.mkd( name )
    except Exception as e:
      print( e )

  #changes directory
  def cd( self, name ):
    try:
      ftp.cwd( name )
    except Exception as e:
      print e 

  def rm( self, name, start_path = '' ):

    name = name.split( '/', 1 )

    #if name starts with /, set start_path to /
    if name[0] == '': 
      start_path = '/'
      #if you try to split /testdir/ you will get
      #name[0] = ''
      #name[1] = testdir/
      # so one more split is required
      name = name[1].split( '/', 1 ) 
    #name doesn't start with /, start_path = current directory
    elif start_path == '':
      start_path = self.pwd()

    #for regex replace * with .*
    name[0] = name[0].replace( '*', '.*' )
    for files in self.getDir( start_path ):
     if files == '.' or files == '..':
       continue
     if  re.match( name[0], files ):
       #for recursion to work this had to be added
       #avoids duplicate // at start
       if( start_path == '/' ):
         start_path = ''
       try:
         self.rm( name[1], start_path + '/' + files )
       except IndexError:
         try:
           self.delete( start_path + '/' + files )
         except Exception as e:
           print ( e )

         

  #removes directory
  def rmdir( self, name ):
    self.rmd( name )

  #lists directory
  def ls( self, name= ''):
    print ( self.retrlines( 'LIST ' + name ) )

  def getDir( self, name ):
    return self.nlst( name )
 
if __name__ == "__main__":
  if ( len(sys.argv) > 1):
    user = sys.argv[1]
  else:
    user = raw_input( "Username: ")

  if ( len(sys.argv) > 2 ):
    srv  = sys.argv[2]
  else:
    srv = raw_input("Server: ")
  passwd = getpass("Password: ")
  print srv
  ftp = pyftp( srv )
  ftp.auth( user, passwd )

  print( ftp.getwelcome() )

  while (1):
    cmd = raw_input( "> ")
    if ( cmd == "quit" or cmd == "exit"):
      break; 

    try:
      param = cmd[1]
    except IndexError:
      param = ""
    cmd = cmd[0]

    getattr ( ftp, cmd )( param )

  try:
    ftp.quit()
  except Exception as e:
    print(e)
