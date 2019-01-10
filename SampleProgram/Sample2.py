try: 
   list = 5*[0]+5*[10] 
   x = list[9] 
   print("Done!") 
except IndexError: 
   print("Index out of Bond!") 
else: 
   print("Nothing is wrong!") 
finally: 
   print("Finally block!") 