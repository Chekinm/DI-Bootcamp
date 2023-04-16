from time import time
import requests


def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper





@performance
def request_google():
    print('\n request google')
    response = requests.get('https://www.google.com/search?q=python')
    status_code = response.status_code
    print(status_code)

@performance
def request_bing():
    print('\n request bing')
    response = requests.get('https://www.bing.com/search?q=python')
    status_code = response.status_code
    print(status_code)


@performance
def request_baidu():
    print('\n request Baidu')
    response = requests.get('https://www.baidu.com/s?&wd=python')
    status_code = response.status_code
    print(status_code)


request_google()
request_bing()
request_baidu()



