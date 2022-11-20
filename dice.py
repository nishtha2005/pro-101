import random;
print("to roll the dice press y")
y=input(str("do you want to roll the dice:"))

while y =="y":
  
  no=random.randint(1,6)
  if(no==1):
    print("[   ","0","   ]")
  elif(no==2):
      print("[   ","0","   "," ","   ]")
      print("[     ","   ","    ]")  
      print("[   "," ","   ","0","  ]")  
  elif(no==3):
    print("[   ","0","   "," ","  ]")
    print("[     "," 0 ","    ]")  
    print("[   "," ","   ","0","  ]")          
  elif(no==4):
    print("[   ","0","   ","0","  ]")
    print("[     ","   ","    ]")  
    print("[   ","0","   ","0","  ]")          
  elif(no==5):
    print("[   ","0","   ","0","  ]")
    print("[     "," 0 ","    ]")  
    print("[   ","0","   ","0","  ]")          
  elif(no==6):
    print("[   ","0","   ","0","  ]")
    print("[   ","0","   ","0","  ]")  
    print("[   ","0","   ","0","  ]")          


  y=input(str("do you want to roll the dice:"))
                         
