What to think about
------

- `cat /etc/fstab`
- `cat /etc/rc.local`
- `grep -ir pass /etc/*`
- `netstat -tpln` will show you listenning port/process on tcp (`-t`). Option `-u` (instead of `-t`) for udp
- `ps auxf` will show you all running process and their $PID
- `strace -p$PID` will show every command a process is doing
- `find / -user $USER -group $GROUP 2> /dev/null` will search for files owned by users
- `find / -name ".*"` will search all hidden file. Pipe to xargs pipe grep to search for a specific word
- `cd /etc/cron.d` verify cron job. There is also `/etc/cron.daily`, `/etc/crond.monthly`, etc
- `ls -l /tmp` check everything in the `/tmp` directory
- Maybe some backup are taken on the server, try to find them (maybe `/backup` ?)
- Check emails in `/var/mail`
- Check `.bash_history` file in all of the home user
- `alias` will show bash alias of the current user
- `screen -ls` will show all active screen. Maybe try the same thing with tmux, etc
- `env` will show environment variable
- `sudo -l` will show you your sudo command
