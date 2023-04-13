
import time
def print_cube(num):
    time.sleep(2)
    print("Cube: {}" .format(num * num * num))

def print_square(num):
    time.sleep(2)
    print("Square: {}" .format(num * num))

# sequential code

def seq_code():
    start_time = time.perf_counter()
    print_cube(10)
    print_square(10)
    end_time = time.perf_counter()
    print(f' Sequential Code finished in {round(end_time-start_time,2) } second(s)')

#parallel code
import threading

def thread_code():
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    start_time = time.perf_counter()
    # starting threads
    t1.start()
    t2.start()

    # wait until thread 1 and 2 is completely executed
    t1.join()
    t2.join()

    end_time = time.perf_counter()
    print(f' Parallel Code finished in {round(end_time-start_time,2) } second(s)')
    # both threads completely executed
    print("Done!")


# processing


#parallel code

import multiprocessing


def multi_code():
    # creating thread
    t1 = multiprocessing.Process(target=print_square, args=(10,))
    t2 = multiprocessing.Process(target=print_cube, args=(10,))

    start_time = time.perf_counter()
    # starting threads
    t1.start()
    t2.start()

    # wait until thread 1 and 2 is completely executed
    t1.join()
    t2.join()

    end_time = time.perf_counter()
    print(f' Multi Parallel Code finished in {round(end_time-start_time,2) } second(s)')
    # both threads completely executed
    print("Done!")


print(__name__)


if __name__ == '__main__':
    # seq_code()
    # thread_code
    multi_code()