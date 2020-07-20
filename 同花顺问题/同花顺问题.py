import random
count=0
 #先创建一副扑克牌，然后实现对齐洗牌
Deck =[101,102,103,104,105,106,107,108,109,110,111,112,113,201,202,203,204,205,206,207,208,209,210,211,212,213,
       301,302,303,304,305,306,307,308,309,310,311,312,313,401,402,403,404,405,406,407,408,409,410,411,412,413,1000,1001] #这里当然也可以直接循环进行初始化，我这里是检查了一下牌的表示法是否可行，1000和1001分别表示大小王
# 通过遍历手牌的方式判断是否存在同花顺
class Tonghuashun:
    def __init__(self,card):
        self.card=  card
    def JUDGE(card):
        consecutive3=1
        i=0;k=1
        #print(player1)
        while(k < len(card) ):
            #print(k);
            if(consecutive3 == 5 ):
                #print("here");
                return True
            elif((card[k]-card[i])==1):
                # print(consecutive3)
                i += 1; k += 1 ; consecutive3 += 1
            else:i += 1 ; k += 1; consecutive3 = 1
    # print("no");
Player1=Tonghuashun
Player2=Tonghuashun
Player3=Tonghuashun
#---------------------------------------------------#
NUM=800000
for temp in range (0,NUM): #NUM为洗牌发牌次数，作业中设定为500,000
    random.shuffle(Deck)
    player1_deck = Deck[0:18]
    player1_deck.sort()
    player2_deck = Deck[18:36]
    player2_deck.sort()
    player3_deck = Deck[36:54]
    player3_deck.sort()
    if(Player1.JUDGE(player1_deck) or Player2.JUDGE(player2_deck) or Player3.JUDGE(player3_deck)): #只要有同花顺出现即计数一次，不用遍历所有人的手牌
        count+=1
    temp+=1
print(count / NUM)

