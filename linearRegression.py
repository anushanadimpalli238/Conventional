x=[[1],[2],[3],[4],[5]]
y=[30,40,50,60,70]
sumx=0
sumy=0
sumxy=0
sumxsquare=0
n=len(x)
for i in range(n):
    x1=x[i][0]
    y1=y[i]
    sumx+=x1 
    sumy+=y1 
    sumxy+=x1*y1 
    sumxsquare+=x1*x1
m=(n*sumxy-sumx*sumy)/(n*sumxsquare-sumx*sumx)    
b=(sumy-m*sumx)/n 
x=6
prediction=m*x+b 
print("Predicted marks:",prediction) 


