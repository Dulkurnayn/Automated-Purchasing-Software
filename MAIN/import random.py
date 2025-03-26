import random
import math
import psutil
import wmi
import time
def get_live_data():
    w = wmi.WMI()
    ram_used = psutil.virtual_memory().percent
    #temp = psutil.sensors_temperatures()['cpu_thermal'][0].current  'on windows temp sendor doesnt work du eto psutil model not facilating
    cpu_used = psutil.cpu_percent()
    return  cpu_used ,ram_used

# Example usage
x1, x2,  = get_live_data()
print(f"cpu_tem: {x1}")
print(f"RAM Used: {x2}%")

    
primes_list = [2]

def randomization():
    global primes_list
      # The starting list includes 2 to avoid complications starting the algorithm from 0
    for i in range(3, 50):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(i)
    print(primes_list)

# Calculate u as the product of items in the primes_list plus 1
def prime_gen(primes_list):
    u = 1
    for prime in primes_list:
        u *= prime
    u += 1

    # Check if u is prime
    is_u_prime = True
    for divisor in range(2, int(math.sqrt(u)) + 1): #It iterates over divisor in the range from 2 to the square root of u (inclusive).
         #t if u is not a prime number, it must have a factor that is less than or equal to its square root.
        
        if u % divisor == 0:
            is_u_prime = False
            primes_list.append(divisor)

            print(divisor,"d")
            print(u)
            print(len(primes_list))
            return prime_gen(primes_list)
        
        if len(primes_list) >= 20 :
            
            return primes_list
            

    if is_u_prime:
        primes_list.append(u)
        print(u,"u")
        return prime_gen(primes_list)
    #if len(primes_list) >= 25 :
     #       return primes_list
def generate_random_ascii_string(length):
    # Generate a random ASCII character for each position in the string
    random_ascii_string = ''.join(chr(random.randint(32, 126)) for counter in range(length))
    return random_ascii_string






randomization()
result = prime_gen(primes_list)
print(primes_list)



length_of_string = 10  # You can replace this with any desired length

# Generate and print the random ASCII string
random_string = generate_random_ascii_string(length_of_string)
print("Random ASCII string:", random_string)
print(primes_list[-1],x1)
licence = f"{random_string}-{x1 * primes_list[-1] * random.randint(1, 100)}-{int(time.strftime('%M%S'))}-{random_string}"

print(licence[:30])
