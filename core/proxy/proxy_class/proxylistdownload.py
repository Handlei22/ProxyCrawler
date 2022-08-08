from core.proxy.proxy_base import ProxyBase

# https://www.proxy-list.download/


class ProxyListDownload(ProxyBase):
    def __init__(self):
        super().__init__()

    def _mount_list(self):
        protocol = ['http', 'https', 'socks4', 'socks5']
        for p in protocol:
            url = f'https://www.proxy-list.download/api/v1/get?type={p}'
            r = self._get(url)
            self._list.extend(list(map(lambda ss: f'{p.upper()}://{ss}', r.splitlines())))
