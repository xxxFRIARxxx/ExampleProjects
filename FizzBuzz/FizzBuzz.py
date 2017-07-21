for multiples of three,   print   Fizz     (instead of the number)
for multiples of five,   print   Buzz     (instead of the number)
for multiples of both three and five,   print   FizzBuzz     (instead of the number)

for i in range(1,101): print("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i, end=' ')

for i in range(1, 101):
    num = ''
    if i % 3 == 0:
        num += "Fizz"
    if i % 5 == 0:
        num += "Buzz"
    if num == '':
        num += str(i)
    print(num)


truth = [(i, not i%3, not i%5) for i in range(1,101)]
message = {(True, True): "FizzBuzz", (True, False): "Fizz", (False, True): "Buzz", (False, False): ""}
results = [message[(p,q)] or i for (i, p, q) in truth]
for result in results:
    print(result)
