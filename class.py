
class dani:
    def __init__(self,name,age,mony):
        self.hi='안녕'
        self.name=name
        self.age=age
        self.__mony=mony
    def seni (self,count):
        self.__mony -= count
        print('오늘 {} 원 차비내니까 {} 남았네'.format(count , self.__mony))
        print(self.hi ,'내이름은 {} 나이는 {} 살 이야 잘부탁해'.format(self.name,self.age))
a=dani('김다니엘','33',10000)
a.seni(int(input(':')))

print(a.name)
///

--------------------------------------------------------------

class unit:
    def __init__ (self,name,lv,hp,mp):
        self.open = '유닛이 생성되었습니다.'
        self.name = name
        self.__lv = lv
        self.hp = hp
        self.mp = mp
    def seni (self,lvup,hpup,mpup):
        print(self.open)
        print(self.name)
        self.__lv += lvup
        self.hp += hpup
        self.mp += mpup
        print('Event 경험치로 인해 레벨이 {}증가하였습니다.'.format(lvup))
        print('''Lv UP!! {} 유닛의 능력치가 올랐습니다. 
        레벨:{}
        HP:{}
        mp:{}'''.format(self.name,self.__lv,self.hp,self.mp))
a=unit('요셉봇',33,2000,1000)
a.seni(int(input('UP LV:')),100,300)