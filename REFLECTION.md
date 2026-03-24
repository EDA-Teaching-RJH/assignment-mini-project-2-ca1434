Testing: I used unittest and assert to test the username,opinion,rating,saving and deleting of the review to make sure the code works as expected 

file:in my project I used file I/o to save reviews to a file (review.txt).I use "a" to save the reviews to the file,"r" to output them and "w" to 
delete them.

libaries:I imported the unittest libary for my tests.I also created my own libary for the regex and imported the regex libary into it and imported my own libary into movie.py

regex:In my project I used regex to make sure the username and opinions were inputted in the correct format.For opinions I used the regex to make sure that the user cannot enter in a empty opinion or a opinion thats all numbers and for the usernames I used the regex to make sure its in the correct format e.g ca14

OOP: I used the class questions that had the parameters user,film,opinion and rating and i used it to group together the functions save,delete,history,review and search.

if statements:I used if statements to make sure the user inputs a number in the specific range 

while loop:I used a while loop to repeatedly ask the user for a certain input if they input a value thats not supposed to be entered e.g if the user enters a username thats not in the correct format it will say noy valid and ask the user again 

match case: I used a match case for the options 

try and except:I used try and except to prevent the code from crashing e.g I used try and except in the test to prevent it from cashing if the file review.txt isnt found 

string manlipulation: I used .title() for the film and search input as the search function is case-sensitive.