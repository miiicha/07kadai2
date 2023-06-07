import random

ans=str(random.randint(100,999))

n=0#回数の初期化

max_n=3#最大の回数

while True:
    number=input("3桁の数字を入力してください:")
    
    if ans ==number:
        print("Correct!!")
        break
    
    else:
        print("数字の桁と数字が合っている場合は「EAT」と言い、数字はあっているが桁が違う場合は「BITE」とします")
        hint=""
        eat=0
        bite=0
        
        for i in range (3):
            if number[i]==ans[i]:
                eat+=1
            elif number[i] in ans:
                bite+=1
            
        hint += f"{eat}EAT-{bite}BITE"
        
        print(hint)

if len(ans) >=4:
    print("回答数の制限に達しました．正解は”ans”でした．")


