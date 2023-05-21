# Combat Robotics Match Ticketing Mangement System
Use bluetooth receipt printers to help manage combat robot events.

My plan is to have the receipt printer at each arena, tickets will be generated each time a match is made on Challonge, they are placed in the Order Holder mounted to the arena (or on the queueing table). As matches are finished, the ref will mark the winner on the ticket and pass it to event staff to update Challonge.

Future plans include:
* having multiple printers, one for queuers and one for each arena
* having a pit display showing upcoming matches
* being able to handle multiple weight classes at same time.


## Materials
1. Orange Pi Zero 2
2. Bluetooth Thermal Printer ((https://www.aliexpress.us/item/3256805115935398.html?spm=a2g0o.order_list.order_list_main.5.21ef1802LgeHEo&gatewayAdapt=glo2usa). I'm waiting for mine to come from China currently
3. Order Holder for each Arena (https://a.co/d/fk8tfZT)


## Required Setup
Create a text file called config.py that has the following two lines of code, replace the text in the quotes with your Challonge details:
```
api_usr = "yourChallongeUsername"
api_key = "yourChallongeAPIKey"
```

## To Do
1. Figure out the connection to Challonge API
2. Figure out the connection to printer
3. Work on enhancements:
    * Work with multiple printers (arena and queuer)
    * Work with multiple tournaments/fields (e.g. different weight classes)
    * Add pit screen display for upcoming matches
    * Modify pit display to handle multiple tournaments
