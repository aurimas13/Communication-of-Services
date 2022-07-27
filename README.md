<p align=center>
  <img height="222px" src="https://github.com/aurimas13/Communication-of-services/blob/main/Public/Photo/communication.jpeg"/>
</p>

<p align="center" > <b> Communication between two services </b> </p>
<p align=center>
  <a href="https://github.com/aurimas13/Communication-of-services"><img alt="python" src="https://img.shields.io/badge/language-python-blue.svg?style=social&logo=python")></a>
  <a href="https://twitter.com/aurimasnausedas"><img alt="twitter" src="https://img.shields.io/twitter/follow/aurimasnausedas?style=social"/></a>
</p>

------

The program communicates between two services - [Event Consumer](#event-consumer) & 
[Event Propagator](#event-propagator). The created Event Consumer program is a Flask API that 
receives requests from Event Propagator. This repository contains the Event Consumer API app and Event Propagator app.

Please refer to [Requirements](#requirements) for importing required libraries before looking at the [Usage](#usage)
of the app or [Configuration](#configuration), [Docker](#docker), [Tests](#tests) and other fields.

# Table of contents

- [Table of contents](#table-of-contents)
- [Event Consumer](#event-consumer)
- [Event Propagator](#event-propagator)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Usage](#usage)
- [Docker](#docker)
- [Functions](#functions)
- [Dataset](#dataset)
- [Tests](#tests)
- [Linting](#linting)
- [Public](#public)
- [Logo](#photo)
- [License](#license)



# Event Consumer
[(Back to top)](#table-of-contents)

The [Event Consumer](https://github.com/aurimas13/Communication-of-services/tree/main/EventConsumer)
is an API application that has on endpoint, **/event**, to receive events 
and then process them while validating the incoming request through 
[data_validation.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/src/data_validation.py).
The program also involves 
[main file](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/main.py) 
that is the entrypoint of the Flask API, 
[output.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/src/output.py) 
that opens a data file, 
[config.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/config.py)
with [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/.env) 
that define constant environment variables &
[routes.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/src/routes.py) 
that contains the endpoint of the application.


# Event Propagator
[(Back to top)](#table-of-contents)

The [Event Propagator](https://github.com/aurimas13/Communication-of-services/tree/main/EventPropagator) send requests
to the Event Consumer API using the **/event** endpoint. 
It randomly takes one event if the events are from a given JSON data file. The function (**send_events()**), imports 
and other functionalities are written in 
[propagator.py](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/propagate.py) module 
while environment variables that can be modified are mentioned in [Configuration](#configuration) section and are in 
the [.env](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/.env) file.


# Requirements
[(Back to top)](#table-of-contents)

`IMPORTANT NOTE:` To run the services you might need to use the virtual environment:
```
virtualenv my_env
source my_env/bin/activate
```

Python 3.10.5 is required to properly execute package's modules, imported libraries, defined functions and built-ins. 
To install the necessary libraries for Event Consumer API and Event Propagator run their respective requirements.txt
file on the respective folder as shown 
[here](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/requirements.txt) and 
[here](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/requirements.txt) like this -
`pip install -r requirements.txt`.

Inspect [Configuration](#configuration) before proceeding further 
as for proper usage of the program you might need to run **python3** rather than proposed **python** as shown in the [Usage](#usage).<sup>1</sup>

<br><sup>1</sup>**python** or **python3** depends on the way how you installed python of version 3.* 
on your machine. </br>

# Configuration
[(Back to top)](#table-of-contents)

You can configure each of the application via their `.env` files. The environment variables that you will pass
will be used in the applications globally. To configure the [Event Propagator](#event-propagator), these are the configuration variables:<sup>1,2,3</sup>
`WAIT_SECONDS` - set the time period with which to send requests from the propagator to the API,
`ENDPOINT` - define the endpoint &
`INPUT_FILE_LOCATION` - define the input event JSON file. To configure the [Event Consumer](#event-consumer), these are the variables of configuration:<sup>4,5</sup>
`PORT` - define the port number for the Flask API &
`TARGET_FILE_LOCATION` - define where write the output file.

`IMPORTANT NOTE:` If you do not configure the variables, the applications will use defaults.

Dependent on whether you run the application via Docker or not, there is an important detail to consider for the value
of the **ENDPOINT** environment variable.  If you run without Docker, in Event Propagator's `.env` file 
the variable **ENDPOINT** will use the localhost `127.0.0.1` for the app to run locally. So, for example:
```
ENDPOINT='http://127.0.0.1:4444/event'
```
If you want to run with Docker, **ENDPOINT** will need to be substituted with the defined service name. 
For example, where the Event Propagator's docker container is given the name `api_service` you can use:
```
ENDPOINT='http://api_service:4444/event
```


Below you can see an example of Event Propagator's `.env` file :
```
WAIT_SECONDS = '5'
ENDPOINT = 'http://127.0.0.1:4444/event'
INPUT_FILE_LOCATION = ''
```
and an example of `.env` file for Event Consumer would be:
```
PORT = '4444'
TARGET_FILE_LOCATION = ''
```

`IMPORTANT NOTE:` Please keep in mind that if you update the EventConsumer's **PORT**, 
you will need to reflect that change in the EventPropagator's **ENDPOINT** variable, 
and vice versa. This could look like this: `PORT=4444` and `ENDPOINT = 'http://127.0.0.1:4444/event'` locally or `PORT=4444` and 
`ENDPOINT = 'http://api_service:4444/event` through Docker.

**To run events through Docker refer [here](#docker).**

<br><sup>1</sup> WAIT_SECONDS is at `.env` file of Event Propagator as described in 
[Configuration](#configuration) section. </br>
<br><sup>2</sup> ENDPOINT is at `.env` file of Event Propagator as described in 
[Configuration](#configuration) section. </br>
<br><sup>3</sup> INPUT_FILE_LOCATION is at `.env` file of Event Propagator as described in 
[Configuration](#configuration) section. It can also be
changed by leaving an empty string at the `.env` file under the VARIABLE name and changing their directory endpoint 
at the `config.py` file.</br>
<br><sup>4</sup> PORT is at `.env` file of Event Consumer as described in 
[Configuration](#configuration) section. </br>
<br><sup>5</sup> TARGET_FILE_LOCATION is at `.env` file of Event Consumer as described in 
[Configuration](#configuration) section. It can also be
changed by leaving an empty string at the `.env` file under the VARIABLE name and changing their directory endpoint 
at the `config.py` file.</br>

# Usage
[(Back to top)](#table-of-contents)

`IMPORTANT NOTE:` You will need to 1<sup>st</sup> run the API before the propagator. After the requirements are met, the package is set at your directory and two terminal windows are run you 
are ready to make the communication between two services.  
- For the 1<sup>st</sup> terminal window to run an Event Consumer (Flask API) you will need to provide 
the python file with no arguments:<sup>1</sup> 
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

When Event Consumer and Event Propagator are run on two terminals, the output of Event Consumer on terminal 
will look like this<sup>3</sup>:

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

You can also run both services on one terminal window by heading to root directory and running **Makefile** command:
```
make services
```
The output of it will look something like this:
```
127.0.0.1 - - [27/Jul/2022 11:05:00] "POST /event HTTP/1.1" 200 -
{"event_payload":"Jack","event_type":"user_joined"}

127.0.0.1 - - [27/Jul/2022 11:05:05] "POST /event HTTP/1.1" 200 -
{"event_payload":"greetings","event_type":"message"}

ERROR:root:Bad request was sent with {'event_type': ['Not a valid string.'], 'event_payload': ['Not a valid string.']}
127.0.0.1 - - [27/Jul/2022 11:14:01] "POST /event HTTP/1.1" 400 -
INFO:werkzeug:127.0.0.1 - - [27/Jul/2022 11:14:01] "POST /event HTTP/1.1" 400 -
{"error": "Validation error - {'event_type': ['Not a valid string.'], 'event_payload': ['Not a valid string.']}"}
127.0.0.1 - - [27/Jul/2022 11:14:06] "POST /event HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [27/Jul/2022 11:14:06] "POST /event HTTP/1.1" 200 -
{"event_payload":"Jack","event_type":"user_joined"}

127.0.0.1 - - [27/Jul/2022 11:14:11] "POST /event HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [27/Jul/2022 11:14:11] "POST /event HTTP/1.1" 200 -
{"event_payload":"Peter","event_type":"user_joined"}
```

<br><sup>1</sup> The output of running Event Consumer API may differ like on what server you are running</br>
<br><sup>2</sup> The output of Event Propagator can differ from example above as it takes events randomly. </br>
<br><sup>3</sup> The output of Event Consumer can differ from example above as it might print output 
in different order.</br>

# Docker
[(Back to top)](#table-of-contents)

Setup up of dockerfiles can be found 
[here](https://github.com/aurimas13/Communication-of-services/blob/main/EventConsumer/Dockerfile) 
for Consumer Event and 
[here](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/Dockerfile) 
for Propagator Event.

`IMPORTANT NOTE:` - You will need to create docker network as shown through the docker run usage of it. If you do not 
have a network you will need to create it by running `docker network create some_network` before running events.

Before running events on Docker, you will need to make a bit of changes in `.env` file:
- Refer to [Configuration](#configuration) for instructions to change **ENDPOINT** (particularly)
and other fields on `.env` files if you don't want to use default environment variables on which the below Docker 
commands are written for running Docker.

After the ENDPOINT is set, the rest of the variables are default, the package is set at your directory and 
two Docker terminal windows are run, follow this<sup>1</sup>:
1) To build docker image on the 1<sup>st</sup> terminal window for the Event Consumer you need to go to 
the EventConsumer folder locally and run:
``` 
>>> docker build -t eventconsumer .  
```
2)  Followed by a Docker run on the same window:
``` 
>>> docker run --name api_service --network some_network -p 4444:4444 eventconsumer 
```
3) Then you will have to build docker image on the 2<sup>nd</sup> terminal window for Event Propagator by going 
to EventPropagator folder locally and running:
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
6) If you wish to check whether there are output when running through Docker as for when running locally open 
the 4<sup>th</sup> terminal window and enter directories of API:
``` 
>>> docker exec -it api_service bash
```
7) Then go to output folder and run:
```
>>> cat events.json
```

`IMPORTANT NOTE` You can also run services though Docker on two terminal windows by heading to root directory and running **Makefile** commands:
```
make event_consumer
```
and:
```
make event_propagator
```

Be aware that if you run by Docker, the input and target paths need to be defined for the docker container are not your
local system specifically. By executing `>>> docker exec -it api_service bash` or `>>> docker exec -it propagator bash` 
then go to where `events.json` is and by running in terminal `>>> pwd` you may update TARGET_FILE_LOCATION or 
INPUT_FILE_LOCATION at respective `.env` files. It could look something like this
`'/ServicesCommunication/EventConsumer/output/events.json'`for Event Consumer `.env` file and for EventPropagator `.env`
file like this `'/ServicesCommunication/EventPropagator/events.json'`.

If you wish to see what you should see on either terminal window through Docker go to [Usage](#usage) as it should be the same as shown locally there.

To cancel either of the services when both are running on Docker and you are happy press `CTRL+C`.

<br><sup>1</sup> Be sure to have opened two different terminal windows for communication  between services</br>

# Dataset
[(Back to top)](#table-of-contents)

The dataset to use for event generation is 
[events.json](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/events.json) 
as extracted from the 
[task](https://github.com/aurimas13/Communication-of-services/blob/main/Public/Task.md) file that contains 11 values.


# Tests
[(Back to top)](#table-of-contents)

Test folder to check the functionality of a created Event Consumer API can be found 
[here](https://github.com/aurimas13/Communication-of-services/tree/main/EventConsumer/Tests). Then by going to 
[Event Consumer's](https://github.com/aurimas13/Communication-of-services/tree/main/EventConsumer) folder, 
one can run this test command:
``` 
>>> python -m pytest tests/tests.py
```

You can also run tests through **Makefile** command while at root:
```
make tests/tests.py
```

<br><sup>1</sup> **Event Propagator** does not have tests as everything defined there is built-in used by
[**propagator.py**](https://github.com/aurimas13/Communication-of-services/blob/main/EventPropagator/propagate.py) 
module. </br>

# Linting
[(Back to top)](#table-of-contents)


To check the linting of the applications navigate to the program's folder - 
[Services Communication](https://github.com/aurimas13/Communication-of-services) - and run below command:
```
>>> pyflakes .
```
To check the linting of the API event go to 
[Event Consumer's](https://github.com/aurimas13/Communication-of-services/tree/main/EventConsumer) folder 
and run:
```
>>> pyflakes tests/tests.py
```

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
