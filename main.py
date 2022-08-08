from core.proxy.proxys import Proxys

def main():
    vlist = []
    vlist = Proxys.proxy_list_download().get_list()
    for s in vlist:
        print(s)
    print(f'Len: {len(vlist)}')

if __name__ == '__main__':
    main()
