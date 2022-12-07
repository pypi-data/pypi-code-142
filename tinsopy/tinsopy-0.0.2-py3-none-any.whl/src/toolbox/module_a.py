import os


def is_prime(N:int, prime_list=None):
    N_root = int(N**(1/2))
    if prime_list != None:
        for p in prime_list:
                if N % p == 0:
                    return False
                if N > N_root:
                    return True
    else:
        if N % 2 == 0:
            return False
        
        for x in range(3,N_root,2):
            if N % x == 0:
                return False
        return True
                       
def get_primes(P_max:int):
    primes_list = [2,3,5,7]
    for x in range(3,P_max,2):
        if is_prime(x, prime_list=primes_list):
            primes_list.append(x)
    return primes_list

def read_to_list(filepath, delimiter = ","):
    with open(filepath, "r") as File:
        data = []
        lines = File.readlines()
        for line in lines:
            line_strings = []
            new_string = ""
            for let_x in line:
                if let_x == delimiter:
                    line_strings.append(new_string)
                    new_string = ""
                else:
                    new_string = new_string + let_x
            if new_string != "":
                line_strings.append(new_string)
            if line_strings[-1][-1] == "\n":
                line_strings[-1] = line_strings[-1][:-1]
            data.append(line_strings)    
    return data

                    
                    
                
            
                    
