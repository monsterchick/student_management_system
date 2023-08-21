# table tbl_manager
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

ALTER TABLE tbl_manager MODIFY COLUMN mUsername VARCHAR(12);    # change VARCHAR(20) to VARCHAR(12)

SELECT * FROM tbl_manager WHERE mId=10;     # search row which's mId=10
SELECT * FROM tbl_manager WHERE mUsername='asdf' AND mPassword=222;     # search row which's mUsername='asdf' and mPassword=222

# table tbl_stu_info
CREATE TABLE tbl_stu_info (
	sId INT NOT NULL AUTO_INCREMENT,
	sName VARCHAR(25),
    sAge INT,
    sMobile VARCHAR(20),
    sCourse VARCHAR(50),
	PRIMARY KEY (sId)
);

SELECT * FROM tbl_stu_info;

ALTER TABLE tbl_stu_info CHANGE sNAME sFirstName VARCHAR(25);
ALTER TABLE tbl_stu_info ADD sLastName VARCHAR(25) AFTER sFirstName;    # add the new column after sFirstName
ALTER TABLE tbl_stu_info CHANGE sCourse sAddress VARCHAR(100);
ALTER TABLE tbl_stu_info MODIFY sId INT;
INSERT INTO tbl_stu_info(
sId,
sFirstName,
sLASTNAME,
sAge,
sMobile,
sAddress
)
VALUES (
0,
'Jimmy',
'Smith',
18,
'+0 1234567890',
'286 Wimborne Rd, Talbot Woods, Bournemouth BH3 7AT, United Kingdom'
);
DELETE FROM tbl_stu_info WHERE sId=0;