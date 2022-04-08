def main():
	# write your code here

 time = input("Enter a number from 1 to 12: ")
 items = input("Enter a noun (plural): ")
 name = input("Enter a name: ")
 scream = input("Enter any sentence:  ")
 action = input("Enter a verb: ")
 
 story = f" It was {time} O'clock when I heard a knock at the door. I opened the door and there was a box full of {items} with a note saying From Mr. {name.title()}. Just as I closed the door I heard a scream {scream.upper()} I froze in place and all I could do was {action}."

 print(story)

if __name__ == '__main__':
	main()