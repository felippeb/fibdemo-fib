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
$ curl localhost:5000/fib?n=9
```

Expected output:

```
$ curl localhost:5000/fib?n=9
{
  "fibonacci_sequence": [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21
  ]
}
```

###Tests
Tests provided by flask test.
