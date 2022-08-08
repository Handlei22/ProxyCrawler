import requests
from core.consts import consts
import random
from bs4 import BeautifulSoup
import urllib.parse


# www.freeproxylists.net


class FreeProxyList:
    def __init__(self):
        self.__FIELDS = [
            'IP Address',
            'Port',
            'Protocol',
            'Anonymity',
            'Country',
            'Region',
            'City',
            'Uptime',
            'Response',
            'Transfer'
        ]
        self.__list = []

    def get_list(self):
        self.__mount_list()
        return self.__list

    def __get(self, url):
        headers = {
            'user-agent': consts.userAgents[random.randint(0, len(consts.userAgents) - 1)],
            'cookie': 'hl=en; userno=20220802-000390; from=google; refdomain=www.google.com; visited=2021/08/02 01:06:35; pv=9',
            'authority': 'www.freeproxylists.net',
            'method': 'GET',
            'path': '/?s=rs&page=1',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        }
        r = requests.get(url, headers=headers)
        return r.text

    def __get_pages(self, request):
        soup = BeautifulSoup(request, "html.parser")
        pages = soup.find('div', {'class': 'page'})
        return len(''.join(filter(lambda x: x.isdigit(), str(pages.text.strip()))))

    def __mount_list(self):
        current_page = 1
        r = self.__get(f'https://www.freeproxylists.net/?s=rs&page={current_page}')
        print(r)
        pages = self.__get_pages(r)

        list = []
        while True:
            soup = BeautifulSoup(r, "html.parser")
            table = soup.find('table', {'class': 'DataGrid'})
            if table:
                rows = table.find_all('tr')[1::]
                for row in rows:
                    cols = row.find_all('td')
                    protocol, ip, port = '', '', ''
                    for _index, _ele in enumerate(cols):
                        if self.__FIELDS[_index] == 'IP Address':
                            if _ele.find('script'):
                                ip = _ele.find('script').text.strip().replace('IPDecode("', '').replace('")', '')
                                ip = urllib.parse.unquote(ip)
                                ip = ip[ip.find('">') + 2:ip.find('</')]
                        elif self.__FIELDS[_index] == 'Port':
                            port = _ele.text.strip()
                        elif self.__FIELDS[_index] == 'Protocol':
                            protocol = _ele.text.strip()
                    if (protocol != '') and (ip != '') and (port != ''):
                        list.append(f'{protocol}://{ip}:{port}')
            if current_page < pages:
                current_page += 1
                r = self.__get(f'https://www.freeproxylists.net/?s=rs&page={current_page}')
            else:
                self.__list = list
                return False
