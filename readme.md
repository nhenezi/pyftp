#pyftp

## What?
PyFTP is a simple ftp client written on top of [ftplib](http://docs.python.org/2/library/ftplib/).
In short, I got frustrated with ftp and its lack of recursive operations.

## What does work?

* `mkdir directory` creates a new directory.
* `rmdir directory` removes directory.
* `cd directory` changes current working directory to `directory`.
* `rm file` removes file. Add -r flag to recursively remove everything inside directory. Example `rm -r directory` removes everything in `directory`.
* `ls directory` lists all files in directory. *NOTE*: If directory is not specified, current directory is listed.
* `put local remote` copies local file to remote.
* `get remote local` copies remote file to local.
* local mode - Allows execution of commands on local machine inside pyftp. To execute command on local machine enter single space followed by command you want to execute. Example: ` ls -a` lists all files in working directory on local machine.

## TODO

### General features
* auto completion
* command history
* multiple transfer types (currently only binary is used)


### Command specific improvements
* `rm`
    * wildcard (and maybe some other matching). Example: `rm images/*` removes all files in `images` directory.
* `put`
    * recursive operations (`-r` flag) allowing copying of directories. Example: `put -r local_folder remote`.
* `get`
    * recursive download (same as `put -r`)
