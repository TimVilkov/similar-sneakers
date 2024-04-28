import warnings
import multiprocessing
import pandas as pd
import requests
import shutil
import time
import re
import json

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

warnings.simplefilter('ignore')



start_time = time.time()
        
    
def do_get(args):
    for image_id, url in args:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(f'sneakers/data/images/{image_id}.png', 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)       
    return True

        
def multiprocess_parsing(data):
    _start = time.time()
    batches = []
    #batch_size = multiprocessing.cpu_count() - 1  # let's keep 1 core for ourselves
    batch_size = 7
    print(f"scraping {len(data)} urls through {batch_size} processes")
    for i in range(0, len(data), batch_size):
        batches.append(data[i : i + batch_size])
    with ProcessPoolExecutor(max_workers=batch_size) as executor:
        for results in executor.map(do_get, batches):
            pass
        print("done")
    print(f"multi-process finished in {time.time() - _start:.2f}")
        
        
         
                
if __name__ == "__main__":
    data = pd.read_csv('sneakers/data/url_dataset_extended.csv', index_col=0)
    data = [(image_id, url) for image_id, url in zip(data.image_id.values, data.url.values)]
    multiprocess_parsing(data)
    print("--- %s seconds ---" % (time.time() - start_time))