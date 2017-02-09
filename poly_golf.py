def golf(n):
    from math import trunc,sqrt
    n+=1
    while(not(len(str(n))==1 or (str(n)[0]==str(n)[-1] and str(n)[1]==str(n)[-2])) and bool([n for i in range(2,trunc(sqrt(n))+1) if n%i==0])):
    	n+=1
    return n

print golf(679)

'─█▄▀▄▀▄█────'
'─█░▀░▀░█▄───'
'─█░▀░░░█─█──'
'─█░░░▀░█▄▀──'
'─▀▀▀▀▀▀▀────'