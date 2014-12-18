counter = 0
                
while True:
          		wordbank = ['s', 't', 'r', 'a', 'w', 'b', 'b', 'e', 'r', 'r', 'y'] 
          		print "Topic is Fruit"
          		print "Guess a letter!"
          		answer = raw_input()
          		found = 0
          		for item in wordbank:
          		    if answer == item:
          		        print "Correct!"
          		        print "-----------"
          		        found = found + 1
          		        wordbank.remove(item)
                        if found == 0:
                            counter = counter + 1
                        if counter == 1:
                            print " O"
                            print "Enter your next letter:"
                            print "_____________"
                        if counter == 2:
                            print " O"
                            print " |"
      		            print " |"
      		            print "Enter your next letter:"
      		            print "______________"
      		        if counter == 3:
      		            print " O"
      		            print " |"
      		            print " |"
      		            print "  \\"
      		            print "Enter your next letter:"
      		            print "______________"
      		        if counter == 4:
      		            print " O"
      		            print " |"
      		            print " |"
      		            print "/ \\"
      		            print "Enter your next letter:"
      		            print "______________"
      		        if counter == 5:
      		            print " O"
      		            print " |\\"
      		            print " |"
      		            print "/ \\"
      		            print "Enter your last letter! This is your last chance to guess!"
      		        if counter == 6:
      		            print " O"
      		            print "/|\\"
      		            print " |"
      		            print "/ \\"
      		            print "What a shame..."
      		        if counter >= 6:
      		            print "He is dead."
      		            print "You lost."
      		            break
      		        if found >= 6:
      		            print "You won!"
#------------------BUNCH OF GARBAGE WE SHOULD NOT TOUCH------------
#oval = drawpad.create_oval(420,90,490,190, fill = "black")  #head
#rectangle = drawpad.create_rectangle(400,190,510,400, fill = "black")  #body
#line = drawpad.create_line(510,230,530,400, fill = "black")   #right arm
#line = drawpad.create_line(400,190,380,400, fill = "black")   #left arm
#rectangle = drawpad.create_rectangle(410,400,430,460, fill = "black")
#rectangle = drawpad.create_rectangle(480,400,500,460, fill = "black")

#myapp = MyApp(root)
#root.mainloop()



#-----------MORE GARBAGE WE SHOULD NOT TOUCH----------------------


















































