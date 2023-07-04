
# autoproxy [![Downloads](https://static.pepy.tech/personalized-badge/autoproxy?period=total&units=international_system&left_color=black&right_color=grey&left_text=Downloads)](https://pepy.tech/project/autoproxy)

Asynchronous python library that simplify the proxies process

## Features
- All Proxy Types
- Fast ( Asynchronous )
- Easy to use

```
⚠️Warring: ( v0.0.2 ) Is not stable 
Just trying it and the code is not clean ( hard to read )

pip install autoproxy
```

### Example
```python
from autoproxy import autoProxy, Auto
import requests, threading, time

# Intialize AutoProxy
ap = autoProxy(logging=False)
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


#### Notes 
```python
# 1. You can update proxies by using ap.init() any time you want!
# 2. To enable logging just do autoProxy(logging=True)
# 3. You Can add your own sources like this:
# ap = autoProxy(logging=True, sources={
#     'http': [...],
#     'socks4': [...],
#     'socks5': [...]
# })
```
