from replit import clear
# call clear() to clear the output in the console.
import art
print(art.logo)
bidders_records={}
def name_bid():
  name=input("What is your name? ")
  bid=float(input("What is your bid? $"))
  bidders_records[name]=bid
name_bid()
next_bid=input("Is there any one else? Type 'yes' or 'no' ").lower()

while next_bid=="yes":
  clear()
  name_bid()
  next_bid=input("Is there any other bidder? Type 'yes' or 'no'")
winner_bid=0
if next_bid=="no":
  for name in bidders_records:
    if bidders_records[name]>winner_bid:
      winner_bid=bidders_records[name]
      winner_name=name
print( f"The winner is {winner_name} with a bid ${winner_bid}")
