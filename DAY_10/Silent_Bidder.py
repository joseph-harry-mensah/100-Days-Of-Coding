#Silent Auction Program


bids = {}

bid_finished = False
print("Welcome to the Silent Auction Program")

 # creating find_highest_bid function to sort out the highest bidder and corresponding name
def find_highest_bid(bid_record):
    highest_bid = 0
    for bid in bid_record:
        bid_cash = bid_record[bid]
        if bid_cash > highest_bid:
            highest_bid = bid_cash
            winner = bid
    print(f"The winner of this bid is {winner} with the bid amount of ${highest_bid}")    # Format of output
      
        
    # taking inputs
while not bid_finished:
    person = input("What is your name?\n")
    bid_amount = int(input("What is your bid?\n $"))
    bids[person] = bid_amount
    
    # Looping if there are other bidders
    should_continue = input("Is there anyone bidding apart from you? Yes | No").lower()
    if should_continue == "no":
        bid_finished = True
        find_highest_bid(bids)
              
    elif should_continue == "yes":
            bids.clear()      # This clears the dictionary when user ends program

    
   