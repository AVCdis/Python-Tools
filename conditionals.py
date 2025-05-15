userReply = input("Do you need to <business offer> ? (Enter yes or no) ")

if userReply == "yes":
    print("We can help you <business offer> ")
else:
    print("Please come back when you need. Thank you.")
    
    userReply = input("Would you like to buy <item>, buy an <item>, or make a <option>? (Enter <item>, <item>, or <option>) ")
if userReply == "<item>":
    print("We have many <item> designs to choose from.")
elif userReply == "<item>":
    print("We have many <item> sizes to choose from.")
elif userReply == "service":
    copies = input("How many would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
  
