#fibapi

###Description
simple flask api. loads module fibgen. returns fibonacci sequence as json object. takes argument from url:

###Requirements
fibgen
flask
flask-RESTful

###Usage

To demo, start the flask directly:

```
$ python ./fibapi/fibapi.py
```

In another shell: 

```
curl localhost:5000/fib?num=9
```

Expected output:

```
$ curl localhost:5000/fib?num=9
{
  "fibonacci_sequence": [
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34
  ]
}
```

###Tests
Tests provided by flask test.
