# your code goes here!
import time

def countdown(i):
    while i > 0:
        print(f'{i} SECOND(S)!')
        i -= 1
    print("HAPPY NEW YEAR!")

# countdown(5)
def countdown_with_sleep(k):
    while k > 0:
        print(f'{k} SECOND(S)!')
        time.sleep(1)
        k -= 1
    print("HAPPY NEW YEAR!")

