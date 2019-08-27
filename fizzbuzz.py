#!/usr/bin/env python

i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(f'Fizzbuzz')
    elif i % 3 == 0:
        print(f'Fizz')
    elif i % 5 == 0:
        print(f'Buzz')
    else:
        print(i)
    i = i+1
input()