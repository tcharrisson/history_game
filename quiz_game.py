import wikipedia

print("Welcome to my computer game!")
print("Would you like to play my computer knowledge game ?..")
playing = input('please answer yes or no....! ').lower().strip()
if playing == "no":
    quit()
if playing == "yes":
    print("okay lets play!...")
while playing not in ('yes', 'no'):
    playing = input('please answer yes or no....! ').lower().strip()
    if playing == "no":
        quit()
        break
    if playing == "yes":
        print("okay lets play!...")
        break
    else:
        continue

