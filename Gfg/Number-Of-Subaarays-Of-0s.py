class Solution():
    def no_of_subarrays(self, n,arr):
        #your code goes here
        sum=0;count=0
        for i in range(n):
            if(arr[i]==0):
                count+=1
            if(arr[i]==1):
                sum=sum+(count*(count+1))//2; 
                count=0
            elif(i==n-1):
                sum=sum+(count*(count+1))//2; 
        return sum
