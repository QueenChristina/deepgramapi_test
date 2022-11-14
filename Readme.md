# Audio Upload API
Simple API server that handles user audio projects. 
Run:
```
python3 manage.py runserver
```

Endpoints allow the following actions: 

1. POST raw audio data and store it. 

```
$ curl -i --form file=@myfile.wav http://localhost:8000/audios/
```
or
```
$ curl -X POST -H "Content-Type:multipart/form-data" -F "file=@myfile.wav" http://localhost:8000/audios/
```

2. GET a list of stored files, GET the content of stored files, and GET metadata of stored files, such as the duration of the audio. The GET endpoint(s) should accept a query parameter that allows the user to filter results. Results should be returned as JSON. 

GET list of stored files
```
$ curl http://localhost:8000/audios/
```

GET filtered results and their metadata
```
$ curl http://localhost:8000/audios/?name=filename.wav
$ curl http://localhost:8000/audios/?maxduration=60
$ curl http://localhost:8000/audios/?minduration=100
```

Oldest to most recent:
```
$ curl http://localhost:8000/audios/?upload_time
```
Increasing file size:
```
$ curl http://localhost:8000/audios/?size
```
Increasing duration:
```
$ curl http://localhost:8000/audios/?duration
```
Increasing bitrate:
```
$ curl http://localhost:8000/audios/?bitrate
```

GET metadata of stored file at index 2
```
$ curl http://localhost:8000/audios/2/
```

# Helpful resources
Resources I found helpful in creation of the API:
*  https://stackoverflow.com/questions/19848385/upload-file-to-django-server-using-curl
*  http://www.tomchristie.com/rest-framework-2-docs/tutorial/1-serialization
*  https://www.django-rest-framework.org/tutorial/quickstart/
*  https://docs.djangoproject.com/en/4.1/topics/http/file-uploads/

# TODO:
Eg: $ curl http://localhost/download?name=myfile.wav 

Eg: $ curl http://localhost/list?maxduration=300 

Eg: $ curl http://localhost/info?name=myfile.wav 

# Extensions
* Select only some query fields https://books.agiliq.com/projects/django-orm-cookbook/en/latest/select_some_fields.html
* Authentication https://docs.djangoproject.com/en/4.1/topics/auth/
    * https://docs.djangoproject.com/en/4.1/topics/auth/default/
    * 