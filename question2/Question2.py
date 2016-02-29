'''
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
'''

'''
Objective is to create an AutoComplete like program in Python, lets say
our user inputs jo and we have john in out name library, the program is to
output John

'''
from constant import Constants

class Question2:


    ##converts given string to lowercase
    def lowerCase(self, string):
        return ((string).lower())


    ##trims listname to match size of enteredname
    def trimName(self,enteredName, listName):
        ##convert enteredname String to List
        enteredName = list(enteredName)
        ##convert convert listName String to list
        listName = list(listName)
        ##create a name string to hold trimmedname
        name = ""
        ##loop enteredname list and create trimmed name
        for i in range(len(enteredName)):
            ##check if list i is within listName index
            if i <= len(listName):
             ##append current index char to name
             name = name + listName[i]
             ##return trimmed name
        return name


    ##Method autoSuggests entered names based on listNames
    def autoSuggest(self):
        ##prompt user to enter name
          print("Enter Name To Search")
        ##pass name object from stream
        ##convert it to lower case
          name = self.lowerCase((input()))
        ##loop through name list
          for j in range (len(Constants.Constants.names)):
              ##get name from list based on current index
              lName = Constants.Constants.names[j]
              try:
                  ##pass entered name and listname to nameTrim(enteredname, listname)
                  ##to trim the listname
                  ##convert listname to lowercase to match
                  ##current case for entered name
                  if name == self.trimName(name, self.lowerCase(lName)):
                      print(lName)
              except(IndexError):
                     print("")






question2 = Question2()
question2.autoSuggest()
