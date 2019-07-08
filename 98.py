fl=int(input())
xy=list(map(int,input().split()))
for i in range(len(xy)-1):
   if(xy[i]>xy[i+1]):
      print(i)
