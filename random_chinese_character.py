#-*- coding:utf-8 -*-
__author__ = 'ashin'

import random

def rand_cn_char(length=1, encode="gb2312"):
    '''get the random chinese characters'''
    chars = []
    try:
        if encode=="gb2312":
            for i in xrange(length):
                head = random.randint(0xB0, 0xCF)
                body = random.randint(0xA, 0xF)
                tail = random.randint(0, 0xF)
                val = ( head << 8 ) | (body << 4) | tail
                char = "%x" % val
                chars.append(char.decode('hex').decode('gb2312'))

        elif encode == "unicode":
            for i in xrange(length):
                val = random.randint(0x4E00, 0x9FBF)
                chars.append(unichr(val)) 
    except:
        chars.append(u'亏')
        
    return ''.join(chars)
    
if __name__ == "__main__":
    chars = rand_cn_char()
    print chars

