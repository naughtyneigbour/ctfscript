Forensics in a filesystem
=====

Look for deleted inode
--------
With debugfs, you can explore the filesystem. The call below will give you an interactive shell on the filesystem.

```
$ debugfs /path/to/filesystem
debugfs 1.42.8 (20-Jun-2013)
debugfs:
```

Using `lsdel`, you can view deleted inode.

```
debugfs:  lsdel
 Inode  Owner  Mode    Size      Blocks   Time deleted
    19      0 100644  12288     12/    12 Tue Feb  4 21:03:11 2014
    12      0 100777     16      1/     1 Tue Feb  4 21:04:51 2014
```

Using the `dump` command over these file will reveal their content.

```
debugfs:  dump <19> /ringzer0/forensic/file1
debugfs:  dump <12> /ringzer0/forensic/file2
```

