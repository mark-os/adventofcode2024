
def calculate_safe(n):
 if len(n)<2:return 1
 d=[b-a for a,b in zip(n,n[1:])]
 return all(0<abs(x)<=3 for x in d)and all(x*d[0]>0 for x in d)

def process_reports():
 with open(__file__[:-7]+'input')as f:
  n=[list(map(int,l.split()))for l in f]
  a=sum(calculate_safe(x)for x in n)
  b=a+sum(any(calculate_safe(x[:i]+x[i+1:])for i in range(len(x)))for x in n if not calculate_safe(x))
  return{"part1":a,"part2":b}

