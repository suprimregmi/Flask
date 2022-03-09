Implementations:

-Using decorators in REST APO
-Secure flask API
-Enable tracking on Flask API
-Writing Unit test for REST API


Flask-restful: It defines resource class, which contains methods for each HTTP method. Method name should be the same as its corresponding
HTTP method and written in lowercase.


<h1>Files::</h1>
response.json(): it is a file we downloaded from postman after visiting localhost 
</br>
check_first_api.py: executing this file will prints the response from api we created. This will fetch data from server.
</br>
rest_api_get_put_delete: Here we are creating 3 HTTP methods, GET<POST<DELETE,. Here we create customize URL and when you request post from(postman or anywhere)
then it will take Name as input and on hitting GET method, will give that Name back and in Delete it will delete