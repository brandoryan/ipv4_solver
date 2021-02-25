def find_net_id(ip_addr, sub_mask):
    net_id = []
    for i in range(len(ip_addr)):
        net_id += '1' if (ip_addr[i] == '1' and sub_mask[i] == '1') else '0'
    return "".join(net_id)

def find_host_id(ip_addr, net_id):
    host_id = []
    for i in range(len(ip_addr)):
        if (ip_addr[i] == '1' and net_id[i] == '0'):
            host_id += '1'
        elif (ip_addr[i] == '0' and net_id[i] == '1'):
            host_id += '1'
        else:
            host_id += '0'
    return "".join(host_id)

def octet_sep(address):
    return '.'.join(address[i:i+8] for i in range(0, len(address), 8))

def calc_dec(address):
    list_addr = octet_sep(address)
    list_addr = list_addr.split('.')
    for i in range(len(list_addr)):
        list_addr[i] = int(list_addr[i], 2)
    return ".".join([str(list_a) for list_a in list_addr])

ip_addr = '00001010000000000000000110101100'
print("\nIP Address: " + octet_sep(ip_addr) + "\t(" + calc_dec(ip_addr) + ")")

sub_mask = '11111111111111111111111110000000'
print("\nSubnet Mask: " + octet_sep(sub_mask) + "\t(" + calc_dec(sub_mask) + ")")

net_id = find_net_id(ip_addr, sub_mask)
print("\nNetwork ID: "+"".join(octet_sep(net_id) + "\t(" + calc_dec(net_id) + ")"))

host_id = find_host_id(ip_addr, net_id)
print("\nHost ID: "+"".join(octet_sep(host_id) + "\t(" + calc_dec(host_id) + ")"))