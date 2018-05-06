class Solution(object):
    def _mask_email(self, S):
        S = S.lower()
        name1, addr = S.strip().split('@')
        name1 = name1.lower()
        return name1[0] + '*****' + name1[-1] + '@' + addr

    def _mask_phone(self, S):

        sign_sets = ('+', '-', '(', ')', ' ')
        def _remove_signs(S, sign_sets):
            for sign in sign_sets:
                S = S.replace(sign, '')
            return S
        phone = _remove_signs(S, sign_sets)
        if len(phone) == 10:
            return '***-***-' + phone[-4:]
        else:
            return '+' + '*'*(len(phone)-10) + '-***-***-' + phone[-4:]

    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            return self._mask_email(S)
        else:
            return self._mask_phone(S)

sol = Solution()
assert sol.maskPII('86-(10)12345678') == "+**-***-***-5678"
assert sol.maskPII('1(234)567-890') == "***-***-7890"