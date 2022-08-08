import core.proxy.proxy_class as p


class Proxys:

    # @staticmethod
    # def free_proxy_list():  # Deprecated
    #     return freeproxylists.FreeProxyList()

    @staticmethod
    def free_proxy_list2():
        return p.freeproxylist2.FreeProxyList2()

    # @staticmethod
    # def free_proxy_cz():  # Deprecated
    #     return freeproxycz.FreeProxyCZ()

    @staticmethod
    def proxy_list_download():
        return p.proxylistdownload.ProxyListDownload()

    @staticmethod
    def open_proxy_space():
        return p.openproxy_space.OpenProxySpace()

    @staticmethod
    def pt_proxy_servers_pro():
        return p.ptproxyserverspro.PtProxyServersPro()
