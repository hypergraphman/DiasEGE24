from ipaddress import ip_network

for i in range(1, 9):
    net = ip_network(f'222.231.131.3/{i + 16}', False)
    k = 0
    for ad in net:
        if f'{int(ad):0>32b}'[:16].count('1') >= f'{int(ad):0>32b}'[-16:].count('1'):
            k += 1
    if k == len(list(net)):
        print(i)
