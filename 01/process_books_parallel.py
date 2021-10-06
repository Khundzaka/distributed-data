# Files:
# https://www.gutenberg.org/cache/epub/66474/pg66474.txt
# https://www.gutenberg.org/cache/epub/36099/pg36099.txt

import multiprocessing
import time

from proc_ebook import process_ebook

def worker(filename):
    """worker function"""
    time.sleep(2) # to confirm that multiprocessing works
    result = process_ebook(filename)
    
    print(result)

if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=('pg36099.txt', ))
    p2 = multiprocessing.Process(target=worker, args=('pg66474.txt', ))
    p.start()
    p2.start()