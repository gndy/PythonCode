import requests
import threading
import Queue
import time

'''
@author GNDY
@usage: download all records with given gi number from NCBI using multiple threads, notice that
the maximum query number of each time is blow 10000 (9000 in this script), and do not using too many
threads in case of being banned by NCBI.
'''
queue = Queue.Queue()
out_queue = Queue.Queue()

def fetch_ids(id_list):
    efetch_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    payload = {'db':'protein', 'id': ','.join(id_list), 'rettype':'fasta', 'retmode':'text'}
    try:
        r = requests.post(efetch_url, data=payload)  
    except requests.exceptions.RequestException as e:
        print e
        return ''
    return r.text

class ThreadNcbi(threading.Thread):
    '''Threaded fasta records fetch'''
    def __init__(self, queue, out_queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue
        
    def run(self):
        while True:
            gi_list = self.queue.get()
            records = fetch_ids(gi_list)
            if records:
                self.out_queue.put(records)
            else:
                queue.put(gi_list)
            self.queue.task_done()
            
class ThreadWrite(threading.Thread):
    
    def __init__(self, out_queue, filename_index):
        threading.Thread.__init__(self)
        self.out_queue = out_queue
        self.filename = filename_index
        
    def run(self):
        out_handle = open('/home/wenlei/viral_db/viral_db_'+str(self.filename), 'a')
        while True:
            records = self.out_queue.get()
            record_number = records.count('>')
            print 'fetched records: '+str(record_number)
            out_handle.write(records)
            self.out_queue.task_done()
        out_handle.close()
            
start = time.time()


with open('/home/wenlei/sequence.gi') as f:
    gi_list = f.read().splitlines()
    length = len(gi_list)

for i in range(6):
    t = ThreadNcbi(queue, out_queue)
    t.setDaemon(True)
    t.start()
    
for j in range(0, 100000, 9000):
    queue.put(gi_list[j:j+9000])
    
for i in range(3):
    tw = ThreadWrite(out_queue, i)
    tw.setDaemon(True)
    tw.start()


queue.join()
out_queue.join()
print 'elapsed time:'
print time.time()-start             
