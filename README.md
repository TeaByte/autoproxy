# autoproxy v0.0.2
Asynchronous python library that simplify the proxies process

## Features
- All Proxy Types
- Fast ( Asynchronous )
- Easy to use

```
⚠️Warring: ( v0.0.2 ) Is not stable 
Just trying it and the code is not clean ( hard to read ) yet 

pip install autoproxy
```

Example
```python
from autoproxy import autoProxy, Auto
import requests

# Intialize AutoProxy
ap = autoProxy(logging=True)
ap.init()

# Auto Decorator
# proxy_type = ( all, socks4, socks5, socks4 )
@Auto(proxy_type="all")
def test(proxies):
    try:
        req = requests.get(
            'https://httpbin.org/ip', 
            proxies=proxies, 
            timeout=10
        )
        print(req.text)
    except requests.exceptions.RequestException as e:
        print('Bad Proxy')

while True:
    test()
```

Lets make it faster 
```python
from autoproxy import autoProxy, Auto
import requests, threading, time

# Intialize AutoProxy
ap = autoProxy(logging=True)
ap.init()

@Auto(proxy_type="all")
def test(proxies):
    try:
        req = requests.get(
            'https://httpbin.org/ip', 
            proxies=proxies, 
            timeout=10
        )
        print(req.text)
    except requests.exceptions.RequestException as e:
        pass

while True:
    while threading.active_count() > 200: time.sleep(0.5)
    threading.Thread(target=test).start()
```

Notes 
```python
# 1. You can update proxies by using ap.init() any time you want!
# 2. To disable logging just do autoProxy(logging=False)
# 3. You Can add your own sources like this:
# ap = autoProxy(logging=True, sources={
#     'http': [...],
#     'socks4': [...],
#     'socks5': [...]
# })
```
