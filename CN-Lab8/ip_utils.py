def ip_to_binary(ip_address: str) -> str:
    octets = ip_address.split('.')
    return ''.join(format(int(o), '08b') for o in octets)

def get_network_prefix(ip_cidr: str) -> str:
    ip, prefix = ip_cidr.split('/')
    return ip_to_binary(ip)[:int(prefix)]
