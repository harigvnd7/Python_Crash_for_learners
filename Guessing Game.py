from Solution import questionanswer
from Solution import choice
Questions_prompts = [                                                                                                   #We are listing a set of questions and choices into a list. Each qn is an individual element of list
    "Which is the greatest Club competition\na)Champions League\nb)Club world cup\nc)La liga\nd)EPL\n\n",               #this element is Question_prompts[0]
    "Which is the greatest Club side ever\na)Barca(08-12)\nb)Madrid(16-18)\nc)Milan(02-04)\nd)ManUtd(06-07)\n\n",
    "Who is the greatest manager of all time\na)Pep Guardiola\nb)Sir Alex Ferguson\nc)Johan Cryuff\nd)Carlo Ancellotti\n\n"
]

Q_array = [                                                                                                             #we define a new list,whose entries are the objects who have assigned respective values from above list into the class attributes
    questionanswer(Questions_prompts[0],"a"),                                                                    #this element is Q_array[0]
    questionanswer(Questions_prompts[1],"a"),                                                                    #this element is Q_array[1]
    questionanswer(Questions_prompts[2],"c")
]

def guess(Q_array):
    score = 0
    for q in Q_array:
        answer = input(q.prompt)
        if answer == q.answer:
            score += 1

    print("You got " + str(score) + " out of " + str(len(Q_array)) + " correct!!")




Reply = choice(input("\nDo you want to play a guessing game? Y/N\n"))

if Reply.choice == "Y":
    guess(Q_array)
elif Reply.choice == "N":
    print("Come back when you want to play")
else :
    print("Invalid input")
