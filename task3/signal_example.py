import signal
import time


class MyError(Exception):
    pass


def handler(sig, frame):
    raise MyError('Received signal ' + str(sig) + ' on line ' + str(frame.f_lineno) + ' in ' + frame.f_code.co_filename)


signal.signal(signal.SIGINT, handler)

try:
    print("Python signal example")
    print("Hit ctrl + c")
    while True:
        time.sleep(1)  # Hit <CTRL>+C
except KeyboardInterrupt:
    print('Keyboard interrupt caught')
except MyError as err:
    print(err)


print('Program terminated')
