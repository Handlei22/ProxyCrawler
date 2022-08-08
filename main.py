from core.proxy.proxys import Proxys

def main():
    listProxy = []
    listObj = []
    listObj.append(Proxys.proxy1())
    listObj.append(Proxys.proxy2())
    listObj.append(Proxys.proxy3())
    listObj.append(Proxys.proxy4())
    for obj in listObj:
        print(obj.link_name)
        listProxy.extend(obj.get_list())
        print(len(listProxy))
    for s in listProxy:
        print(s)
    print(len(listProxy))


if __name__ == '__main__':
    main()
