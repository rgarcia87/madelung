import numpy 

def madelung_rocksalt(threshold_x=10,threshold_y=10,threshold_z=10) : 
    """ Calculates the madelung constant for a cubic cell """ 
    sum=0
    for i in range(-threshold_x,threshold_x+1) :
        for j in range(-threshold_y,threshold_y+1) : 
            for k in range(-threshold_z,threshold_z+1) : 
                if (i,j,k)!=(0,0,0) : 
                    sum+=((-1)**(i+j+k))/numpy.sqrt(i**2+j**2+k**2)
    return sum 

for threshold in range(0,50) : 
    print(threshold , madelung_rocksalt(threshold, threshold, threshold))


threshold=10
threshold_x=threshold
threshold_y=threshold
threshold_z=threshold


A=numpy.array([((-1)**(i+j+k))/numpy.sqrt(i**2+j**2+k**2)  for i in range(-threshold_x,threshold_x+1) for j in range(-threshold_y,threshold_y+1) 
for k in range(-threshold_z,threshold_z+1)  if (i,j,k)!=(0,0,0)  ]) 

print(sum(A))


