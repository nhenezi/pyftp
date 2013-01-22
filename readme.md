#pyftp

## What?
PyFTP is a simple ftp client written on top of [ftplib](http://docs.python.org/2/library/ftplib/).
In short, I got frustrated with ftp and its lack of recursive operations.

## What does work?

`mkdir directory` creates a new directory.
`rmdir directory` removes directory.
`cd directory` changes current working directory to `directory`.
`rm file` removes file. Add -r flag to recursively remove everything inside directory. Example `rm -r directory` removes everything in `directory`.
`ls directory` lists all files in directory. *NOTE*: If directory is not specified, current directory is listed.
`put local remote` copies local file to remote.
`get remote local` copies remote file to local.

## TODO

### General features
* auto completion
* local mode - Allow execution of commands on local machine inside pyftp. Suggestion: Use one space ` ` as prefix for local mode. Example ` pwd` will print working directory on local machine
* command history
* multiple transfer types (currently only binary is used)


### Command specific improvements
* `rm`
** wildcard (and maybe some other matching). Example: `rm images/*` removes all files in `images` directory.
* `put`
** recursive operations (`-r` flag) allowing copying of directories. Example: `put -r local_folder remote`.
* `get`
** recursive download (same as `put -r`)
