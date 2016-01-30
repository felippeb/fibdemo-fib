#fibapi

#description
simple flask api. loads module fibgen. returns fibonacci sequence as json object. takes argument from url:

#requirements
fibgen
flask
flask-RESTful

#usage

python ./fibapi/fibapi.py

curl localhost:5000/fib?num=10
