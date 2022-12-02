# 입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) 
# (단 n은 1보다 크거나 같다. n >= 1)
# 출력 : 총페이지수


# m,n=int(input(":").split())
m = int(input(":"))
n = int(input(":"))
if m%n <0:
    a= m/n+1
else:
    a= m%n ==0
print(int(a))