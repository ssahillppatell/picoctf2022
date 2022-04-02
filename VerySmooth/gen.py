#!/usr/bin/python

from binascii import hexlify, unhexlify
from email.mime import base
from gmpy2 import *
import math
import os
import sys
_DEBUG = True
if sys.version_info < (3, 9):
    math.gcd = gcd
    math.lcm = lcm

FLAG  = open('flag.txt').read().strip()
FLAG  = mpz(hexlify(FLAG.encode()), 16)
SEED  = mpz(hexlify(os.urandom(32)).decode(), 16)
STATE = random_state(SEED)

def get_prime(state, bits):
    return next_prime(mpz_urandomb(state, bits) | (1 << (bits - 1)))

def get_smooth_prime(state, bits, smoothness=16):
    p = mpz(2)
    p_factors = [p]
    while p.bit_length() < bits - 2 * smoothness:
        factor = get_prime(state, smoothness)
        p_factors.append(factor)
        p *= factor

    bitcnt = (bits - p.bit_length()) // 2

    while True:
        prime1 = get_prime(state, bitcnt)
        prime2 = get_prime(state, bitcnt)
        tmpp = p * prime1 * prime2
        if tmpp.bit_length() < bits:
            bitcnt += 1
            continue
        if tmpp.bit_length() > bits:
            bitcnt -= 1
            continue
        if is_prime(tmpp + 1):
            p_factors.append(prime1)
            p_factors.append(prime2)
            p = tmpp + 1
            break

    p_factors.sort()

    return (p, p_factors)

e = 0x10001

while True:
    p, p_factors = get_smooth_prime(STATE, 1024, 16)
    if len(p_factors) != len(set(p_factors)):
        continue
    # Smoothness should be different or some might encounter issues.
    q, q_factors = get_smooth_prime(STATE, 1024, 17)
    if len(q_factors) != len(set(q_factors)):
        continue
    factors = p_factors + q_factors
    if e not in factors:
        break

if _DEBUG:
    import sys
    sys.stdout.write(f'p = {p.digits(10)}\n\n')
    # sys.stdout.write(f'p_factors = [\n')
    # for factor in p_factors:
    #     sys.stdout.write(f'    {factor.digits(16)},\n')
    # sys.stdout.write(f']\n\n')

    sys.stdout.write(f'q = {q.digits(10)}\n\n')
    # sys.stdout.write(f'q_factors = [\n')
    # for factor in q_factors:
    #     sys.stdout.write(f'    {factor.digits(16)},\n')
    # sys.stdout.write(f']\n\n')

# print("P & Q:", p, q)
n = p * q

m = math.lcm(p - 1, q - 1)
d = pow(e, -1, m)
print("D:", d)
c = pow(FLAG, e, n)

iC = int('65446ab139efe9744c78a271ad04d94ce541a299f9d4dcb658f66f49414fb913d8ac6c90dacc1ad43135454c3c5ac76c56d71d2816dac23db5c8caa773ae2397bd5909a1f2823c230f44ac684c437f16e4ca75d50b75d2f7e5549c034aa8a723c9eaa904572a8c5c6c1ed7093a0695522a5c41575c4dbf1158ca940c02b223f50ae86e6782819278d989200a2cd2be4b7b303dffd07209752ee5a3060c6d910a108444c7a769d003bf8976617b4459fdc15a2a73fc661564267f55be6a0d0d2ec4c06a4951df5a096b079d9e300f7ad72fa6c73a630f9a38e472563434c10225bde7d08c651bdd23fd471077d44c6aab4e01323ed78641983b29633ad104f3fd', 16)
iN = int('c3117013c516d166931082a0dff0b96d80f32025ee0cd87e09097d1c7bda27058b0ed44a1275ca2f7d12cf53d3f87cfa9c5066f32a333965916673f33134d3109742c95063b8657061b4dffbc6e86c42daadf6811529666f0dacb74fad4740e8d8fdfed4e0499ff9cbe3246d70da187ad81d48b6d3875ade70c2a48fa4427bd0a66d1dee8cf0106ec2ffb4605b77f7da391e033259b82fd2d043d630c3049d47b585e4a2f348f97edc670a3a263caa5bb14b060bf4f7badab7fd542b49e7b4505b5f8de807ab6d23a53ebed81e1ff0fb9de0e7bb78ebf027a335725e62dac642e94ad55432a97267a33b2df5a1cbde63f5ee14c73a0ba9088933402a02f28d5d', 16)
print("N:", iN)
print("C:", iC)
flag = pow(iC, d, iN)
# print(flag)
hFlag = hex(flag).replace("0x", "")
# print(hFlag)
# myStr = unhexlify(f"{hex(int(f'{flag}', 10))}")
# print(unhexlify(hFlag).decode())

# print(f'n = {n.digits(16)}')
# print(f'c = {c.digits(16)}')
# 12954733754028997852381974337794052578657234445997116888773986966833953906672927333854758087138948311067026705283702432554604219365588846661439455564194249403482666797639300117516778121739499113516789569276383982528664190495721795018287071819289884517705815212104301123614307140643473978030386304775315817698143316364939915680048037281679233004764926158827916510829220765313693618920074505066976844887963253978635556217475922266969312846165177092175652574301894802746920876519919635272016595300603357669704345528528306292072369372136891250855506144433602292726785910450272810596568835511218394317159257270398452685