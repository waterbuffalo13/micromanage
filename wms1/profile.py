import os
def personalProfile():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("----PERSONAL PROFILE-----")
	print("Name: Patrick")

	with open("savefiles/journallist.txt", "r") as file:
		data2 = eval(file.readline())
	journallist = data2

	with open("savefiles/test.txt", "r") as file:
		data3 = eval(file.readline())
	tasklist = data3

	#L = [int(n) for n in wellbeinglist if n]
	#ave = sum(L)/float(len(L)) if L else '-'
	#L = [int(n) for n in wellbeinglist if n]
#	ave = sum(L)/float(len(L)) if L else "-"
	#average = round(ave,0)
	total = 0
	for x in journallist:
		total += int(x.get("wellbeing"))

	#print(total)
	count = len(journallist)
	#print(count)

	wellbeingindex = round(total/count,0)


	#To be implemented
	print("Wellbeing index (-2 to 3): " + str(wellbeingindex))
	print("Inner Circle: 2")
	print("Outer Circle: 3")

	print("\n========")
	print("VIRTUES")
	print("========")
#	rationality = 0
	#for i in virtueslist:
		#rationality += i.get("value")

	#i=0
	#for x in virtueslist:
#		print(x.get("virtue")+":",x.get("value"))
#	print("Rationality :"+rationality)

	productionvalue = 0
	for x in tasklist:
		if(x.get("status") == "COMPLETE"):
			productionvalue += int(x.get("production"))
	print("Production: " + str(productionvalue))

#	print("---------------")
	#print("Rationality: ", rationality)
	#print("---------------")

