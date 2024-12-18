def c6():
	prelim = eval(input("Prelim grade: "))
	midterm = eval(input("Midterm grade: "))
	semifinal = eval(input("Semifinal grade: "))
	final = eval(input("Final grade: "))
	quiz = eval(input("Quiz grade: "))
	project = eval(input("Project grade: "))

	if (prelim >= 65 and prelim <= 100) and (midterm >= 65 and midterm <= 100) and (semifinal >= 65 and semifinal <= 100) and (final >= 65 and final <= 100) and (quiz >= 65 and quiz <= 100) and (project >= 65 and project <= 100):

		finalgrade = (prelim*0.15)+(midterm*0.15)+(semifinal*0.15)+(final*0.15)+(quiz*0.25)+(project*0.15)
			
		if finalgrade >= 75 and finalgrade <= 100:	

			print("congratulations, you passed!")
		else:
			print("Sorry, You have failed.")

	else:
		print("Invalid Grades")
c6()