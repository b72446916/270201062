quit = ""
false_quit = ""
name = str(input("Please enter your name: "))
for i in name :
    print(i.upper())

while not "quit" in quit :
    false_quit += quit
    quit = str(input("Please type 'quit'if you want to quit: ")
print(false_quit)