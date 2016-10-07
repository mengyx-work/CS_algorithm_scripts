class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull_counts = 0
        cow_counts = 0
        secret_dict, guess_dict = {}, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull_counts += 1
            else:
                if secret[i] in secret_dict:
                    secret_dict[secret[i]] += 1
                else:
                    secret_dict[secret[i]] = 1

                if guess[i] in guess_dict:
                    guess_dict[guess[i]] += 1
                else:
                    guess_dict[guess[i]] = 1


        for key, value in guess_dict.items():
            if key in secret_dict:
                cow_counts += min(value, secret_dict[key])

        return '{}A{}B'.format(bull_counts, cow_counts)

sol = Solution()
print sol.getHint('1807', '7810')
print sol.getHint('1123', '0111')

        
