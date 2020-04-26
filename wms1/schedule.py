import os
import datetime
import booklog
import friends
import habits
import profile
import virtues
import achievements
import spec
import task
import journal
import schedule

now = datetime.datetime.now()
day = (now.day)

months = ["Unknown", "January", "Febuary", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]
month = (months[now.month])
def sched():
	suffix = ""

	if 4 <= day <= 20 or 24 <= day <= 30:
		suffix = "th"
	else:
		suffix = ["st", "nd", "rd"][day % 10 - 1]
	
	currdate = datetime.datetime(now.year, now.month, now.day)
	
#items consist of (time stamp, startt, finisht, time,
	os.system('cls' if os.name == 'nt' else 'clear')
	with open("savefiles/schedule.txt", "r") as file:
		data2 = eval(file.readline())
	schedulelist=data2
	print("Welcome to your schedule! \nThe current date is: " + now.strftime("%d" +suffix +" "+ month+" %Y | %A %H:%M"))
	print("=========================================\n")
	for x in schedulelist:
		if(x.get("timestamp") == currdate):
			print(x.get("start time")+"-"+x.get("end time")+"| "+x.get("schedule"))
	
	if(len(schedulelist) == 0):
		print("Your schedule is currently empty")
	print("")	
	print("1 - Add item to schedule")
	print("2 - Remove an item")
		
	print("")
	print("Switch views")
	print(" (A)chievements log | (D)iet Planner   |")
	print(" (H)abits tracker   | (F)riends        | (T)odo")
	print(" (J)ournal          | (P)rofile")
	choice = input("what do you want to do?")
	if(choice == "1"):
		with open("savefiles/schedule.txt", "r") as file:
			data2 = eval(file.readline())
		schedulelist=data2
		
		os.system('cls' if os.name == 'nt' else 'clear')
		
		schedule = input("What is the name of the task you would like to add? \n")
		btime = input("what time does the task begin")
		etime = input("when does the task end")
		time = datetime.datetime(now.year, now.month, now.day)
		comb = {"timestamp":time, "schedule": schedule, "start time" : btime, "end time" : etime} 
		print(comb)
		schedulelist.append(dict(comb))

#		os.system('cls' if os.name == 'nt' else 'clear')
		with open("savefiles/schedule.txt", "w") as file:
			file.write(str(schedulelist))
		sched()
	if(choice == "2"):
		with open("savefiles/schedule.txt", "r") as file:
			data2 = eval(file.readline())
		schedulelist=data2
		for x in schedulelist:
			print(str(schedulelist.index(x) + 1), x.get("timestamp"),x.get("start time"), x.get("end time"), x.get("schedule"))
		print("DELETE A TASK")
		print("==============")
		delete= input("which task would you like to delete\n")
		del schedulelist[int(delete) - 1]
		os.system('cls' if os.name == 'nt' else 'clear')
		with open("savefiles/schedule.txt", "w") as file:
			file.write(str(schedulelist))
	
	if(choice == "b" or choice == "B"):
		booklog.booklog()
		task.switchViewsMany()
	if(choice == "j" or choice == "J"):
		journal.Journal()
	if(choice == "f" or choice =="F"):
		friends.viewFriends()
		task.switchViewsMany()
	if(choice == "p" or choice == "P"):
		profile.personalProfile()
		task.switchViewsMany()
	if(choice == "v" or choice == "V"):
		virtues.virtues()
		task.switchViewsMany()
	if(choice == "H" or choice == "h"):
		habits.habittracker()
		task.switchViewsMany()
	if(choice == "a" or choice == "A"):
		achievements.getAchievements()
		task.switchViewsMany()
	if(choice == "spec" or choice == "SPEC"):
		spec.specification()
		task.switchViewsMany()
	if(choice == "T" or choice == "t"):
		task.start3()
		task.switchViewsMany()
		sched()	