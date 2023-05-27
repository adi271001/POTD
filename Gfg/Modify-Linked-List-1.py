class Solution:
    def modify_the_list(self, head):
        a=[]
        x=head
        while True:
            a.append(x.data)
            if(x.next==None):
                break
            x=x.next
        n= int(len(a))
        for i in range(int(n/2)):
            t=a[i]
            a[i]=a[n-i-1]-a[i]
            a[n-i-1]=t
        x=head
        i=0
        while True:
            x.data=a[i]
            i+=1
            if(x.next==None):
                break
            x=x.next
        return head
