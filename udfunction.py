def defArgFunc( empname, emprole = "Manager" ):   
   print ("Emp Name: ", empname)
   print ("Emp Role ", emprole)
   return;
print("Using default value")
defArgFunc(empname="Nick")
print("************************")
print("Overwriting default value")
defArgFunc(empname="Tom",emprole = "CEO")