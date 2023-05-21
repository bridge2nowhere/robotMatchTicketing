# Combat Robotics Match Ticketing Mangement System
Use bluetooth receipt printers to help manage combat robot events.


Current Plan
1. Figure out computer/micro **I'm going Orange Pi Zero 2**
    * Pi Nano/Orange Pi
    * Pi Pico W
    * ESP32
2. Get printer, I'm waiting for this one from China (https://www.aliexpress.us/item/3256805115935398.html?spm=a2g0o.order_list.order_list_main.5.21ef1802LgeHEo&gatewayAdapt=glo2usa)
3. Figure out the connection to Challonge API
4. Figure out the connection to printer
5. Work on enhancements:
    * Work with multiple printers (arena and queuer)
    * Work with multiple tournaments/fields (e.g. different weight classes)
    * Add pit screen display for upcoming matches
    * Modify pit display to handle multiple tournaments


## Required Setup

1. Create a text file called config.py that has the following two lines of code:
```
api_usr = "yourChallongeUsername"
api_key = "yourChallongeAPIKey"
```

