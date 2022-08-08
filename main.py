from core.proxy.proxys import Proxys

def main():
    listObj = []
    listObj.append(Proxys.proxy1())
    listObj.append(Proxys.proxy2())
    listObj.append(Proxys.proxy3())
    listObj.append(Proxys.proxy4())
    for obj in listObj:
        print(obj.link_name)


if __name__ == '__main__':
    main()
