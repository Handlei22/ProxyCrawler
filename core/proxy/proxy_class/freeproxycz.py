from bs4 import BeautifulSoup
from core.proxy.proxy_base import ProxyBase
import base64

# http://free-proxy.cz/


class FreeProxyCZ(ProxyBase):
    def __init__(self):
        super().__init__()

    def __get_pages(self, response):
        soup = BeautifulSoup(response, "html.parser")
        print(response)
        pages = soup.find_all('div', {'class': 'paginator'})
        print(pages)
        # pages = pages.find_all('a')
        # for a in pages:
        #     print(a)
        input('tess')
        # return len(''.join(filter(lambda x: x.isdigit(), str(pages.text.strip()))))

    def _mount_list(self):
        def __get_ip(element):
            s = element.find('script').text.strip()
            s = s[s.find('("')+2:s.find('")')]
            s = base64.b64decode(s).decode()
            return str(s)

        url = 'http://free-proxy.cz/en/proxylist/country/all/all/ping/all'
        r = self._get(url)

        count_pages = self.__get_pages(r)
        # # print(count_pages)
        # # input('sss')

        soup = BeautifulSoup(r, "html.parser")
        table = soup.find('table', {'id': 'proxy_list'})


        if table:
            rows = table.find_all('tr')
            row_header = rows[:1][0].find_all('th')
            rows = rows[1::]
            __FIELDS = [s.text.strip() for s in row_header]
            idx_ip = __FIELDS.index('IP address')
            idx_port = __FIELDS.index('Port')
            idx_prot = __FIELDS.index('Protocol')
            for row in rows:
                cols = row.find_all('td')
                if cols[0].has_attr('colspan'):
                    continue
                ip = __get_ip(cols[idx_ip])
                port = cols[idx_port].text.strip()
                protocol = cols[idx_prot].text.strip()

                if all([ip, port, protocol]):
                    print(f'{protocol}://{ip}:{port}')
                    self._list.append(f'{protocol}://{ip}:{port}')