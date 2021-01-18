code folder contains 3 file
1. scrap.py 
 to run this file one need cromedriver which is present in chrome folder.  change path to chrome folder
 one might need to chage the ulr text to latest but shoud maintan the same formante i.e city to , city frome , date
  change date  as required.

2. scrape coordinate;
  this will read the data colleected in csv format, will identify unique cities and will search foe its coordinate. it is important to maintain same name of city in csv file scraped through scrap.py and in this scrap coordinate output file. this code takes care of it

3. weighted network 
this file calculate weighted network , it read the filght data csv file and output a file in format city_from+"_"+city_to and weight as other coloumn. after that we will need to use exel to seperate these 2 coloumn into 3 coloum i.e city_from | city_to | weight.


if you run the code all output will save on temp folder
