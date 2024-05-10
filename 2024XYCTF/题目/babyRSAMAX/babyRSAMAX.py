from Crypto.Util.number import *
from gmpy2 import *
from random import choice

flag = b'XYCTF{******}'
e = '?'
def getBabyPrime(nbits):
    while True:
        p = 1
        while p.bit_length() <= nbits:
            p *= choice(sieve_base)
        
        if isPrime(p+1):
            return p+1

p = getBabyPrime(512)
q = getBabyPrime(512)
n = p*q
gift1 = (pow(p,e,n)-pow(q,e,n)) % n
gift2 = pow(p+q,e,n)

t = 65537
x = bytes_to_long(e)
y = pow(x, t, n)

m = bytes_to_long(flag)
c = powmod(m, e, n)

print(f'n = {n}')
print(f'gift1 = {gift1}')
print(f'gift2 = {gift2}')
print(f'c = {c}')
print(f'y = {y}')

'''
n = 39332423872740210783246069030855946244104982381157166843977599780233911183158560901377359925435092326653303964261550158658551518626014048783435245471536959844874036516931542444719549997971482644905523459407775392702211086149279473784796202020281909706723380472571862792003687423791576530085747716706475220532321
gift1 = 4549402444746338327349007235818187793950285105091726167573552412678416759694660166956782755631447271662108564084382098562999950228708300902201571583419116299932264478381197034402338481872937576172197202519770782458343606060544694608852844228400457232100904217062914047342663534138668490328400022651816597367310
gift2 = 111061215998959709920736448050860427855012026815376672067601244053580566359594802604251992986382187891022583247997994146019970445247509119719411310760491983876636264003942870756402328634092146799825005835867245563420135253048223898334460067523975023732153230791136870324302259127159852763634051238811969161011462
c = 16938927825234407267026017561045490265698491840814929432152839745035946118743714566623315033802681009017695526374397370343984360997903165842591414203197184946588470355728984912522040744691974819630118163976259246941579063687857994193309554129816268931672391946592680578681270693589911021465752454315629283033043
y = 1813650001270967709841306491297716908969425248888510985109381881270362755031385564927869313112540534780853966341044526856705589020295048473305762088786992446350060024881117741041260391405962817182674421715239197211274668450947666394594121764333794138308442124114744892164155894256326961605137479286082964520217

'''