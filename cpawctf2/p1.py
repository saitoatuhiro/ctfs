import requests
from pyquery import PyQuery as pq
import re


if __name__ == '__main__':
    url = 'http://web-01.ctf2.cpaw.site/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    proxies = {'http': 'http://localhost:8080', 'https': 'https://localhost:8080'}

    session = requests.Session()
    session.headers.update(headers)
    session.proxies.update(proxies)

    res = session.get(url=url, headers=headers, proxies=proxies)

    dom = pq(res.text)
    token = dom('input[name=\'csrfmiddlewaretoken\']').val()

    data = {'csrfmiddlewaretoken': token}
    res = session.post(url=url, data=data)

    pattern = r'(C|c)(P|p)(A|a)(W|w){[^}]+}'
    match = re.search(pattern, res.text)

    if match:
        print('[+]FLAG is', match.group())
    else:
        print('[-]FLAG not found')
