import wikipedia
from datetime import date, timedelta
import random
import calendar

print("Welcome to my history game!")
print("Would you like to play my history knowledge game ?..")
playing = input('please answer yes or no....! ').lower().strip()
if playing == "no":
    quit()
if playing == "yes":
    print("okay lets play!...")
while playing not in ('yes', 'no'):
    playing = input('please answer yes or no....! ').lower().strip()
    if playing == "no":
        print('Thanks for your time, see you next time....')
        quit()
        break
    if playing == "yes":
        print("okay lets play!...")
        break
    else:
        continue
# To get a random date that we can use to gate info on wikipedia today in history, we need to generate
# a random date that wont involve the year.
question_number = 0
while question_number < 9:
    first_jan = date.today().replace(month=1, day=1)
    random_day = first_jan + timedelta(days=random.randint(0, 366 if calendar.isleap(first_jan.year) else 365))
# we have to format the date so that we can use only the month and day to search the wikipedia
# to get info about that day in history.
    formatted_date = random_day.strftime('%b, %d')
# i need to make sure that my wikipedia search does not include events that happened before 1600
    query = formatted_date + ' 1600 - 2021'
    correct_answer = wikipedia.summary(query, 8)
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our",
                           "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from",
                           "here", "when", "where", "how", "all", "any", "both", "each", "few", "more", "some", "such",
                           "no", "nor", "too", "very", "can", "will", "just"]

    print("On this day " + formatted_date + ", what event(s) happened in history between 1600 to 1900...")
    reply = input('answer.. ').lower()

    reply_list = []
    for i in reply.split():
        if i in uninteresting_words:
            pass
        else:
            reply_list += i
    print(correct_answer)
    reply_list1 = ' '.join(reply_list)
    if reply_list1 in correct_answer:
        print('correct')
    else:
        print('incorrect')
        question_number +=1
