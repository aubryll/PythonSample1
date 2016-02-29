# PythonSample1
Simply python Code I wrote when I first started learning Python

Code Explanation

Question 1:
Make Two lists of animals A and B and compare them to find the intersection

Question 2:
Create a list of names of your choice and have a program that searches through the list for a name that match a partial name entered from the keyboard.


Solution (Question A):
First I create my lists of animals
Then I import my Animal List I then enter 2 for loops, the first one waits for the nested for loop to loop through to move to the next index, this way I make sure no name is left unmatched.
Once a Match Name Is found it is printed out

 

Solution (Question B):
A list of names is first created to run against all search attempts
A lowercase () method that converts given strings to lowercase
This is to ensure that all searches performed are done in the same case
So that even though user inputs all lowercases or all uppercase the programmer always finds a matching output
A trim Name () method that trims a name at given index to match the size with the entered name, but before it can do that it makes sure the list name has size ranging with the entered string so that incase the entered name is 10 characters and list name is 8 characters the program does not fail but simply skips the list name and looks for one within the required parameters
The output name is then returned to the calling method
 
     Copyright (c) 2016 Nemo Technology, Inc.
 
    This file is part of PythonSample1.
 
    This is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License
    version 3 as published by the Free Software Foundation
 
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
 
    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
 

