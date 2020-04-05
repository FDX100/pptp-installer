import os
import time
print('''
              _                    _               
             | |                  | |              
  _ __  _ __ | |_ _ __    ___  ___| |_ _   _ _ __  
 | '_ \| '_ \| __| '_ \  / __|/ _ \ __| | | | '_ \ 
 | |_) | |_) | |_| |_) | \__ \  __/ |_| |_| | |_) |
 | .__/| .__/ \__| .__/  |___/\___|\__|\__,_| .__/ 
 | |   | |       | |                        | |    
 |_|   |_|       |_|                        |_| 
install PPTPD
''')
ask = raw_input('to start install press (y) >> ')
if ask=='y' or ask=='Y':
    print('start')
else:
    os.system('killall python')
os.system('sudo apt-get update')
print('=====================')
print('system is updated')
print('=====================')
time.sleep(1)
os.system('apt-get install pptpd -y')
os.system('update-rc.d pptpd defaults')

print('=====================')
print('pptpd installed seccessfuly')
print('=====================')
time.sleep(1)
os.system('echo "localip 172.20.1.1" >> /etc/pptpd.conf')
os.system('echo "remoteip 172.20.1.2-254" >> /etc/pptpd.conf')

print('=====================')
print('subneting is completed !')
print('=====================')
time.sleep(1)
os.system('echo "ms-dns 8.8.8.8" >> /etc/ppp/pptpd-options')
os.system('echo "ms-dns 8.8.4.4" >> /etc/ppp/pptpd-options')
print('=====================')
print('DNS is installed to google DNS !')
print('=====================')
time.sleep(1)
username = raw_input('enter vpn username >> ')
password = raw_input('enter vpn password >> ')

os.system('echo "'+username+' * '+password+' *" >> /etc/ppp/chap-secrets')
print('=====================')
print('username and password set !')
print('=====================')
time.sleep(1)
os.system('echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf')
os.system('sysctl -p')
print('=====================')
print('ip forward seccessfuly !')
print('=====================')
time.sleep(1)
os.system('iptables -I INPUT -p tcp --dport 1723 -m state --state NEW -j ACCEPT')
os.system('iptables -I INPUT -p gre -j ACCEPT')
os.system('iptables -t nat -I POSTROUTING -o eth0 -j MASQUERADE')
os.system('iptables -I FORWARD -p tcp --tcp-flags SYN,RST SYN -s 172.20.1.0/24 -j TCPMSS  --clamp-mss-to-pmtu')

print('=====================')
print('ip forward seccessfuly !')
print('=====================')
time.sleep(1)
print('=====================')
print('PPTP installed and configured seccessfuly !')
print('=====================')































