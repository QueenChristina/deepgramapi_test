Simple API server that handles user audio projects. Endpoints allow the following actions: 

1. POST raw audio data and store it. 

$ curl -i --form file=@myfile.wav http://localhost:8000/audios/

2. GET a list of stored files, GET the content of stored files, and GET metadata of stored files, such as the duration of the audio. The GET endpoint(s) should accept a query parameter that allows the user to filter results. Results should be returned as JSON. 

% Eg: $ curl http://localhost/download?name=myfile.wav 

% Eg: $ curl http://localhost/list?maxduration=300 

% Eg: $ curl http://localhost/info?name=myfile.wav 

GET list of stored files
$ curl http://localhost:8000/audios/

GET metadata of stored file at index 2
$ curl http://localhost:8000/audios/2/


# Helpful resources
Resources I found helpful in creation of the API:
*  https://stackoverflow.com/questions/19848385/upload-file-to-django-server-using-curl