import os

def booklog():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("					|  READINGLIST   |\n 	 			        ===================")
	print("IN-PROGRESS")
	print("Title            | Progress  | %   | Days to finish book at current rate")
	print(" Atlas Shrugged  | (494/1054)| 46% | booksize * days - finaldays  ")
	print("PENDING")
	print("Mindfulness book\n Python book")
	print("READING LIST")
	print("1 - Add book to list")
	print("2 - Update progress")
	print("3 - Mark book as complete")
	print("4 - Add book to reading list")
	print("5 - Start book progress")
	print("6 - Delete book")