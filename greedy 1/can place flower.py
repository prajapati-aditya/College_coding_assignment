flowerbed = [1,0,0,0,1,0,0]
n =3

def can(flower) :
    count = 0
    
    for i in range(len(flower)) :
        if flower[i] == 0:
            left = (i==0) or flower[i-1] == 0 
            right = (i==len(flower)-1) or flower[i+1] == 0
            
            if left and right :
                flower[i] = 1
                count += 1
    
    return True if count >=n else False

print(can(flowerbed))