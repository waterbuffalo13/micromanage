import os
import os
import booklog
import friends
import habits
import profile
import virtues
from datetime import datetime
import achievements
import spec
import task
import journal

months = ["Unknown", "January", "Febuary", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]
date = ["th", "st" , "nd", "rd"]
estime =["1-10 minutes", "10-30 minutes","30-60 minutes", "1-2 hours","2-4 hours", "4+ hours"]
now = datetime.now()
month = (months[now.month])
day = (now.day)
suffix = ""
newtasks = ""
moral = ""
curdate = now.strftime("%m" +"/"+ "%d"+ "/" + "%Y")

def Journal():
	os.system('cls' if os.name == 'nt' else 'clear')
	with open("savefiles/journallist.txt", "r") as file:
		data2 = eval(file.readline())
	journallist=data2

	print("Welcome to my journal! \n")
	print("View current entries")
	for x in journallist:
		print(str(journallist.index(x) + 1) + " " + x.get("timestamp") + " " + x.get("title") +  " " +x.get("wellbeing"))
	print("\n")
	#Read wellbeing
#	with open("wellbeing.txt", "r") as file:
#		data2 = eval(file.readline())
#	wellbeinglist=data2
	#print(wellbeinglist)
	#wellbeing

	print("(1) - Add an entry for today")
	print("(2) - View previous entry")
	print("(3) - Modify previous entry")
	
	print("")
	print("Switch views")
	print(" (A)chievements log | (D)iet Planner   |")
	print(" (H)abits tracker   | (F)riends        | (T)odo")
	print(" (J)ournal          | (P)rofile")

	check = input("What would you like to do? \n \n")
	if(check == "1"):
		strtimestamp = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
		#catch date
		#for x in journallist:
		#	if(strtimestamp == x.get("timestamp")):
			#	catch = input("failed")
		title = input("What is the title for today's entry?: ")
		lines = []
		index  = 0
		suffix =""
		while True:
			if 4 <= index <= 20 or 24 <= index <= 30:
				suffix = "th"
			else:
				suffix = ["st", "nd", "rd"][index % 10 - 1]
			index +=1
			if(index == 1):
				line = input("What did you do today? \n")
			else:
				
				line = input(str(index) + suffix +" paragraph \n")
			if line:
				lines.append(line)
			else:
				break
		content = "\n".join(lines)	
		wellbeing = input("How did you feel today? \n (-3 Severe Depression -2 Moderate Depression 1-Borderline Depression 0- Neutral 1-Content 2-Happy 3-Eastatics ")
		comb = {"timestamp": strtimestamp, "title": title, "content": content, "wellbeing": wellbeing }
		print(comb)

		journallist.append(dict(comb))
		copyjournallist= journallist
		os.system('cls' if os.name == 'nt' else 'clear')
		with open("savefiles/journallist.txt", "w") as file:
			file.write(str(copyjournallist))
		Journal()


	if(check == "2"):
		print("View current entries")
		for x in journallist:
			print(str(journallist.index(x) + 1) + " " + x.get("timestamp") + " " + x.get("title") +  " " +x.get("wellbeing"))
		print("\n")
		picklist = input("which one do you want to view")
		for idx,val in enumerate(journallist):
			if(str(idx + 1) == picklist):
				print(val.get("title") + "\n\n" + val.get("content"))
				
	if(check == "b" or check == "B"):
		booklog.booklog()
		task.switchViewsMany()
	if(check == "j" or check == "J"):
		journal.Journal()
	if(check == "f" or check =="F"):
		friends.viewFriends()
		task.switchViewsMany()
	if(check == "p" or check == "P"):
		profile.personalProfile()
		task.switchViewsMany()
	if(check == "v" or check == "V"):
		virtues.virtues()
		task.switchViewsMany()
	if(check == "H" or check == "h"):
		habits.habittracker()
		task.switchViewsMany()
	if(check == "a" or check == "A"):
		achievements.getAchievements()
		task.switchViewsMany()
	if(check == "spec" or check == "SPEC"):
		spec.specification()
		task.switchViewsMany()
	if(check == "T" or check == "t"):
		task.start3()
		task.switchViewsMany()

