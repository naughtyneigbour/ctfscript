SQL-TRUNCATION
====

SQL truncation happen when a database field with a fixed length is given a larger than acceptable string. For example, a `username` varchar(10) field will truncate to 10 character any input it receives. Sometimes, the validation mechanism does not check for this. This technique is mostly used in registration form when you know that there is an admin user.

Vulnerability
-----
This mostly affect older database. In the case of mysql, the newest version has all the security measure to disaallow such thing, see `STRICT_TRANS_TABLES` and `STRICT_ALL_TABLES`.

Practical example
------

Let's say we have two field in a database : `username` varchar(10) and `password` varchar(10) and a registration form as follow :

```
REGISTRATION

USERNAME : _______
PASSWORD : _______
```

Giving the username input the string `admin     pwned` and the password input the string `password`, we would effectively insert `admin` into the username field.
