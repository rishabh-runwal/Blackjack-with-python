import time       #importing time module
import random     #importing random module to generate pseudo random choices

status=[]  #creating a list which keeps track of win or lose status of players

#creating dictionary for deck of cards and assigning corresponding blackjack values
dict_deck = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Ace':11,
             'King':10,'Queen':10,'Jack':10}
kys=list(dict_deck.keys())
amt_bet=[]#creating a list which keeps track of amount bet by the players

tot_amt=[]#creating a list which keeps track of the total amount the players have

"""creating a list of Unicode values of characters representing symbols of a
    deck of cards- Heart, Diamond, Club and spade respectively"""
sym=["\U00002661" , "\U00002662" , "\U00002667" , "\U00002664"]

#Number of Players
nop = int(input("Enter no. of players "))

#Providing initial amount=1000$ to each player
for i in range(nop):
    tot_amt.append(1000)
print("Each player currently has 1000$, which can be used to bet!")

#Providing an infinite loop which runs for as long as User wishes to continue playing the game
while 1:
    #reinitializing variables for while loop
    amt_bet=[]
    cards_dealer = []
    player_cards = []
    status=[]
    val_li=[]
    cards_sym=[]
    dealer_sym=[]
    
    #Setting bet amount for each player    
    for i in range(nop):
        #Setting bet amount as negative number
        bt=-1
        player_cards.append([])
        cards_sym.append([])
        val_li.append([])
        status.append(0)
        #Continue asking for bet amount till user enters positive number
        while bt<=0:
            bt=int(input("Player {}, Enter the amount of money you want to bet".format(i+1)))
        amt_bet.append(bt)
        tot_amt[i]-=bt#Subtracting bet amount of player from his total balance
    
    
    #Function to return the sum of cards
    def val(li):
        total=0
        for i in (li):
            total+=dict_deck[i]
        if (total>21 and 'Ace' in li):
            total-=10
        return total
    
    
    # Distributing n Cards to i-th Player
    def Player_cards(n,i):
            for j in range(n):
                player_cards[i].append(random.choice(kys))
                cards_sym[i].append(random.choice(sym))
    
    
    #Distributing n cards to Dealer
    def Dealer_cards(n):
        for i in range(n):
            cards_dealer.append(random.choice(kys))
            dealer_sym.append(random.choice(sym))
            
    #Function for verifying sum of cards of dealer and Creating Dealer Hits-Condition when necessary
    def Dealer_Hits():
         while(val(cards_dealer)<17 or (val(cards_dealer)==17 and 'Ace' in cards_dealer)):
            print("Dealer -- Hits")
            Dealer_cards(1)
            print("Now the dealer has a total of " + str(val(cards_dealer)) + " with ", end='')
            for i in range(len(cards_dealer)):
                print(cards_dealer[i],dealer_sym[i],end='')
                if (i!=(len(cards_dealer))):
                    print(' and ', end='') 
                else:print('')
    #Function Which checks when Player loses and when Dealer loses
    def Win_Or_Lose(i):
        if(len(cards_dealer)==2 and val(cards_dealer)==21 and val(player_cards[i])!=21):#Dealer has BlackJack
            status[i]=0#Dealer Wins
        elif ((val(cards_dealer) > val(player_cards[i])) and val(cards_dealer)<22):#PLayer Loses
            status[i]=0
        elif(val(player_cards[i])>21):#Player Busts and loses
            status[i]=0            
        elif(val(cards_dealer) == val(player_cards[i])):#Push Condition
            status[i]=-1
        elif(val(cards_dealer)>21):#Dealer Busts
            status[i]=1
        else:
            status[i]=1#Player Wins


    Dealer_cards(2)
    print("Dealer has ?? &", cards_dealer[1],dealer_sym[1])
    #Distributing Cards to all Players
    for i in range(len(player_cards)):
        (Player_cards(2,i))
        if len(player_cards[i]) == 2:
           #Displaying Player Cards
            print("Player {} has ".format(i+1),end='')
            for l in range(len(player_cards[i])):
                print(player_cards[i][l],cards_sym[i][l],end='')
                if(l!=(len(player_cards[i])-1)):
                    print(' and ',end='')
                else:
                        print("")
        # Offering Double Down Condition
        while val(player_cards[i]) < 21:
            if(len(player_cards[i])==2):
                action = str(input("Player {}, Do you want to Double Down?, D-Yes,N-No ".format(i+1)))
                if action == 'D'or action=='d':
                    Player_cards(1,i)
                    tot_amt[i]-=amt_bet[i]
                    amt_bet[i]+=amt_bet[i]
                    
                    #Displaying Player Cards
                    print("Player {} now has a total of ".format(i+1) + str(val(player_cards[i])) + " from the cards ",end='')
                    for l in range(len(player_cards[i])):
                        print(player_cards[i][l],cards_sym[i][l],end='')
                        if(l!=(len(player_cards[i])-1)):
                            print(' and ',end='')
                        else:
                            print("")
                    break
           
            # Offering Stand and Hit Conditions
            action = str(input("Player {}, Do you want to stand or hit?, S-Stand, H-Hit ".format(i+1)))
           
            if action == "H"or action =='h':
                Player_cards(1,i)
                print("Player {} now has a total of ".format(i+1) + str(val(player_cards[i])) + " from the cards ",end='')
                for l in range(len(player_cards[i])):
                    print(player_cards[i][l],cards_sym[i][l],end='')
                    if(l!=(len(player_cards[i])-1)):
                        print(' and ',end='')
                    else:
                        print("")
            else:
                print("Player {} now has a total of ".format(i+1) + str(val(player_cards[i])) + " with ",end='')
                
                #Displaying Player Cards
                for l in range(len(player_cards[i])):
                    print(player_cards[i][l],cards_sym[i][l],end='')
                    if(l!=(len(player_cards[i])-1)):
                        print(' and ',end='')
                    else:
                        print("")
                break
        if val(player_cards[i]) > 21:#Player Bust Condition
            print("Player {} BUSTED! :( .".format(i+1))
            status[i]=0
        
        elif (val(player_cards[i]) == 21 and len(player_cards[i])==2):#Player has Blackjack condition    
             print("Player {} has BLACKJACK! Player {} Wins!! ".format(i+1,i+1))
             status[i]=1
             
    #Displaying Dealer Cards        
    print("The dealer has a total of " + str(val(cards_dealer)) + " with ", end='')
    for i in range(len(cards_dealer)):
        print(cards_dealer[i],dealer_sym[i],end='')
        if (i<(len(cards_dealer))):
            print(' and ', end='') 
        else:print('')
    Dealer_Hits()
    if val(cards_dealer) > 21:
            print("Dealer has busted!")      
    
    for i in range(len(status)):
        #Displaying Win or Lose status of Players
        Win_Or_Lose(i)    
        if status[i]==0:
            print("Player {} loses!!".format(i+1))
        elif status[i]==-1:
            print("Player {}, It is a push! You will get your money back.".format(i+1))
            tot_amt[i]+=amt_bet[i]
        elif(val(player_cards[i])==21 and len(player_cards[i])==2):
            print("Congratulations!!! Player {} Wins ${}!!".format(i+1,2.5*amt_bet[i]))
            tot_amt[i]+=(2.5*amt_bet[i])
        else:
            print("Congratulations!!! Player {} Wins ${}!!".format(i+1,2.0*amt_bet[i]))
            tot_amt[i]+=(2.0*amt_bet[i])
    
    # Displaying Balance amounts of Players, if any player has negative amount, stop the Game immediately
    for i in range(nop):
        print("Player {} has {}$ remaining".format(i+1,tot_amt[i]))
    f=0
    for i in range(nop):
        if (tot_amt[i]<0):
            f=1
            neg_plr=i
            break
    if(f==1):
        print("Player {} has Negative balance. You can no longer continue Playing!".format(neg_plr+1))
        break
    #Ask player if he wishes to continue playing
    r=(input("Do you wish to continue playing? y/n"))
    if r=='y'or r=='Y':
        #Resetting all Values of Variables
        cards_dealer = []
        player_cards = []
        status=[]
        amt_bet=[]
        i,j=0,0
        cards_sym=[]
        dealer_sym=[]
        continue
    else:break
