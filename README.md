ncalt
======

Simple ncat alternative script.
Use it for remote shell access.

The code is written in Python 3.

Installation
============


```
pip install ncalt
```

Example
=======

Listen on a socket
```
python -m ncalt.stage -l -t 127.0.0.1 -p 4444
```

Connect to socket
```
python -m ncalt.stage -t 127.0.0.1 -p 4444
```

Here is the output:
```
>>>[username]:
```
