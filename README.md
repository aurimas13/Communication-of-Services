<p align=center>
  <img height="222px" src="https://github.com/aurimas13/Communication-of-services/blob/main/Public/communication.jpeg"/>
</p>

<p align="center" > <b> Communication between two services. </b> </p>
<p align=center>
  <a href="https://github.com/aurimas13/Communication-of-services"><img alt="python" src="https://img.shields.io/badge/language-python-blue.svg?style=social&logo=python")></a>
  <a href="https://twitter.com/aurimasnausedas"><img alt="twitter" src="https://img.shields.io/twitter/follow/aurimasnausedas?style=social"/></a>
</p>

------

The program communicates between two events - [Event Consumer](#event-consumer) & [Event Propagator](#event-propagator). The created Event Consumer program is a FLASK API that receives requests from Event Propagator program. 
This repository contains **2** **modules** where [bdayreminder.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/bdayreminder.py) involves these functionalities while [tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py) tests the package. Please refer to [Requirements](#requirements) for importing libraries, packages and addtional modules before looking at the [Usage](#usage) of the app or [Functions](#functions), [Tests](#tests), [Cron Job](#cron-job) and other fields.

# Table of contents

- [Table of contents](#table-of-contents)
- [Event Consumer](#event-consumer)
- [Event Propagator](#event-propagator)
- [Requirements](#requirements)
- [Environment variables](#environment-variables)
- [Authentication](#authentication)
- [Usage](#usage)
- [Functions](#functions)
- [Datasets](#datasets)
- [Tests](#tests)
- [Error](#errors)
- [Cron Job](#cron-job)
- [Public](#public)
- [Logo](#photo)
- [License](#license)


# Event Consumer

The [Event Consumer](https://github.com/aurimas13/Communication-of-services/tree/main/EventConsumer) sends a POST request to the terminal while validating the incoming request through [data_validation.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/data_validation.py).
The program also involves [main file]() that creates a FLASK API, [output.py]() that opens a json data file, [config.py]() with [.env]() which defines constant VARIABLES that can be changed and [routes.py]() that sends a request to an event endpoint as defined like **/event** as API endpoint.

# Event Propagator

The [Event Propagator](https://github.com/aurimas13/Communication-of-services/tree/main/EventPropagator)

# Requirements

**Python 3.9.12** is required to properly execute package's modules, imported libraries and defined functions. Imports of several libraries like dotnet, pytest to name a few are also needed. Some required versions are found [here](https://github.com/aurimas13/BirthdayReminderApp/blob/main/requirements.txt) while those that are not mentioned come with the used Python version. Also inspect [environment variables](#environment-variables) and [authentication](#authentication) before proceeding further. For proper usage of the program you might need to run **python3** rather than proposed **python** as shown in the [Usage](#usage).<sup>1</sup>

<br><sup>1</sup>**python** or **python3** depends on the way how you installed python on your machine. </br>
# Environment variables
To be able to send emails you will need to set up environment variables. To do this locally, please create a `.env` file and add two env variables to it with valid values, like this:<sup>1</sup>
```
USR=<youremail>
PSW=<yourpassword> or <token>
```
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

