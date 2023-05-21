import challonge
import config

# Tell pychallonge about your [CHALLONGE! API credentials](http://api.challonge.com/v1).
challonge.set_credentials(config.api_usr, config.api_key)

# Retrieve a tournament by its id (or its url).
tournament = challonge.tournaments.show("sn1rdt6a")

# Tournaments, matches, and participants are all represented as normal Python dicts.
print(tournament["id"]) # 3272
print(tournament["name"]) # My Awesome Tournament
print(tournament["started_at"]) # None

# Retrieve the participants for a given tournament.
matches = challonge.matches.index(tournament["id"])
#for m in matches:

#print(len(matches))

participants = challonge.participants.index(tournament["id"])
for i in participants:
    print(i["name"],i["id"])

#print(len(participants)) # 13

# Start the tournament and retrieve the updated information to see the effects
# of the change.
#challonge.tournaments.start(tournament["id"])
#tournament = challonge.tournaments.show(tournament["id"])
#print(tournament["started_at"]) # 2011-07-31 16:16:02-04:00
