import threading, os, time
threads = []
tic=[]
filterlist=['one','two','three','four','five']
for i in range(len(filterlist)):
    arg=filterlist[i].strip("'")
    if i % 2==0:
        print('Waiting')
        time.sleep(5)
    command='python stream.py '+ arg
    print(command)
    def worker():
        os.system(command)
        print('Worker '+ str(i) +' complete')
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

