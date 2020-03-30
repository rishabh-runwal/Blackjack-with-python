# Blackjack with Python
This program is designed to simulate one of the most popular card games to play, Blackjack. With the exception of Poker, Blackjack is the most popular gambling card game. 
#### About Blackjack
Equally well known as Twenty-One. The rules are simple, the play is thrilling, and there is opportunity for high strategy. In fact, for the expert player who mathematically plays a perfect game and is able to count cards, the odds are sometimes in that player's favor to win.
But even for the casual participant who plays a reasonably good game, the casino odds are less, making Blackjack one of the most attractive casino games for the player.This program is designed to simulate one of the most popular card games to play, Blackjack. 

In casino play, the dealer remains standing, and the players are seated. The dealer is in charge of running all aspects of the game, from shuffling and dealing the cards to handling all bets.

## Game Features
- Text based multi-player or single-player modes
- Option for Double-down when player has 2 cards
- 2.5 times payoff for Player upon Blackjack(b) If the player busted, she lost her bet.
- if player wins(otherthan Blackjack) The player receives twice the amount bet wins.
- If the value of the two hands is equal, it is a push and the player gets back her bet money. That is, no profit no loss.
- Tracks results of chips
- Game ends when any of the players are out of money or on demand
## Implementation
This famous card game can be quite well implemented using a simple text based script, coded in Python 3.
### Objective of the game
Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.
- **Card Values/Scoring**
 It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value.

- **Betting**
Before the deal begins, each player places a bet, in chips, in front of them in the designated area. Minimum and maximum limits are established on the betting, and the limits for this program are from $1 to $1000.

- **The Deal**
 When all the players have placed their bets, the dealer gives two cards face up to each player, and then one card face up to themselves and another face down.

- **Naturals**
 If a player's first two cards are an ace and a "ten-card" (a picture card or 10), giving him a count of 21 in two cards, this is a natural or "blackjack." 

- **The Play**
 All the players go sequentially, beginning with PLayer 1 first who must decide whether to "stand" (not ask for another card) or "hit" (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly). Thus, a player may stand on the two cards originally dealt him, or he may ask the dealer for additional cards, one at a time, until he either decides to stand on the total (if it is 21 or under), or goes "bust" (if it is over 21). In the latter case, the player loses and the dealer collects the bet wagered.

- ***Soft Hand***
 The combination of an ace with a card other than a ten-card is known as a "soft hand," because the player can count the ace as a 1 or 11, and either draw cards or not. For example with a "soft 17" (an ace and a 6), the total is 7 or 17. While a count of 17 is a good hand, the player may wish to draw for a higher total. If the draw creates a bust hand by counting the ace as an 11, the player simply counts the ace as a 1 and continues playing by standing or "hitting" (asking the dealer for additional cards, one at a time).

- **The Dealer's Play**
 When the dealer has served, his face-down card is turned up. If the total is 17 or more, he must stand. If the total is 16 or under, he must take a card. He must continue to take cards until the total is 17 or more, at which point the dealer must stand. If the dealer has an ace, and counting it as 11 would bring his total to 17 or more (but not over 21), he must count the ace as 11 and stand. 

- **Doubling Down**
 Another option open to the player is doubling his bet when the original two cards dealt total 9, 10, or 11. When the player's turn comes, he places a bet equal to the original bet, and the dealer gives him just one card, which is placed face down and is not turned up until the bets are settled at the end of the hand. With two fives, the player may split a pair, double down, or just play the hand in the regular way. Note that the dealer does not have the option of splitting or doubling down.


- See more at: http://www.bicyclecards.com/how-to-play/blackjack/#sthash.JBVMjJeE.dpuf
