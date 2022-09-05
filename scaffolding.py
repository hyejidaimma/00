import random

Scaffolding=dict()
sf_all={1,2,3,4,5,6,7,8,9}
sf_owner=set(list(Scaffolding))
sf_ownerless = sf_all 

def add() :
    global sf_ownerless 
    user = int(input('4자리 숫자 (등록번호)입력하시오. : '))
    
    if user > 0 :
        sf_ownerless = list(sf_ownerless)
        owner=random.choice(sf_ownerless)
        Scaffolding[owner]=user #key:value이렇게 맞춰야 실행됨(1:3829 <-이런형태)
    
    sf_ownerless = set(sf_ownerless)    
    
    for i in sf_all:
        if i in Scaffolding:
            sf_owner.add(i)
            
            sf_ownerless = sf_all - sf_owner
    
    print(f"추가 완료 Scaffolding{Scaffolding}, 주인ㅇ {sf_owner}, 주인ㄴ{sf_ownerless}")
    


def delsf():
    global Scaffolding
    global sf_owner
    global sf_ownerless
    del_user = int(input('4자리 숫자 (삭제번호)입력하시오. : '))
    if del_user>0 : 
        mir_sf={v:k for k,v in Scaffolding.items()} #ket:value 반전시켜서 삭제 
        if del_user in mir_sf:
            del mir_sf[del_user]
            Scaffolding={v:k for k,v in mir_sf.items()}
            sf_owner=set(list(Scaffolding))
            sf_ownerless=sf_all - sf_owner
            print(f"삭제 완료 Scaffolding{Scaffolding}, 주인ㅇ {sf_owner}, 주인ㄴ{sf_ownerless}")
        else:
            print("error: 등록된 사용자 정보가 없습니다.")
            
    elif del_user == 0:
        print("삭제과정을 생략합니다.")    
            

   
while True:
    add()
    
    delsf()
    
    
