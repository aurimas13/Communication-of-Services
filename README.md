<p align=center>
  <img height="222px" src="https://github.com/aurimas13/Communication-of-services/blob/main/Public/communication.jpeg"/>
</p>

<p align="center" > <b> Solutions </b> to <b> LeetCode </b> & HackerRank problems. </p>
<p align="center" > Most common <b>problems</b> & <b>solutions</b> from <b> MAANG </b> interviews given. </p>
<br>
<p align=center>
  <a href="https://github.com/aurimas13/LeetCode-HackerRank-MAANG/tree/main/LeetCode/Python%20Solutions"><img alt="python" src="https://img.shields.io/badge/language-python-blue.svg?style=social&logo=python")></a>
  <a href="https://github.com/aurimas13/LeetCode-HackerRank-MAANG/tree/main/LeetCode/SQL%20Solutions"><img alt="sql" src="https://img.shields.io/badge/language-sql-orange.svg?style=social&logo=sql")></a>
  <a href="https://twitter.com/aurimasnausedas"><img alt="twitter" src="https://img.shields.io/twitter/follow/aurimasnausedas?style=social"/></a>
  <img height="20px" title="profile views" src="https://img.shields.io/github/stars/aurimas13/LeetCode-HackerRank-MAANG?style=social" alt="stars">

[//]: # (  <a href="https://github.com/aurimas13/HackerRank-LeetCode/blob/main/LICENSE"><img alt="license" src="https://img.shields.io/npm/l/express?style=social"></a>)
[//]: # (  <a href="https://github.com/badges/shields/pulse"><img alt="activity" src="https://img.shields.io/github/checks-status/aurimas13/LeetCode-HackerRank-MAANG></a>)
[//]: # (  <a href="https://coveralls.io/github/badges/shields"><img alt="coverage" src="https://img.shields.io/coveralls/github/badges/shields"></a>)
</p>
<p align="center">

[//]: # (  <a href="https://github.com/aurimas13/LeetCode-HackerRank-MAANG/tree/main/LeetCode/SQL%20Solutions"><img alt="sql" src="https://img.shields.io/badge/language-sql-orange.svg?style=social&logo=sql"&#41;></a>)

[//]: # (  <a href="https://github.com/aurimas13/HackerRank-LeetCode/blob/main/LICENSE"><img alt="license" src="https://img.shields.io/npm/l/express?style=social"></a>)

[//]: # (</p>)

[//]: # (https://activity-graph.herokuapp.com/graph?username=aurimas13&theme=minimal)

------
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

