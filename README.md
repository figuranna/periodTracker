# Period Tracker
The program let's the user log their menstrual circle and its symptoms.

![program_test](https://github.com/figuranna/periodTracker/assets/101461379/d1f4c772-e6b5-44a0-b6e5-3c203af40013)
## About the program
The Python program covers the following point:

- Basic MVC architecture 
- Stores data in a MySQL database
- Uses Enums
- User Interface created with Tkinter 
## The programs structure
### trackerModel
Gets the data from the *periodtracker* database.

**imports**
- *mysql.connector*
  - Makes the connection possible between the program and the database 

**Functions**

- *insertPeriod*
  - Inserts the *date* into the *period* table
- *insertSymptoms*
  - Inserts the datas into the symptoms table
- *selectFiveDates*
  - Selects the latest 5 dates and stores it in a list

### trackerController
Connects the model and the view

**imports**
- *trackerModel*
- _tkinter -> *_
- *datetime*
  - Get's the current date with today() and formats it

**Functions**

- *fillList*
  - Passes the list elements into a new list that is reachable from *trackerView*
- *saveData*
  - *getEntryData*: Gets the input from the entrys and a dropdown menu
  - Saves the user's input into the database

### trackerView
Creates the User Interface using Tkinter

**imports**
- *flowEnum*
- *trackerController*
- _tkinter -> *_

**Functions**

- *popup*
  - In charge of the Log Period window

### flowEnum
Strores the period flow's intensity in an Enum

**Enums**
- LIGHT
- MEDIUM
- HEAVY
## Database
### Tables
**Period table**

![period_database](https://github.com/figuranna/periodTracker/assets/101461379/9e924111-9857-413d-b9b7-7a8da23e3288)

**Symptoms table**

![symptoms_database](https://github.com/figuranna/periodTracker/assets/101461379/3b76d638-73f1-4efd-bc1e-82cffba4dce1)
### Connection
![database_view](https://github.com/figuranna/periodTracker/assets/101461379/ac8f7617-4b9e-477c-8c14-09de32ac78f8)
