class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1
        sz = 2 * m

        # Transition matrix
        T = [[0] * sz for _ in range(sz)]

        # 0..m-1     -> next compare = down
        # m..2m-1    -> next compare = up
        for x in range(m):
            # down -> choose y < x -> up
            for y in range(x):
                T[y + m][x] = 1

            # up -> choose y > x -> down
            for y in range(x + 1, m):
                T[y][x + m] = 1

        def mat_mul(A, B):
            n1, n2, n3 = len(A), len(B), len(B[0])
            C = [[0] * n3 for _ in range(n1)]

            for i in range(n1):
                Ai = A[i]
                Ci = C[i]
                for k in range(n2):
                    if Ai[k] == 0:
                        continue
                    aik = Ai[k]
                    Bk = B[k]
                    for j in range(n3):
                        Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
            return C

        def mat_pow(M, p):
            size = len(M)
            R = [[0] * size for _ in range(size)]
            for i in range(size):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                p >>= 1
            return R

        # Initial vector: every value can start in either block
        init = [[1] for _ in range(sz)]

        P = mat_pow(T, n - 1)
        res = mat_mul(P, init)

        return sum(row[0] for row in res) % MOD