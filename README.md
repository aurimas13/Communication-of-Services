<p align=center>
  <img height="222px" src="https://github.com/aurimas13/Communication-of-services/blob/main/Public/Photo/communication.jpeg"/>
</p>

<p align="center" > <b> Communication between two services. </b> </p>
<p align=center>
  <a href="https://github.com/aurimas13/Communication-of-services"><img alt="python" src="https://img.shields.io/badge/language-python-blue.svg?style=social&logo=python")></a>
  <a href="https://twitter.com/aurimasnausedas"><img alt="twitter" src="https://img.shields.io/twitter/follow/aurimasnausedas?style=social"/></a>
</p>

------

The program communicates between two events - [Event Consumer](#event-consumer) & [Event Propagator](#event-propagator). The created Event Consumer program is a FLASK API that receives requests from Event Propagator program. 
This repository contains **12** **modules** like [main.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/main.py) that runs the Event Consumer event and [propagate.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/propagate.py)that runs Event Propagator event.
Please refer to [Requirements](#requirements) for importing libraries, packages and additional modules before looking at the [Usage](#usage) of the app or [Functions](#functions), [Tests](#tests) and other fields.

# Table of contents

- [Table of contents](#table-of-contents)
- [Event Consumer](#event-consumer)
- [Event Propagator](#event-propagator)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Environment variables](#environment-variables)
- [Usage](#usage)
- [Functions](#functions)
- [Datasets](#datasets)
- [Tests](#tests)
- [Error](#errors)
- [Docker](#docker)
- [Public](#public)
- [Logo](#photo)
- [License](#license)


# Event Consumer

The [Event Consumer](https://github.com/aurimas13/Communication-of-services/tree/main/EventConsumer) sends a POST request to the terminal while validating the incoming request through [data_validation.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/data_validation.py).
The program also involves [main file](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/main.py) that creates a FLASK API, [output.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/output.py) that opens a json data file,
[config.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/config.py) with [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/.env) that define constant VARIABLES &
[routes.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/routes.py) that sends a request to an API endpoint that is defined as **/event**.

# Event Propagator

The [Event Propagator](https://github.com/aurimas13/Communication-of-services/tree/main/EventPropagator) send events taking JSON files randomly. The function (*send_events()*), imports and other functionalities are written in [propagator.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/propagate.py) module 
while VARIABLES that can be modified are mentioned in [config.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/config.py) that can be changed through the [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/.env) file.

# Requirements

**Python 3.10.5** is required to properly execute package's modules, imported libraries, defined functions and built-ins. Imports of libraries like flask, dotnet, marshmallow, pytest to name a few are needed. 
Some required versions are found under specific requirements.txt files for Consumer Event - [here](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/requirements.txt) and for the Propagator Event - [here](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/requirements.txt) while those that are not mentioned come with the used Python version.
Also inspect [configuration](#configuration) and [environment variables](#environment-variables) before proceeding further. 

For proper usage of the program you might need to run **python3** rather than proposed **python** as shown in the [Usage](#usage).<sup>1</sup>



<br><sup>1</sup>**python** or **python3** depends on the way how you installed python of version 3.* on your machine. </br>

# Configuration

Some VARIABLES can be changed as instructed through the task. Such are WAIT_SECONDS, ENDPOINT, INPUT_FILE_LOCATION of [Propagator Event](#event-propagator) &
PORT, TARGET_FILE_LOCATION of [Consumer Event](#event-consumer). 
WAIT_SECONDS & PORT VARIABLES are configurable as defined through [Environment Variables](#environment-variables) section.

# Environment variables
WAIT_SECONDS & PORT variables (*for the time to randomly send events* and *define the port number*) are configurable through `.env` files found on a specific event folder, respectively.
To change these values please go into a `.env` file and add or change the value, like this:<sup>1</sup>
```
WAIT_SECONDS = '<int value in seconds>'
PORT='<port number like 4444>'
```
<br><sup>1</sup> WAIT_SECONDS are at `.env` file of Event Propagator while PORT is at `.env` file of Event Consumer [authentication](#authentication) section. </br>

# Usage
After the requirements are met, the app package is set at your directory and terminal is run you have four options<sup>1,2,3</sup>:
1) To allow yourself to run **validation** or **check & send** providing the Python file and data file as arguments. You will then be prompted choose either option 1 (validate) or 2 (validate and send): 
```
>>> python bdayreminder.py <data_file_path>
Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails
>>> 1
ERROR: Invalid email for Laura Dreyfuss at row 6 
ERROR: Empty name field is for email TheoGermaine@goal.com at row 7 
ERROR: Invalid date for Anna Higgins at row 11. Date given is 02-30 
ERROR: Date is in the future for Tom Brady at row 12. Date given is 2075-10-22 
ERROR: Invalid email for Ching Yeung Michael Tam at row 19
'''
'''
>>> python bdayreminder.py <data_file_path>
Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails
>>> 2
Kai Yuen Leung will have birthday in a week.
Patrick Kienzle will have birthday in a week.
Emails sent successfully.
```
2) To run **validation** or **check & send** providing the Python file, data file and any number other than 1 or 2 as arguments. You will then be prompted choose either option 1 (validate) or 2 (validate and send), as no other numbers are options: 

```
>>> python bdayreminder.py <data_file_path> 3
Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails
>>> 3
Please choose either 1 or 2
>>> 1
ERROR: Invalid email for Laura Dreyfuss at row 6 
ERROR: Empty name field is for email TheoGermaine@goal.com at row 7 
ERROR: Invalid date for Anna Higgins at row 11. Date given is 02-30 
ERROR: Date is in the future for Tom Brady at row 12. Date given is 2075-10-22 
ERROR: Invalid email for Ching Yeung Michael Tam at row 19 
```

3) You can avoid having the prompt displayed to you altogether. To **validate** birthday persons **data file** for errors set the second argument to be **1**:

```
>>> python bdayreminder.py <data_file_path> 1
ERROR: Invalid email for Laura Dreyfuss at row 6 
ERROR: Empty name field is for email TheoGermaine@goal.com at row 7 
ERROR: Invalid date for Anna Higgins at row 11. Date given is 02-30 
ERROR: Date is in the future for Tom Brady at row 12. Date given is 2075-10-22 
ERROR: Invalid email for Ching Yeung Michael Tam at row 19
``` 
4) To **check** birthday persons **data file** and **send emails** set the second argument to be **2**:

```
>>> python bdayreminder.py <data_file_path> 2
Kai Yuen Leung will have birthday in a week.
Patrick Kienzle will have birthday in a week.
Emails sent successfully.
```
<br><sup>1</sup> **<data_file_path>** should look like this - Datasets/data_20.csv, but in your directory. The full path for me would be /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/Datasets/data_20.csv </br>
<br><sup>2</sup> Main module takes two arguments when run from console. </br>
<br><sup>3</sup> The data used for examples was data_20.csv on 23<sup>th</sup> of June 2022.</br>

# Functions

An overview of functions found inside a module - ***bdayreminder.py***:

- **validate_data_and_send_emails(input_file, send_emails)** checks the validity of an *input_file* and whether a birthday is in a week as well as optionally sends the respective emails (*send_emails*).
- **parse_date(date)** parses the *date*.
- **is_valid_input(date_format, item, index, to_print)** validates inputs (*date_format*,*item*,*index*,*to_print*).
- **send_multiple_emails(birthday_individuals, to_send)** sends emails to recipients of *to_send* list.
- **is_date_in_past(date, date_format)** looks if *date* is in the past.
- **is_valid_email(email)** checks if an email is valid.
- **send_email(name, bday_name, bday_date, days_left, to_email)** sends an email to a recipient (*name*,*to_email*) as a reminder of a birthday (*bday_name*,*bday_date*) in advance (*days_left*).
- **run(read_path, cron_value)** takes the csv data file and runs the script without as choices are passed as arguments (*read_path*,*cron_value*).
- **choose_options(read_path)** asks for input (*read_path*) and chooses option to run.

In depth explanations of the functions can be found inside a module - [bdayreminder.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/bdayreminder.py).

# Datasets

There are three possible datasets to use. These are [data_20](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Datasets/data_20.csv) of 20 recipients, [data_50](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Datasets/data_50.csv) of 50 recipients and [data_80](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Datasets/data_80.csv) of 80 recipients.

# Tests

Test folder to check the functionality of created API event can be found [here](https://github.com/aurimas13/Communication-of-services/tree/main/EventConsumer/Tests). 
An overview of functions found inside a module - [tests.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/Tests/tests.py) are:
- *test_correct_parse_date_ymd()* tests if the correct date is parsed.
- *test_correct_parse_date_md()* tests if the correct date is parsed.
- *test_is_date_in_past_old()* tests if the old date is in the past.
- *test_is_date_in_past_future()* tests if the future date is in the past.
- *test_is_date_in_past_past_month_day()* tests if the old date is in the past.
- *test_is_valid_email_good()* tests if the email address is valid.
- *test_is_valid_email_bad()* tests if the email address is invalid.

By navigating to the program/app folder where it is extracted - [BirthdayReminderApp](https://github.com/aurimas13/BirthdayReminderApp#birthday-reminder-app) - one folder before where [tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py) is held and one can run these test commands:

[//]: # ([comment]: <> &#40;For DocTest run this command in terminal:&#41;)

[//]: # ()
[//]: # ([comment]: <> &#40;``` python&#41;)

[//]: # ()
[//]: # ([comment]: <> &#40;> python -m doctest -v calculator.py&#41;)

[//]: # ()
[//]: # ([comment]: <> &#40;```&#41;)
1) To check source files for errors in the project folder:
```
>>> pyflakes .
```

2) To check source files for errors in test file: 
```
>>> pyflakes Tests/tests.py
```

3) To check typing for test file:
``` 
>>> python -m pytest Tests/tests.py
```
# Errors

There could arise a few errors like:

1) 1st argument error if the provided 1st argument is of different format to the csv format:
```
>>> python bdayreminder.py Datasets/data_20.json 1      
Traceback (most recent call last):
  File "/Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/bdayreminder.py", line 237, in <module>
    run(arg_path, cron_input)
  File "/Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/bdayreminder.py", line 215, in run
    raise Exception('ERROR: Wrong data format file')
Exception: ERROR: Wrong data format file
```
2) 1st argument error if the provided 1st argument of data file doesn't exist:
```
>>> python bdayreminder.py Datasets/data_13.csv 1 
Traceback (most recent call last):
  File "/Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/bdayreminder.py", line 237, in <module>
    run(arg_path, cron_input)
  File "/Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/bdayreminder.py", line 199, in run
    raise Exception('ERROR: File doesn\'t exist')
Exception: ERROR: File doesn't exist
```
3) 2nd argument error if the provided 2nd argument is a string:
```
>>>  python bdayreminder.py Datasets/data_20.csv versada
Argument passed not an integer
```

There are more yet these would be the most common.

# Docker

To build cron job in mac terminal run:
``` 
>>> crontab -e
```

The syntax for cronjob when entering terminal could look like this:<sup>1,2,3</sup>
``` 
>>> 0 6 * * * cd <directory_to_app> && <directory_to_python> bdayreminder.py <data_file_path> 2
[Optional] >>> 0 6 * * * cd <directory_to_app> && <directory_to_python> bdayreminder.py <data_file_path> 2 >> Public/birthdays.txt
```
<br><sup>1</sup> **<directory_to_app>** - should be the directory where BirthdayReminderApp folder is like /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp </br>
<br><sup>2</sup> **<directory_to_python>** should be where you installed python on your machine like /Users/aurimasnausedas/opt/miniconda3/envs/symmetric/bin/python </br>
<br><sup>3</sup> **<data_file_path>** should be the dataset in the directory of app like in /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp by setting it to Datasets/data_20.csv </br>

Syntax customization for Cron Job can be checked [here](https://crontab.guru/).

# Public

Public folder contains three files: 
- [task](https://github.com/aurimas13/Communication-of-services/blob/main/Public/Task.md) - the problem or task overview.
- [todolist](https://github.com/aurimas13/Communication-of-services/blob/main/Public/todolist.txt) - the TO DO List.
- [photo](https://github.com/aurimas13/Communication-of-services/blob/main/Public/Photo) - the Photo folder.

[//]: # (- [task.pdf]&#40;https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/task.pdf&#41; - the problem for which this program was implemented.)

# Logo

The logo of the communication between two services can be found [here](https://github.com/aurimas13/Communication-of-services/blob/main/Public/Photo/communication.jpeg).

# License

The MIT [LICENSE](https://github.com/aurimas13/Communication-of-services/blob/main/LICENSE)



---------------
Apkeisti Propagator'yje config.py ENDPOINT jei docker arba locally

Need two dockerfiles

docker build -t services .  
docker run -p 4444:4444 services

Enter directories of api: docker exec -it api_service bash
docker exec -it api_service bash (FLASK stuff)

FLASK api:
docker build -t api .  
docker run --name api_service --network some_network -p 4444:4444 api 

Propagator:
docker build -t propagator .   
docker run -p 6444:6444 --name propagator_name --network some_network propagator

Paleisti Flask galima per python main.py nuejus i ta flasko direktorija
arba per
konsoleje pradzioje rasai export FLASK_APP=main.py kai esi toje direktorijoje
ir po to paleidi flask run
Kai changinti direktorija folderi palikti ta pati bet keisti json ar kita failo formata kaip events.json



# *The Task to Solve by Wednesday (07/27)*
 
### Task overview

Create two services that communicate with each other. One that periodically sends out predefined event payloads and another one that consumes them.  
  
The code for the task must be written in Python.  

### The first service (Event propagator)

Description: The service should periodically (every N seconds) send a predefined JSON object to a specific HTTP API endpoint.

Requirements for the first service:

1. DONE The period of time should be measured in seconds.

2. DONE The period of time between sent JSON objects(events) should be configurable via a configuration file or startup arguments. config.py -> WAIT_SECONDS | configuration file taking environment variables
    
3. DONE The HTTP API endpoint that the payloads are sent to should be configurable via a configuration file or startup arguments.
    
4. DONE The predefined JSON objects(events) that can be sent should be read from a file. INPUT_FILE_LOCATION
    
5. DONE The location of the JSON objects(events) file should be configurable via a configuration file or startup arguments. config.py -> INPUT_FILE_LOCATION
    
6. DONE The algorithm for choosing a specific JSON object(event) to send at each period from all the objects read from file, should be random.
        
The array of JSON objects(events) that can be sent individually:  


    [
	    {
		    "event_type":"message",
		    "event_payload":"hello"
	    },
	    {
		    "event_type":"user_joined",
		    "event_payload":"Peter"
	    },
	    {
		    "event_type":"message",
		    "event_payload":"greetings"
	    },
	    {
		    "event_type":"message",
		    "event_payload":"no, thanks"
	    },
	    {
		    "event_type":"user_joined",
		    "event_payload":"Jack"
		},
	    {
		    "event_type":"message",
		    "event_payload":"yes, please"
	    },
	    {
		    "event_type":"user_joined",
		    "event_payload":"Thomas"
	    },
	    {
		    "event_type":"message",
		    "event_payload":"okay"
	    },
	    {
		    "event_type":"message",
		    "event_payload":"welcome"
	    },
	    {
		    "event_type":"user_left",
		    "event_payload":"Thomas"
	    },
	    {
		    "event_type":123,
		    "event_payload":{}
	    }
    ]

  

### The second service (Event consumer)

Description: The service should expose a HTTP API endpoint that accepts incoming JSON payloads and persists them to a file.

Requirements for the first service:

7. DONE The service should expose a HTTP API endpoint that accepts incoming POST requests on the path `/event`
    
8. DONE The port for running HTTP API should be configurable via a configuration file or startup arguments. config.py -> SERVER_NAME 
    
9. DONE The location of the file for the incoming payloads should be configurable via a configuration file or startup arguments. config.py -> TARGET_FILE_LOCATION 
    
10. DONE The service should only accept payloads matching this JSON template:

    [
        {
            "event_type": string,
            "event_payload": string
        }
    ]

Upon task completion:

- Write an instruction on how to run the project (preferably a Makefile with a predefined launch command)
    
- Zip the whole project and its files and send it to both darius.baltakys@cybercare.cc and tomas.vilcinskas@cybercare.cc

