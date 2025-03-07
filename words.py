#season = input("What is your favourite season?")

#season_list = ["summer", "winter", "autumn", "spring", "fall"]
#if season.lower().strip() in season_list:
#    print("That is a valid season")
#else:
#    print("That is not a valid season.")

bible = input("What is the first book of the Bible? Genesis, Exodus, Numbers or Leviticus: ")
correct = ["a","a)", "genesis", "a) genesis"]
incorrect = ["b", "b)", "exodus", "b) exodus", "c", "c)", "numbers", "c) numbers", "leviticus", "d) leviticus"]

if bible in correct.lower().strip():
    print("You are correct")

else:
    print("That is wrong")
    
