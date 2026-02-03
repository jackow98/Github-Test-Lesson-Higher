def linearSearch(studentName):
     for count in range(0,6):
          if theTeam[count] == studentName:
               print("True")
               return True
     return False
          
found = linearSearch("Bob")

linearSearch("Chloe")
linearSearch("Dany")