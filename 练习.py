
import urllib.request

import re

base_url = 'https://www.qiushibaike.com/hot/page'
url = base_url + '/'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3608.4 Safari/537.36'
    }
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
html_content = resp.read().decode('utf-8')
# print(html_content)
pattern = re.compile(r'<div class="content">\n<span>(.*?)</span>',re.S)

results = re.findall(pattern, html_content)
# print(results)

i = 0
for row in results:
    i += 1
    # print('第{}条'.format(i), row)
for i in range(1, 13):
    url1 = url + '{}'.format(i)
    # print(url1)
    pattern = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
    results = re.findall(pattern, html_content)
    print('--------------')
    print('第{}页'.format(i), results)


