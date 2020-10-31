## Data

```
{'u_id': '12345'}
```

via 
```
Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import jwt
>>> encoded = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1X2lkIjoiMTIzNDUifQ.lBTAPFU1xxDAi2Vrusfo67ypBai0vBr6O7KOt6CJf1s'
>>> print(jwt.decode(encoded, verify=False))
{'u_id': '12345'}
>>> 
```

## Justify

No, if encode the data using secrete 'comp1531' again, the result is different from the given one.

```
Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import jwt
>>> secrete = 'comp1531'
>>> data = {'u_id': '12345'}
>>> new_encoded = jwt.encode(data, secrete, algorithm='HS256')
>>> encoded = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1X2lkIjoiMTIzNDUifQ.lBTAPFU1xxDAi2Vrusfo67ypBai0vBr6O7KOt6CJf1s'
>>> assert new_encoded == encoded
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>> 
```