nums= list(range(1,101))

for num in nums:
    if num % 3 ==0 and  num % 5 ==0:
        print('FizzBuzz')
        continue
    elif num % 5 == 0:
        print('Buzz')
        continue
    elif num % 3 ==0 :
        print('Fizz')
        continue
    print(num)