import random
import time

print('generate a random number that leans towards large numbers')

#the number of cycles will be the random number
cycle = 0

#start time using unix time stamp
st = time.time()

while True:

    num = random.getrandbits(48)

    cycle = cycle + 1

    if num == 12:

        et = time.time()

        tt = et - st

        print(f'random number is {cycle}')
        print(f'it took {tt} seconds to generate')

        with open ('ran.txt', 'a') as f:

            f.write(f'random number is {cycle}, it took {tt} seconds to generate the number')

        break


