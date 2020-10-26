GPA = float(input("Please enter your GPA note : "))
number_of_lectures = float(input("Please enter your number of lectures: "))

if number_of_lectures < 47 :
   if GPA < 2.0 : 
     print("Not enough number of lectures and GPA!")
   if GPA >= 2.0 :
     print("Not enough number of lectures.")
if number_of_lectures >= 47 :
   if GPA < 2.0 :
     print("Not enough GPA!")
   if GPA >= 2.0 :
     print("GRADUATED!")

