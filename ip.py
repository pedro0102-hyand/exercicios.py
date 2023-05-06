with open("input.txt", "r") as file:
    lines=file.readlines()
valida_ips=[]
invalida_ips=[]
for line in lines:
    ip=line.strip()
    octets=ip.split(".")
    valida=True
    if len(octets)!=4:
        valida=False
        for octet in octets:
            if not octet.isdigit() or int(octet)<0 or int(octet)>255:
                valida-False
        if valida:
            valida_ips.append(ip)
        else:
            invalida_ips.appen(ip)
    with open("output.txt","w") as file:
        file.write("[Enderecos validos:]\n")
        for ip in valida_ips:
            file.write(ip+"\n")
        file.write("\n[Enderecos invalidos:]\n")
        for ip in invalida_ips:
            file.write(ip+"\n")
