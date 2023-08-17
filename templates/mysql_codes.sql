SHOW DATABASES;
USE mydb;
SHOW TABLES;	# show table list
SELECT * FROM tbl_manager;	# show a specific table
DROP TABLE tbl_manager;	# delete a table
DELETE FROM tbl_manager WHERE mId=1;
create table tbl_manager	# create a table
(
    mId       INT NOT NULL AUTO_INCREMENT,
    mUsername VARCHAR(20),
    mPassword VARCHAR(20),
    mEmail    VARCHAR(25),
    PRIMARY KEY (mId)
);

INSERT INTO tbl_manager(
	mId,
    mUsername,
    mPassword,
    mEmail
) VALUE(
	1,
    123,
    456,
    'ASDF@gmail.com'
);

CREATE TABLE tbl_manager
(
    mId       INT NOT NULL AUTO_INCREMENT,
    mUsername VARCHAR(20),
    mPassword VARCHAR(20),
    mEmail    VARCHAR(25),
    PRIMARY KEY (mId)
);

INSERT INTO tbl_manager(
    mUsername,
    mPassword,
    mEmail
) VALUE(
    123,
    456,
    'ASDF@gmail.com'
);

