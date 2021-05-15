# 대수학에서 합동인 두 숫자는, 숫자의 실제 크기를 불문하고 어떤 수로 나누었을 때 나머지만 같으면 합동이라고 일치화합니다
# 12와 26은 7로 나누면 둘다 나머지가 5이므로
# 12≡26 (mod 7)

# print(pow(3, 644) % 645)
# print(pow(1024, 1024))

# a = pow(1024, 1024)
# b = 0
# print("b : {0}".format(len(str(a))))

# 공개키 (4183, 97) 47 * 89
# 평서문 777
# 777^97 mod 4183 = 3913
print("777^97 mod 4183 = ", pow(777, 97) % 4183) # 3913

# 비밀키 d 구하기 
# d*97 mod 4183 = 1

####################################

# 예 - 교과서)

# 공개키(2537, 13) 43 * 59, e = 13
# STOP 1819 1415

# 1819^13 mod 2537 = 2081
print("1819^13 mod 2537 :", pow(1819, 13) % 2537) # 2081

# 1415^13 mod 2537 = 2182
print("1415^13 mod 2537 :", pow(1415, 13) % 2537) # 2182

# 완성된 암호문 2081 2182

# 복호화

# 개인키 = (2537, d)
# d*13 mod 2537 = 1
# d = (1 + 2537)/ 13
print("D :", (1 + 2537)/ 13)

#################################

# 예 )

#  88^7 mod 187 = 11
print(pow(88, 7) % 187)

#  d*e mod 160=1 d를 구해야 함.
# e 7이면
# d*7 mod 160=1
# d=(1+160)/7 하면, d=23이다. 

print((1+160)/7) # 23



############################
#    RSA 암호 알고리즘      #
############################

# ※ p, q의 조건
# ① p는 q와 거의 같은 크기이다.
# ② p-1과 q-1은 큰 소인수를 갖는다.
# ③ p-1과 q-1의 최대공약수는 작은 수 이다.
# ④ d는 n과 거의 같은 크기이다.

# 공개키 (n, e)

# n = p * q
# e =  1 < e < Φ(n), Φ(n)와 서로소

# Φ(n) = (p - 1) * (q - 1)

# 개인키 (n, d)
# (e * d) mod Φ(n) = 1

# 암호화
# C = M^e mod n
# C : 암호화 된 결과
# M : 원본

# 복호화
# M = C^d mod n
print()
#######################################

# 예제
# p = 17, q = 11

# n = 187
# Φ(n) = 160
# e = 7

# 공개키 (187, 7)

# d * 7 ≡ 1 mod(160)
# d * 7 % 160 = 1
# d = ( 1 + 160 ) / 7
# d = 23

# 개인키 (187, 23)


# 원본 : 88

# 암호화 88^7 mod 187
print("88^7 mod 187 :", pow(88, 7) % 187) # 11

# 암호화 된 결과 : 11

# 복호화 11^23 mod 187
print("11^23 mod 187 :", pow(11, 23) % 187) # 88
print()
###################################################

# 원본 : STOP
# 숫자화 : 18191415

# n = 187
# Z = 25 < n < ZZ = 2525 이므로 두자리씩 나누어
# 18 19 14 15 암호화

# 암호화 
print("18^7 mod 187 :", pow(18, 7) % 187) # 171
print("19^7 mod 187 :", pow(19, 7) % 187) # 145
print("14^7 mod 187 :", pow(14, 7) % 187) # 108
print("15^7 mod 187 :", pow(15, 7) % 187) # 93

# 암호화 된 결과 : 171 145 108 93

# 복호화 
print("171^23 mod 187 :", pow(171, 23) % 187) # 18
print("145^23 mod 187 :", pow(145, 23) % 187) # 19
print("108^23 mod 187 :", pow(108, 23) % 187) # 14
print("93^23 mod 187 :", pow(93, 23) % 187) # 15

# 복호화 결과 18 19 14 15

print()
###################################################

# 예제 2

# p = 43, q = 59

# n = 2537
# Φ(n) = 2436
# e = 13

# 공개키 (2537, 13)

# d * 13 ≡ 1 mod(2436)
# d = 937

# 개인키 (2537, 937)

print("원본 : STOP")
print("숫자화 : 1819 1415")

# n = 2537
# ZZ = 2525 < n < ZZZ = 252525 이므로 네자리씩 나누어
# 1819 1415 암호화

# 암호화 
print("1819^13 mod 2537 :", pow(1819, 13) % 2537) # 2081
print("1415^13 mod 2537 :", pow(1415, 13) % 2537) # 2182

# 암호화 된 결과 : 2081 2182

# 복호화 
print("2081^937 mod 2537 :", pow(2081, 937) % 2537) # 1819
print("2182^937 mod 2537 :", pow(2182, 937) % 2537) # 1415

# 복호화 결과 1819 1415

print()
###################################################

print("원본 : 777")

# n = 2537
# ZZ = 2525 < n < ZZZ = 252525 이므로 네자리씩 나누어
# 777 암호화

# 암호화 
print("777^13 mod 2537 :", pow(777, 13) % 2537) # 1990

# 암호화 된 결과 : 1990

# 복호화 
print("1990^937 mod 2537 :", pow(1990, 937) % 2537) # 777

# 복호화 결과 777

print()
###################################################

# 과제

# 공개키 (4183, 97) 47 * 89
# (p-1)(q-1) = 4048

# d = 2337
# 개인키 (4183, 2337)

print("원본 : LEE777")

# n = 4183
# ZZ = 2525 < n < ZZZ = 252525 이므로 네자리씩 나눔
print("숫자화 : 1104 0477 7")

# 암호화 
print("1104^97 mod 4183 :", pow(1104, 97) % 4183) # 257
print("0477^97 mod 4183 :", pow(477, 97) % 4183) # 2049
print("0007^97 mod 4183 :", pow(7, 97) % 4183) # 28

# 암호화 결과 0257 2049 0028

# 복호화
print("0257^2337 mod 4183 :", pow(257, 2337) % 4183) # 1104
print("2049^2337 mod 4183 :", pow(2049, 2337) % 4183) # 477
print("0028^2337 mod 4183 :", pow(28, 2337) % 4183) # 7

# 복호화 결과 1104 0477 7

#############################################

