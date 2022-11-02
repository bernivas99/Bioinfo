with open("rosalind_iprb.txt") as f:
    k,m,n = [int(x) for x in f.readline().split(' ')]

total_prob=(k+m+n)*(k+m+n-1)/2

two_homozig_dom_prob=k*(k-1)/(2*total_prob)
two_heterozig_prob=m*(m-1)/(2*total_prob)

result=1*two_homozig_dom_prob+(3/4)*two_heterozig_prob+1*k*m/total_prob+1*k*n/total_prob+(1/2)*m*n/total_prob

print(result)
