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
This repository contains **modules** like [main.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/main.py) that runs the Event Consumer event and [propagate.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/propagate.py)that runs Event Propagator event.
Please refer to [Requirements](#requirements) for importing libraries, packages and additional modules before looking at the [Usage](#usage) of the app or [Functions](#functions), [Tests](#tests) and other fields.

# Table of contents

- [Table of contents](#table-of-contents)
- [Event Consumer](#event-consumer)
- [Event Propagator](#event-propagator)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Environment variables](#environment-variables)
- [Usage](#usage)
- [Docker](#docker)
- [Functions](#functions)
- [Datasets](#datasets)
- [Tests](#tests)
- [Error](#errors)
- [Public](#public)
- [Logo](#photo)
- [License](#license)


# Event Consumer

The [Event Consumer](https://github.com/aurimas13/Communication-of-services/tree/main/EventConsumer) is an API application that has one endpoint **'/event'** POST method to receive events and then process eventss while validating the incoming request through [data_validation.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/data_validation.py).
The program also involves [main file](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/main.py) that creates a FLASK API, [output.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/output.py) that opens a json data file,
[config.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/config.py) with [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/.env) that define constant VARIABLES &
[routes.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/routes.py) contains the endpoint of the application.

# Event Propagator

The [Event Propagator](https://github.com/aurimas13/Communication-of-services/tree/main/EventPropagator) send events to the Consumer API using the **/events** endpoint. It randomly takes one if the events from a given JSON file. The function (*send_events()*), imports and other functionalities are written in [propagator.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/propagate.py) module 
while VARIABLES that can be modified are mentioned in [config.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/config.py) that can be changed through the [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/.env) file.

# Requirements

Python 3.10.5 is required to properly execute package's modules, imported libraries, defined functions and built-ins. To install the necessary libraries for Event Consumer API  and Event Propagator run their respective requirements.txt file like this:
To install the necessary libraries for Event Consumer API  and Event Propagator run their respective requirements.txt file like this:
`pip install -r requirements.txt`
Also inspect [Configuration](#configuration) and [Environment variables](#environment-variable) before proceeding further.

**Python 3.10.5** is required to properly execute package's modules, imported libraries, defined functions and built-ins. Imports of libraries like flask, dotnet, marshmallow, pytest to name a few are needed. 
Some required versions are found under specific requirements.txt files for Consumer Event - [here](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/requirements.txt) and for the Propagator Event - [here](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/requirements.txt) while those that are not mentioned come with the used Python version.

For proper usage of the program you might need to run **python3** rather than proposed **python** as shown in the [Usage](#usage).<sup>1</sup>



<br><sup>1</sup>**python** or **python3** depends on the way how you installed python of version 3.* on your machine. </br>

# Configuration

Some VARIABLES can be changed as instructed through the task. For [Event Propagator]((#event-propagator)):
```
WAIT_SECONDS
ENDPOINT
INPUT_FILE_LOCATION
```
and for [Event Consumer API]((#event-consumer)):
```
PORT
TARGET_FILE_LOCATION
```
All these VARIABLES are configurable as defined through [Environment Variables](#environment-variables) section.

To run locally you will need to configure the **ENDPOINT** in your Event Consumer's [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/.env).
The `.env` variable **ENDPOINT** will use the localhost `127.0.0.1` to be run locally, and for running with Docker 
it will need to be substituted with the defined service name:
1) For example, for running without Docker in your Event Consumer's `.env` file fill in:
```
ENDPOINT='http://127.0.0.1:4444/event'
```
2) And the example for running with Docker where the API is given the name *api_service*:
```
ENDPOINT='http://api_service:4444/event
```
**PORT** can be changed at Event Consumer's [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/.env) file and 
updated at Event Propagator's [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/.env) under **ENTRYPOINT** variable with the same **PORT** as in Event's Consumer `.env` file.

**INPUT_FILE_LOCATION** can be changed at Event Propagator's [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/.env) while
**TARGET_FILE_LOCATION** at Event Consumer's [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/.env) file.

**To run events through Docker refer [here](#docker).**

# Environment variables

WAIT_SECONDS, ENDPOINT, INPUT_FILE_LOCATION, PORT & TARGET_FILE_LOCATION variables 
(*set the time to randomly send events*, *define the endpoint*, *define the input data file*, *define the port number* & *write the output file*) 
are configurable through `.env` files by adding or changing the value found on a specific event folder, like this:<sup>1,2,3,4,5</sup>
```
WAIT_SECONDS = '<int value in seconds>'
ENDPOINT = '<server:PORT/endpoint>'
INPUT_FILE_LOCATION = 
PORT='<port number like 4444>'
TARGET_FILE_LOCATION = 
```
<br><sup>1</sup> WAIT_SECONDS is at `.env` file of Event Propagator as described in [Configuration](#configuration) section. </br>
<br><sup>2</sup> ENDPOINT is at `.env` file of Event Propagator as described in [Configuration](#configuration) section. </br>
<br><sup>3</sup> INPUT_FILE_LOCATION is at `.env` file of Event Propagator as described in [Configuration](#configuration) section. </br>
<br><sup>4</sup> PORT is at `.env` file of Event Consumer as described in [Configuration](#configuration) section. </br>
<br><sup>5</sup> TARGET_FILE_LOCATION is at `.env` file of Event Consumer as described in [Configuration](#configuration) section. </br>

# Usage

After the requirements are met, the package is set at your directory and two terminal windows are run you are ready to make the communication between two services:
- For the 1<sup>st</sup> terminal window to run an Event Consumer (FLASK API) you will need to provide the python file with no arguments:<sup>1</sup> 
```
>>> python main.py
 * Serving Flask app 'main' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://192.168.0.156:4444/ (Press CTRL+C to quit)
```
- For the 2<sup>nd</sup> terminal window to run Event Propagator and send a request to the Event Consumer API
you need to provide the python file with no arguments, and it should look like this:<sup>2</sup>
```
>>>  python propagate.py
{"event_payload":"welcome","event_type":"message"}

{"event_payload":"Thomas","event_type":"user_left"}

{"event_payload":"greetings","event_type":"message"}

{"error": "Validation error - {'event_payload': ['Not a valid string.'], 'event_type': ['Not a valid string.']}"}
{"event_payload":"no, thanks","event_type":"message"}

{"event_payload":"Thomas","event_type":"user_left"}
```

When Event Consumer and Event Propagator are run on two terminals, the output of Event Consumer on terminal will look like this<sup>3</sup>:

```
127.0.0.1 - - [25/Jul/2022 16:16:37] "POST /event HTTP/1.1" 200 -
127.0.0.1 - - [25/Jul/2022 16:16:42] "POST /event HTTP/1.1" 200 -
127.0.0.1 - - [25/Jul/2022 16:16:47] "POST /event HTTP/1.1" 200 -
ERROR:root:Bad request was sent with {'event_type': ['Not a valid string.'], 'event_payload': ['Not a valid string.']}
127.0.0.1 - - [25/Jul/2022 16:16:52] "POST /event HTTP/1.1" 400 -
INFO:werkzeug:127.0.0.1 - - [25/Jul/2022 16:16:52] "POST /event HTTP/1.1" 400 -
127.0.0.1 - - [25/Jul/2022 16:16:57] "POST /event HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [26/Jul/2022 11:21:47] "POST /event HTTP/1.1" 200 -
127.0.0.1 - - [26/Jul/2022 11:21:52] "POST /event HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [26/Jul/2022 11:21:52] "POST /event HTTP/1.1" 200 -
```

To cancel either of the services when both are running locally and you are happy press `CTRL+C`.

<br><sup>1</sup> The output of running Event Consumer API may differ like on what server you are running</br>
<br><sup>2</sup> The output of Event Propagator can differ from example above as it takes events randomly. </br>
<br><sup>3</sup> The output of Event Consumer can differ from example above as it might print output in different sequence.</br>

# Docker

Setup up of dockerfiles can be found [here](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/Dockerfile) for Consumer Event and 
[here](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/Dockerfile) for Propagator Event.

Before running events on Docker, you will need to make a bit of changes in `.env` file:
- Refer to [Configuration](#configuration) for instructions to change **ENDPOINT** (particularly)
and other fields on `.env` files if you don't want to use default VARIABLES on which the below Docker commands are written for running Docker.

After the **ENDPOINT** is set, the rest VARIABLES are default, the package is set at your directory and two Docker terminal windows are run, follow this<sup>1</sup>:
1) To build docker image on the 1<sup>st</sup> terminal window for the Event Consumer you need to go to the EventConsumer folder locally and run:
``` python
>>> docker build -t eventconsumer .  
```
2)  Followed by a Docker run on the same window:
``` python
> docker run --name api_service --network some_network -p 4444:4444 eventconsumer 
```
3) Then you will have to build docker image on the 2<sup>nd</sup> terminal window for Event Propagator by going to EventPropagator folder locally and running:
``` python
> docker build -t eventpropagator .  
```
4) Followed by a Docker run on the 2<sup>nd</sup> window:
``` python
> docker run -p 3333:3333 --name propagator --network some_network eventpropagator
```
5) If you wish to see logs on how requests are sent, open the 3<sup>rd</sup> terminal window and in it run this:
``` python
docker logs api_service --follow
```
6) If you wish to check whether there are output when running through Docker as for when running locally open the 4<sup>th</sup> terminal window and enter directories of API:
``` python
> docker exec -it api_service bash
```
7) Then go to output folder and run:
``` python
> cat events.json
```

If you wish to see what you should see on either terminal window through Docker go to [Usage](#usage)  as it should be the same as shown locally there.

To cancel either of the services when both are running on Docker and you are happy press `CTRL+C`.

<br><sup>1</sup> Be sure to have opened two different terminal windows for communication  between services</br>

# Functions

Overview of functions found inside modules - ***main.py***, ***routes.py***, ***output.py*** & ***propagate.py***:

- **create_app()** creates a FLASK API.
- **event_endpoint():** takes a request and returns json event.
- **persist_output(json_string, target_path)** takes a request as **json_string** and writes it to **target_path** file.
- **send_events()** opens a data from an input file, reads data from it, randomly converts it to JSON data and sends a POST request.

In depth explanations of the functions can be found inside modules.

# Datasets

The dataset to use is [events.json](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/events.json) 
as extracted from the [task](https://github.com/aurimas13/Communication-of-services/blob/main/Public/Task.md) file that contains 11 JSON values.

# Tests

Test folder to check the functionality of a created Event Consumer API can be found [here](https://github.com/aurimas13/Communication-of-services/tree/main/EventConsumer/Tests). 
An overview of functions found inside a module, [tests.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/Tests/tests.py),
of Event Consumer API are:<sup>1</sup>
- *test_correct_request_code(client)* tests if the correct request code is returned.
- *test_correct_request_output(client)* tests if the correct request output is returned.
- *test_incorrect_response_code(client)* tests if the incorrect request code is returned for `event_payload`.
- *test_incorrect_response_code_two(client)* tests if the incorrect request code is returned for `event_type`.
- *test_incorrect_response_for_event_payload(client)* tests if the incorrect request output is returned for `event_payload`.
- *test_incorrect_response_for_event_type(client)* tests if the incorrect request output is returned for `event_type`.

By first navigating to the program's folder - [Communication-of_services](https://github.com/aurimas13/Communication-of-services) - where it is extracted, 
one can check the source files for errors:
```
>>> pyflakes .
```

Then by going to [Event Consumer's API](https://github.com/aurimas13/Communication-of-services/tree/main/EventConsumer) folder, 
one can run these test commands:
1) To check the source files for errors in test file: 
```
>>> pyflakes Tests/tests.py
```

2) To check typing for test file:
``` 
>>> python -m pytest tests/tests.py
```

<br><sup>1</sup> **Event Propagator** does not have tests as everything defined there is built-in used by [**propagator.py**](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/propagate.py) </br>

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

