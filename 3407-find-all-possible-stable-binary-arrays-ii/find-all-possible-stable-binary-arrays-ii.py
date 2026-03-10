class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1000000007
        N = 2001
        fac = [1]+[i for i in range(1, N)]
        for i in range(1, len(fac)):
            fac[i]*=fac[i-1]
            fac[i]%=MOD 
        
        facinv = [0 for i in fac]
        for i in range(len(fac)):
            facinv[i] = pow(fac[i], MOD-2, MOD)
            
        def S(n, k):
            ans = 0
            for i in range(k+1):
                if n-i*limit-1>=0 and n-i*limit-1>=k-1:
                    ans += ((-1)**i * fac[k]*facinv[k-i]*facinv[i]*fac[n-i*limit-1]*facinv[k-1]*facinv[n-i*limit-k]+MOD)%MOD
            return (ans+MOD)%MOD

        ans = 0
        for k0 in range(1, zero+1):
            for k1 in range(max(k0-1, 1), min(k0+2, one+1)):
                if k0==k1: ans += 2*S(zero, k0)*S(one, k1)
                else: ans += S(zero, k0)*S(one, k1)
                ans%= MOD
        return ans