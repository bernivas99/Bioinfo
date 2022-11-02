with open("rosalind_fib.txt") as f:
    n, k = [int(x) for x in f.readline().split(' ')]

fib_nums=[0,1,1]

def fib(n,k,fib_nums):
    for m in range(3,n+1):
        new_val= fib_nums[m-2]*k+fib_nums[m-1]
        fib_nums.append(new_val)
    return fib_nums[n]

print(fib(n,k,fib_nums))
