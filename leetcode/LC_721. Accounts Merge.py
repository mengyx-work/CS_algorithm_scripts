from collections import defaultdict
class Solution(object):
    def get_accNum(self, cnnt, i):
        while i in cnnt:
            i = cnnt[i]
        return i

    def accountsMerge(self, accounts):
        accNum = 0
        emails, names, cnnt = {}, {}, {}
        for account in accounts:
            names[accNum] = account[0]
            for email in account[1:]:
                if email in emails:
                    oldAccNum = self.get_accNum(cnnt, emails[email])
                    if oldAccNum != accNum:
                        cnnt[oldAccNum] = accNum
                else:
                    emails[email] = accNum
            accNum += 1

        res = defaultdict(list)
        for email in emails:
            idx = self.get_accNum(cnnt, emails[email])
            res[idx].append(email)
        # print(cnnt)

        finals = []
        for idx in res:
            final = [names[idx]]
            res[idx].sort()
            final.extend(res[idx])
            finals.append(final)
        return finals

sol = Solution()
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
print(sol.accountsMerge(accounts))





