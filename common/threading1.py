# -*- coding: UTF-8 -*-
# @date: 2020/6/15 23:02
# @name: threading1
# @author：wuyandong

import threading
import time


def test01():
    for i in range(10):
        print("%s" % i)

def test02():
    time1= time.time()
    threads =[]
    print("%s" % time.time())
    for i in range(10):
        t1 = threading.Thread(target=test01)
        threads.append(t1)
        print(threads)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    time2 = time.time()
    print("%s" % time.time())
    time3 = time2 - time1
    print("time3 %s " % time3)


def test03():
    time1 = time.time()
    print("%s" % time.time())
    for i in range(100):
        test01(i)
    time2 = time.time()
    print("%s" % time.time())
    time3 = time2 - time1
    print("time3 %s " % time3)


if __name__ == '__main__':
    test02()