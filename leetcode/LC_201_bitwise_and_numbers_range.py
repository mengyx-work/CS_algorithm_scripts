class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        mStr = '{0:032b}'.format(m)
        nStr = '{0:032b}'.format(n)
        #print mStr, len(mStr)
        bits = []
        for digit, mBit, nBit in zip(range(len(mStr)), reversed(mStr), reversed(nStr)):
            #print 'mBit[digit+1:]: ', mStr[:-digit-1]
            #print 'nBit[digit+1:]: ', nStr[:-digit-1]
            #print  (mStr[digit+1:]<nStr[digit+1:])
            if mBit=='0' or nBit=='0':
                bits.append('0')
            elif mStr[:-digit-1]<nStr[:-digit-1]:
                bits.append('0')
            else:
                bits.append('1')

        return int(''.join(reversed(bits)), 2)




solut = Solution()
print solut.rangeBitwiseAnd(5, 7)

#print solut.rangeBitwiseAnd(234324235, 1231243545556)
