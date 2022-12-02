# 'Hello, world!' 두 개를 각 줄에 출력하는 프로그램을 만드세요
# (대소문자 구분과 띄어쓰기가 정확해야 합니다). 
# 정답에는 출력 결과를 만족하는 전체 소스 코드를 입력해야 합니다.

# print('Hello, world!' '\n' 'Hello, world!' )


# 결과
# Hello, world!
# Hello, world!
# a,b=list(map(int,(14//3,14%3)))
# print(a,b)
# a= int(input(':'))
# print(a)
# print(type(a))

# print(list(map(int,(14 //3 , 14% 3))))
# a= 'you need python'
# print(len(a))

# a=3
# b='나'
# c=5

# print(f''' 'Hello, world!' 두 개를 각 줄에 출력하는 프로그램을 만드세요
# # (대소문자 구분과 띄어쓰기가 정확해야 합니다). {a}
# # 정답{b}에는 출력 결과를 만족하는 전체 소스 코드를 입력해야 합니다{5}.''')

# a=['a','a','s','s','d','d','f','f']
# a.sort()
# print(a)


# a={'1':'2' , '3':'4' , '5':'6'}
# print(list(a.keys()))
# a.values()

# for k in a.keys():
#     print(k)

# list(a.keys())

# a={'name':'pey' , 'phone' : '01075567183' , 'birth' : '1118'}
# print(a.get('name'))
# b='hellohi'
# b=set('h''e''l''l''o')
# print(b)

# a=('국어','영어','수학')
# b=(80,75,55)

# a=int(input(':'))
# if a%2 == 0:
#     print('짝수입니다.')
# else:
#     print('홀수입니다.')

# a= 'a:b:c:d'
# b= a.replace(':','#')
# print(b)
# a=[1,3,5,4,2]
# a.sort()
# a.reverse()
# print(a)

# a={'A':90,'B':80,'C':70}
# b=a.pop('B')
# print(a)
# print(b)

# a=2000

# if a > 3000:
#     print('택시를 타고가')
# else:
#     print('걸어가')

# hit = 0
# while hit < 10:
#     hit +=1
#     print('나무를 {} 번찍었습니다.'.format(hit))
#     # hit +=1
#     if hit == 10:
#         print('나무쓰러짐')

# for a in range(10):
#     a +=1
#     print('나무를' ,a, '번 찍었습니다.')
#     if a ==10:
#         print('나무 쓰러짐')

# a=[i*2 for i in range(6) if i%2==1]
# print(a)

# a= [i+1 for i in range(10) if i<=10 == print('나무를{}번 베었습니다'.format(i+1))]

# a=0
# while i <= 1000:
#     if i %3==0:
#         a+=i
#     i +=1
# print(a)

# a= (lambda x,y: q+w)(3,4)
# print(a)

# def dani(num): return num*2
# print(list(map(dani,[1,2,3,4])))

# print(list(map(lambda a:a*2,[1,2,3,4])))

# def dani(num):
#     a=[]
#     for i in num:
#         a.append(i*2)
#     return a
# a= dani([1,2,3,4])
# print(a)


# class unit :
#     def __init__ (self,name,lv):
#         self.hello = '안녕'
#         self.__name= name
#         self.lv= lv
#     def dani (self,changename,lvup):
#         self.lv+=lvup
#         print('''{}하세요 레벨이{}으로 올랐습니다
#         유저님의 직업이 {}에서 {}로 변경 되었음을알려드립니다.'''.format(self.hello,self.lv,self.__name,changename))
# a=unit('전사',29)
# a.dani('광전사',int(input(':')))


# 다음 소스 코드에서 클래스를 작성하여 게임 캐릭터의 능력치와 '베기'가 출력되게 만드세요.

# class Knight:
#     def __init__(self,health,mana,armor):
#         self.health=health
#         self.mana=mana
#         self.armor=armor
#     def slash (self):
#         # print(self.health,self.mana,self.armor)           
#         print('베기')       
                                            
 
# x = Knight(health=542.4, mana=210.3, armor=38)
# print(x.health, x.mana, x.armor)
# x.slash()
# 실행 결과
# 542.4 210.3 38
# 베기

# 표준 입력으로 게임 캐릭터 능력치(체력, 마나, AP)가 입력됩니다. 
# 다음 소스 코드에서 애니(Annie) 클래스를 작성하여 티버(tibbers) 스킬의 피해량이 출력되게 만드세요. 
# 티버의 피해량은 AP * 0.65 + 400이며 AP(Ability Power, 주문력)는 마법 능력치를 뜻합니다.

class Annie :
    def __init__ (self,health,mana,ability_power):
         self.health=health
         self.mana=mana
         self.ability_power=ability_power
    def tibbers (self):
         power=self.ability_power*0.65+400
        print('티버:피해량 {}'.format( power))

health, mana, ability_power = map(float, input(':').split())
 
 x = Annie(health=health, mana=mana, ability_power=ability_power)
 x.tibbers()
# # 예
# # 입력
# # 511.68 334.0 298
# # 결과
# # 티버: 피해량 593.7

# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.

# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.
# a=0
# b=0
# for i in range(1000):
#     if i % 3==0:
#         a+=i
#     elif i%5==0:
#         b+=i
# print(a+b)

# print(sum(list([i for i in range(1000) if i%3==0 or i%5==0] )))