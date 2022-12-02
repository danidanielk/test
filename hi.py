names = ['다니','세니']
for name in names:
    with open('{}.txt'.format(name),'w',encoding='utf8')as mail:
        mail.write


(f'''
안녕하세요 {name} 님.

코딩 편집자 다니엘 입니다
현재 저희 출판사는 파이썬에 관해 책 출간을 기획중입니다.
{name} 님의 유튜브 영상을 보고 연락 드리게 되었습니다.
자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

좋은 하루 보내세요
감사합니다.

김다니엘
''')