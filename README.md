# RTX Stock Bot  

A somewhat-useful webcrawling script that searches a few sites for stock on graphics cards.  **NOTE** This bot does not purchase any stock that it finds, because it is my opinion that scalpers eating up the stock of these items with bots are part of the problem and are wrong to be doing so.  I wrote this script merely to alert myself if stock became available anywhere, so that I'd have a better chance of purchasing one the old-fashioned way. 

--- 
## Use 
This script runs three threads, each using the BeatifulSoup library to search the page for the button that says if an item is in stock or not.  If stock is found, phone numbers added as strings to the phone_number_list will be sent a text message with the link via AWS SNS.  An SNS topic must be configured for this feature to work.  On macOS, the system will also verbally alert the user that stock has been found.  These threads run every 15 seconds.  Additional threads can be configured to search additional pages, and for a wider variety of unit.  This can be done by following the format that I have configured these first three.

Some of the sites on the list also regularly change the structure of their pages, so this may need some tweaking.  I can't guarantee that it will work out of the box with high levels of consistency because of the way these large sellers configure their distributions, but it did help me ultimately find a unit to purchase.