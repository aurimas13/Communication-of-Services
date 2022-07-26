<p align=center>
  <img height="222px" src="https://github.com/aurimas13/Communication-of-services/blob/main/Public/Photo/communication.jpeg"/>
</p>

<p align="center" > <b> Communication between two services </b> </p>
<p align=center>
  <a href="https://github.com/aurimas13/Communication-of-services"><img alt="python" src="https://img.shields.io/badge/language-python-blue.svg?style=social&logo=python")></a>
  <a href="https://twitter.com/aurimasnausedas"><img alt="twitter" src="https://img.shields.io/twitter/follow/aurimasnausedas?style=social"/></a>
</p>

------

The program communicates between two services - [Event Consumer](#event-consumer) & [Event Propagator](#event-propagator). The created Event Consumer program is a FLASK API that receives requests from Event Propagator. 
This repository contains **modules** like [main.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/main.py) that runs the Event Consumer API and 
[propagate.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/propagate.py) that runs Event Propagator service.

Please refer to [Requirements](#requirements) for importing libraries, packages and additional modules before looking at the [Usage](#usage) of the app or [Configuration](#configuration), [Environment variables](#environment-variables), [Docker](#docker), [Tests](#tests) and other fields.

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
- [Dataset](#dataset)
- [Tests](#tests)
- [Public](#public)
- [Logo](#photo)
- [License](#license)



# Event Consumer
[(Back to top)](#table-of-contents)

The [Event Consumer](https://github.com/aurimas13/Communication-of-services/tree/main/EventConsumer) is an API application that has a default endpoint as **/event** to receive events 
and then process them while validating the incoming request through [data_validation.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/src/data_validation.py).
The program also involves [main file](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/main.py) that creates a FLASK API, [output.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/src/output.py) 
that opens a data file, [config.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/config.py)
with [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/.env) that define constant VARIABLES &
[routes.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/src/routes.pyy) that contains the endpoint of the application.


# Event Propagator
[(Back to top)](#table-of-contents)

The [Event Propagator](https://github.com/aurimas13/Communication-of-services/tree/main/EventPropagator) send requests to the Event Consumer API using the **/event** endpoint. 
It randomly takes one event if the events are from a given JSON data file. The function (**send_events()**), imports and other functionalities are written in [propagator.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/propagate.py) module 
while VARIABLES that can be modified are mentioned in [Configuration](#configuration) section and are in 
the [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/.env) file.


# Requirements
[(Back to top)](#table-of-contents)

Python 3.10.5 is required to properly execute package's modules, imported libraries, defined functions and built-ins. 
To install the necessary libraries for Event Consumer API and Event Propagator run their respective requirements.txt file on the respective folder
as shown [here](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/requirements.txt) and [here](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/requirements.txt) like this -
`pip install -r requirements.txt`.

Inspect [Configuration](#configuration) and [Environment variables](#environment-variable) before proceeding further 
as for proper usage of the program you might need to run **python3** rather than proposed **python** as shown in the [Usage](#usage).<sup>1</sup>

<br><sup>1</sup>**python** or **python3** depends on the way how you installed python of version 3.* on your machine. </br>


# Configuration
[(Back to top)](#table-of-contents)

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
updated at Event Propagator's [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/.env) under **ENTRYPOINT** variable 
with the same **PORT** as in the Event's Consumer `.env` file.

**INPUT_FILE_LOCATION** can be changed at Event Propagator's [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/.env) file while
**TARGET_FILE_LOCATION** at Event Consumer's [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/.env) file. Further instructions are found at 
[Environment variables](#environment-variables) section.

**To run events through Docker refer [here](#docker).**

# Environment variables
[(Back to top)](#table-of-contents)

WAIT_SECONDS, ENDPOINT, INPUT_FILE_LOCATION, PORT & TARGET_FILE_LOCATION variables 
(*set the time*, *define the endpoint*, *define the input data file directory*, *define the port number* & *write the output file with directory*) 
are configurable through `.env` files by adding or changing the value found on a specific event folder like this:<sup>1,2,3,4,5</sup>
```
WAIT_SECONDS = '<int value in seconds>'
ENDPOINT = '<server:PORT/endpoint>'
INPUT_FILE_LOCATION = 'input_file_with_directory'
PORT='<port number like 4444>'
INPUT_FILE_LOCATION = 'target_file_with_directory'
```

<br><sup>1</sup> WAIT_SECONDS is at `.env` file of Event Propagator as described in [Configuration](#configuration) section. </br>
<br><sup>2</sup> ENDPOINT is at `.env` file of Event Propagator as described in [Configuration](#configuration) section. </br>
<br><sup>3</sup> INPUT_FILE_LOCATION is at `.env` file of Event Propagator as described in [Configuration](#configuration) section. It can also be
changed by leaving an empty string at the `.env` file under the VARIABLE name and changing their directory endpoint at the `config.py` file.</br>
<br><sup>4</sup> PORT is at `.env` file of Event Consumer as described in [Configuration](#configuration) section. </br>
<br><sup>5</sup> TARGET_FILE_LOCATION is at `.env` file of Event Consumer as described in [Configuration](#configuration) section. It can also be
changed by leaving an empty string at the `.env` file under the VARIABLE name and changing their directory endpoint at the `config.py` file.</br>
# Usage
[(Back to top)](#table-of-contents)

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
you will need to provide the python file with no arguments, and it should look like this:<sup>2</sup>
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
<br><sup>3</sup> The output of Event Consumer can differ from example above as it might print output in different order.</br>


# Docker
[(Back to top)](#table-of-contents)

Setup up of dockerfiles can be found [here](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/Dockerfile) for Consumer Event and 
[here](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/Dockerfile) for Propagator Event.

Before running events on Docker, you will need to make a bit of changes in `.env` file:
- Refer to [Configuration](#configuration) for instructions to change **ENDPOINT** (particularly)
and other fields on `.env` files if you don't want to use default VARIABLES on which the below Docker commands are written for running Docker.

After the **ENDPOINT** is set, the rest VARIABLES are default, the package is set at your directory and two Docker terminal windows are run, follow this<sup>1</sup>:
1) To build docker image on the 1<sup>st</sup> terminal window for the Event Consumer you need to go to the EventConsumer folder locally and run:
``` 
>>> docker build -t eventconsumer .  
```
2)  Followed by a Docker run on the same window:
``` 
>>> docker run --name api_service --network some_network -p 4444:4444 eventconsumer 
```
3) Then you will have to build docker image on the 2<sup>nd</sup> terminal window for Event Propagator by going to EventPropagator folder locally and running:
``` 
>>> docker build -t eventpropagator .  
```
4) Followed by a Docker run on the 2<sup>nd</sup> window:
``` 
>>> docker run -p 3333:3333 --name propagator --network some_network eventpropagator
```
5) If you wish to see logs on how requests are sent, open the 3<sup>rd</sup> terminal window and in it run this:
``` 
>>> docker logs api_service --follow
```
6) If you wish to check whether there are output when running through Docker as for when running locally open the 4<sup>th</sup> terminal window and enter directories of API:
``` 
>>> docker exec -it api_service bash
```
7) Then go to output folder and run:
```
>>> cat events.json
```

If you wish to see what you should see on either terminal window through Docker go to [Usage](#usage)  as it should be the same as shown locally there.

To cancel either of the services when both are running on Docker and you are happy press `CTRL+C`.

<br><sup>1</sup> Be sure to have opened two different terminal windows for communication  between services</br>


# Functions
[(Back to top](#table-of-contents)

Overview of functions found inside modules - ***main.py***, ***routes.py***, ***output.py*** & ***propagate.py***:

- **create_app()** creates a FLASK API.
- **event_endpoint():** takes a request and returns JSON object.
- **persist_output(json_string, target_path)** takes a request as **json_string** and writes it to **target_path** file.
- **send_events()** opens a data from an input file, reads data from it, randomly converts it to JSON data and sends a POST request.

In depth explanations of the functions can be found inside modules.


# Dataset
[(Back to top)](#table-of-contents)

The dataset to use is [events.json](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/events.json) 
as extracted from the [task](https://github.com/aurimas13/Communication-of-services/blob/main/Public/Task.md) file that contains 11 values.


# Tests
[(Back to top)](#table-of-contents)

Test folder to check the functionality of a created Event Consumer API can be found [here](https://github.com/aurimas13/Communication-of-services/tree/main/EventConsumer/Tests). 
An overview of functions found inside a module, [tests.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/Tests/tests.py),
of Event Consumer API are:<sup>1</sup>
- *test_correct_request_code(client)* tests if the correct response code is returned by taking a request as client.
- *test_correct_request_output(client)* tests if the correct response output is returned by taking a request as client.
- *test_incorrect_response_code(client)* tests if the incorrect response code is returned for `event_payload` by taking a request as client.
- *test_incorrect_response_code_two(client)* tests if the incorrect response code is returned for `event_type` by taking a request as client.
- *test_incorrect_response_for_event_payload(client)* tests if the incorrect response output is returned for `event_payload` by taking a request as client.
- *test_incorrect_response_for_event_type(client)* tests if the incorrect response output is returned for `event_type` by taking a request as client.

By first navigating to the program's folder - [Communication-of_services](https://github.com/aurimas13/Communication-of-services) - where it is extracted, 
one can check the source files for errors:
```
>>> pyflakes .
```

Then by going to [Event Consumer's](https://github.com/aurimas13/Communication-of-services/tree/main/EventConsumer) folder, 
one can run these test commands:
1) To check the source files for errors in test file: 
```
>>> pyflakes Tests/tests.py
```

2) To check typing for test file:
``` 
>>> python -m pytest tests/tests.py
```

<br><sup>1</sup> **Event Propagator** does not have tests as everything defined there is built-in used by
[**propagator.py**](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/propagate.py) module. </br>


# Public
[(Back to top)](#table-of-contents)

Public folder contains three files: 
- [task](https://github.com/aurimas13/Communication-of-services/blob/main/Public/Task.md) - the problem or task overview.
- [todolist](https://github.com/aurimas13/Communication-of-services/blob/main/Public/todolist.txt) - the TO DO List.
- [photo](https://github.com/aurimas13/Communication-of-services/blob/main/Public/Photo) - the Photo folder.


# Logo
[(Back to top)](#table-of-contents)

The logo of the communication between two services can be found [here](https://github.com/aurimas13/Communication-of-services/blob/main/Public/Photo/communication.jpeg).

# License
[(Back to top)](#table-of-contents)

The MIT [LICENSE](https://github.com/aurimas13/Communication-of-services/blob/main/LICENSE)
