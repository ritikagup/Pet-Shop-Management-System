
**PET SHOP MANAGEMENT SYSTEM**


This project implements a Pet Shop Management System.

The user can perform various operations –

- As a Guest, he can view the pets available.

- As an Admin, along with viewing, he can add and delete a pet. He can also modify the details of the pet.

A user is by default a Guest as soon as he runs the application. For Admin access, he needs to login with the proper credentials.

The user can search for a pet on any of the mentioned fields – Id, Type (eg- dog, cat etc), breed or colour. Pattern matching of the strings are also taken care of. Whereas, while deleting or modifying a pet from the store, the user only needs to mention the Pet ID.


PROJECT DESCRIPTION

**MODULES USED:**

- Mysql is used to maintain the database of the Pets. Hence, module Pymysql is used as an interface between Python and Mysql.

- ` `Tkinter module is used for creating the GUI interface.

- ` `Pillow (PIL) module is used for displaying images.





**DATABASE AND TABLES USED:**

The database used is “mydb” and the table used is “Pet”. The details of the columns of the table “Pet” as given as :


|**S. No**|**Name of the Column**|**Type**|**Description**|
| - | - | - | - |
|1|ID (Primary Key)|Int |Unique identification number|
|2|Type|Varchar(20)|Type of pet (dog, cat etc.)|
|3|Breed|Varchar(20)|Breed |
|4|Colour|Varchar(20)|Colour|
|5|Age|decimal|Age in years|
|6|Height|Decimal|height|
|7|Price|Decimal|Cost of  the pet|
|8|Gender|Varchar(1)|Male (M)/Female(F)|
|9|Avail|Varchar(1)|Availability (Y/N)|




**USER DEFINED FUNCTIONS:**


|**S No.**|**Name**|**Use**|
| :-: | :-: | :-: |
|1|Main|To create a menu window and for calling other functions|
|2|Main\_menu|To display the various menu options in the form of buttons|
|3|Login|To display a login screen for entering the credentials of an admin|
|4|Check\_login|To check for the credentials|
|5|Logout|To logout as Admin|
|6|Add\_pet|To display the screen for adding the details of the pet|
|7|Insert\_rec|To add the details of the pet in the “Pet” table|
|8|Modify\_pet|To display the screen for entering the ID of the pet whose details are to be modified|
|9|Search\_id|To search for the ID of the pet in the table “Pet”|
|10|Modify\_rec|To modify the record in the table “Pet”|
|11|Delete\_pet|To display the screen for entering the Id of the pet which needs to be deleted|
|12|Delete\_rec|To delete the record from the table “pet”|
|13|Search\_pet|To display the screen for entering the search strings of the pet.|
|14|Search\_rec|To search for the records in the table “Pet” according to the search strings|
|15|Display\_recs|To display the records found|
|16|Fr\_destroy|To destroy the previous frames|





fUTURE EXPANSION

- The accessories and pet food can be added in the menu.

- Various inconsistency checks can be added.

- Provision can be added for the user to buy online from the pet shop. For this, the application needs to be integrated with the payment gateway.

- The image of the pet can be added along with other data.
