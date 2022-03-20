# VerdantPages - Contact list written in python ( WIP ).

## Need to make some functions for connecting and creating the db ( if not exists ).  Will have to do manually for now ( will be fixed shortly ).

## Setup
$ cd db/ && sqlite3 contactsDb

CREATE TABLE contacts(name varchar(80), email varchar(120), phoneNum int(16));

#### Test if works
INSERT INTO contacts VALUES("TestName", "Email@Email.com", 12345678910);
SELECT * FROM contacts;

then interrupt and run program normally.
