class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))

    def Find(self, x):
        if self.root[x] != x:
            self.root[x] = self.Find(self.root[x])
        return self.root[x]

    def Union(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if x == y:
            return
        if y > x:
            self.root[y] = x
        else:
            self.root[x] = y


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        email_to_account = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    uf.Union(i, email_to_account[email])
                email_to_account[email] = i

        merged = {}
        for email, account_idx in email_to_account.items():
            root = uf.Find(account_idx)
            if root not in merged:
                merged[root] = set()
            merged[root].add(email)

        result = []
        for root, emails in merged.items():
            name = accounts[root][0]
            result.append([name] + sorted(emails))

        return result