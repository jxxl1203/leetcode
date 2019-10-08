def hostInit():
    outsides = ['172.16.12.223 www.baidu.com',
                '172.16.10.223 pan.baidu.com',
                '172.16.12.111 un.baidu.com',
                '172.16.12.223 passport.baidu.com']
    output = open(r'C:\WINDOWS\system32\drivers\etc\HOSTS', 'w')
    for i in outsides:
        output.write(i)
        output.write("\n")
    output.close()

hostInit()