 def maxConsecutiveOnes(self, N):
        c=0
        m=0
        while N!=0:
            y=N&1
            if y==1:
                c+=1
            else:
                if c>m:
                    m=c                                                     """geeks for geeks"""
                c=0
            N=N>>1
        else:
            if c>m:
                m=c
        return m
