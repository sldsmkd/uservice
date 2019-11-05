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


the stuff in /identity is rebuilding from scratch, there's some unittests
/ mocks there.

