c=lambda l:len(l)<2or all(0<abs(b-a)<4and(b-a)*(l[1]-l[0])>0for a,b in zip(l,l[1:]))
def process_reports():n=[*map(lambda l:list(map(int,l.split())),open(__file__[:-7]+'input'))];return{"part1":(r:=sum(c(x)for x in n)),"part2":r+sum(any(c(x[:i]+x[i+1:])for i in range(len(x)))for x in n if not c(x))}

