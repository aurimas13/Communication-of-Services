all: event_consumer event_propagator

servers:
	make -j 2 event_consumer event_propagator

event_consumer: setup
	python EventConsumer/main.py

event_propagator:
	sleep 5
	python EventPropagator/propagate.py

setup:
	pip install -r EventConsumer/requirements.txt
	pip install -r EventPropagator/requirements.txt

test:
	python -m pytest EventConsumer/tests/tests.py

# Need to update ENDPOINT environment variable api_service instead of 127.0.0.1 a
docker_consumer:
	docker build -t eventconsumer EventConsumer/.
	docker run --name api_service --network some_network -p 4444:4444 eventconsumer

docker_propagator:
	docker build -t eventpropagator EventPropagator/.
	docker run -p 3333:3333 --name propagator --network some_network eventpropagator