import challonge
import time
import sys

import config

# Tell pychallonge about your [CHALLONGE! API credentials](http://api.challonge.com/v1).
challonge.set_credentials(config.api_usr, config.api_key)

# Retrieve a tournament by its id (or its url).
tournament = challonge.tournaments.show("sn1rdt6a")



#get initial data
matches = challonge.matches.index(tournament["id"])
participants = challonge.participants.index(tournament["id"])
numOfMatches = len(matches)

#make a list to track which tickets have been printed
printed = []
for n in matches:
    printed.append(False)


def printMatch(matchNum:int):
    ###function will consume match number and print the details###
    player1 = matches[matchNum]["player1_id"]
    player2 = matches[matchNum]["player2_id"]

    printer = open('/dev/usb/lp0', 'w')
    matchString = "Match " + str(matchNum+1) + "\n"
    print("Match", matchNum+1)
    printer.write(matchString)


    for r in participants:
      if (r["id"] == player1):
        print(r["name"])
        printer.write(r["name"])
        printer.write("  vs  ")
    for r in participants:
      if (r["id"] == player2):
        print(r["name"])
        printer.write(r["name"])
    printer.write("\n\n\n\n")
    printer.close()    


#main program body
while True:
    for c,m in enumerate(matches):
        #if we have 2 players and the ticket hasn't been printed, print it.
        if(m["player1_id"] != None and m["player2_id"] != None and printed[c] == False):
            printMatch(c)
            printed[c] = True
            print(printed)
    #sleep to keep API happy
    
    #pull fresh data
    matches = challonge.matches.index(tournament["id"])
    participants = challonge.participants.index(tournament["id"])
    #leave program once tournament is over.
    if all(printed):
        sys.exit("All Labels Printed")
    time.sleep(10)      




# Tournaments, matches, and participants are all represented as normal Python dicts.
#print(tournament["id"]) # 3272
#print(tournament["name"]) # My Awesome Tournament
#print(tournament["started_at"]) # None


# Retrieve the participants for a given tournament.
#matches = challonge.matches.index(tournament["id"])
#playerList = []
#playerList.append(matches[0]["player1_id"])
#playerList.append(matches[0]["player2_id"])

#participants = challonge.participants.index(tournament["id"])

#for p in playerList:
#    for r in participants:
#     if (r["id"] == p):
#        print(r["name"])

#print(len(matches))

#participants = challonge.participants.index(tournament["id"])
#for i in participants:
#    print(i["name"],i["id"])

#print(len(participants)) # 13
