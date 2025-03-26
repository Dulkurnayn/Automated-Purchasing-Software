import random
import math
import psutil
import time

class Liverandom:
    def __init__(self):
        self.primes_list = [2] # Initialise the prime list variable

    def get_live_data(self): # Get live data of the device hardware
        ram_used = psutil.virtual_memory().percent
        cpu_used = psutil.cpu_percent(interval=1)
        print(cpu_used)
        return cpu_used, ram_used # Returns the values

    def prime_check(self):
        for i in range(3, 50): # Nested for loop to find primes iteratively between 3 and 50
            is_prime = True
            for divisor in range(2, int(math.sqrt(i)) + 1): 
                if i % divisor == 0: # Check if the number is prime
                    is_prime = False
                    break
            if is_prime:
                self.primes_list.append(i)
        print(self.primes_list)
    def prime_gen(self):
        u = 1
        for prime in self.primes_list:
            u *= prime

        u += 1

        is_u_prime = True
        for divisor in range(2, int(math.sqrt(u)) + 1):
            if u % divisor == 0:
                is_u_prime = False
                self.primes_list.append(divisor)
                self.primes_list.append(u//divisor)
                return self.prime_gen()

            if len(self.primes_list) >= 20:
                return self.primes_list

        if is_u_prime:
            self.primes_list.append(u)
            return self.prime_gen()

    def generate_random_ascii_string(self, length):
        random_ascii_string = ''.join(chr(random.randint(32, 126)) for _ in range(length))
        return random_ascii_string

    def combine(self):
        self.prime_check()
        self.prime_gen()
        x1, x2 = self.get_live_data()
        print(f"cpu_used: {x1}")
        print(f"RAM Used: {x2}%")
        print(self.primes_list)
        length_of_string = 10
        random_string = self.generate_random_ascii_string(length_of_string)
        print("Random ASCII string:", random_string)
        licence = f"{self.generate_random_ascii_string(10)}{x1*x2 * self.primes_list[-1] * random.randint(1, 100)}{self.generate_random_ascii_string(10)}{time.strftime('%H%M%S')}"
        print("License:", licence)
        print(licence[:30])

try:
    l1 = Liverandom()
    l1.combine()
   
except Exception as e:
    print(e)