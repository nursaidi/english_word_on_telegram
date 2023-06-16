from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += 1
    return result

