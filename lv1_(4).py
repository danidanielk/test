# 일전에 뭐 게임 회사에서 본 간단한 퀴즈 테스트 입니다.

# 0~9까지의 문자로 된 숫자를 입력 받았을 때, 이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.

# sample inputs: 0123456789 01234 01234567890 6789012345 012322456789

# sample outputs: true false false true false



# num_list=[]

# a=input('숫자를 입력하세요 :')
# num_list.append(a)


# list1=set(a)
# # list2=list(list1)
# # list2=list.replace(',','')
# list2=sorted(list2)
# list3=num_list

# # if list1 == num_list:
# #     print('true')
# # elif list1 != num_list:
# #     print('false')

# print(list2)
# print(list3)








a=(input('숫자를 입력하세요 :').split(' '))


list1=set(a)
list2=list(list1)
list3=sorted(list2)

if len(a) > len(list3):
    print('false')
else:
    print('True')
# print((list3))
# print((str(a)))




# 모르겠다..다시풀자

# a=input('숫자를 입력하세요 :')


# set_a=list(a)
# set_a=set(a)
# set_b=(set_a)
# list(set_b)
# # set_a=sorted(a)
# for i in set_b:
#     list(i)
#     print(i)
