# A씨는 게시판 프로그램을 작성하고 있다.

# A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.

# 입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)

# 출력 예제

# m 	n	 출력
# 0	    1	  0
# 1	    1	  1
# 2	    1	  2
# 1	    10	  1
# 10	10	  1
# 11	10	  2



# def board(m,n):
#     page = m // n
#     if m % n != 0:
#         page += 1
#     print(page)
# print(board(1,2))


def page_nom ():

    m = int(input('게시물 총 건수를 입력핫오: '))
    no = int(input('한페이지에 보여줄 게시물 수를 입력하시오: '))

    nom1= m // no
    nom2= m % no

    if nom2 >= 1 :
        nom3 = nom1+1
    else:
        nom3 = nom1
    print(m , no ,nom3 )
page_nom()