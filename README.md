was a bit tight on time for this:

initially used a framework that supported swagger and oauth, didn't work out as
well as hoped. thats in /users

you can build the docker image by:

`cd user && docker build . -t demo-user:latest`

and then run it using:

`docker run demo-user:latest -p 8080:8080`

to test it, use:

`http PUT http://localhost:8080/users/kris name=kris email=kris@smkd.net`
`http GET http://localhost:8080/users/kris`
`http GET http://localhost:8080/users/`

it exposes a simple user service, there's also api documentation at: http://localhost/ui/

there is some oauth support also, but didn't get it fully working; uncomment line 13 in the yaml and rebuild the docker image. this uses a hardcoded auth token:

`http PUT http://localhost:8080/users/1 'Authorization: Bearer 123'`


after some struggles with the framework, I built a simple microservice from scratch in identity.

this seperates out the routing, application and persistence. the data store is injected in at runtime to allow for simplified testing locally; in real world scenarios something like dynamo would be used.

the app is also instrumented to send some basic stats to statsd for monitoring purposes

to build the docker image

`docker build . -t demo-identity:latest`

to run `docker run demo-identity:latest -p 5000:5000`

testing:

    (venv) kris@sldbook:~/xyz$ http http://localhost:5000/user/1
    HTTP/1.0 404 NOT FOUND
    Content-Length: 9
    Content-Type: text/html; charset=utf-8
    Date: Tue, 05 Nov 2019 09:48:33 GMT
    Server: Werkzeug/0.16.0 Python/3.6.8

    Not found

    (venv) kris@sldbook:~/xyz$ http -f POST http://localhost:5000/user/1 name=kris email=kris@smkd.net
    HTTP/1.0 201 CREATED
    Content-Length: 12
    Content-Type: text/html; charset=utf-8
    Date: Tue, 05 Nov 2019 09:48:38 GMT
    Server: Werkzeug/0.16.0 Python/3.6.8

    User Created

    (venv) kris@sldbook:~/xyz$ http -f POST http://localhost:5000/user/1 name=kris email=kris@smkd.net
    HTTP/1.0 409 CONFLICT
    Content-Length: 21
    Content-Type: text/html; charset=utf-8
    Date: Tue, 05 Nov 2019 09:48:45 GMT
    Server: Werkzeug/0.16.0 Python/3.6.8

    Conflict: User Exists

    (venv) kris@sldbook:~/xyz$ http http://localhost:5000/user/1
    HTTP/1.0 200 OK
    Content-Length: 40
    Content-Type: application/json
    Date: Tue, 05 Nov 2019 09:48:50 GMT
    Server: Werkzeug/0.16.0 Python/3.6.8

    {
        "email": "kris@smkd.net",
        "name": "kris"
    }

theres some unit tests impemented for the datastore, they can be run with `pytest`

