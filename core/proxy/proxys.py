from core.proxy.proxy_class import freeproxylist, proxylistdownload, openproxy_space, ptproxyserverspro


class Proxys:
    @staticmethod
    def proxy1():
        return freeproxylist.FreeProxyList()

    @staticmethod
    def proxy2():
        return proxylistdownload.ProxyListDownload()

    @staticmethod
    def proxy3():
        return openproxy_space.OpenProxySpace()

    @staticmethod
    def proxy4():
        return ptproxyserverspro.PtProxyServersPro()

