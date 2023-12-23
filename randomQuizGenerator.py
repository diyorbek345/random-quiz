import random

capitals = {'Alabama': 'Montgomery',
            'Alaska':'Juneau',
            'Arizona':'Phoneix',          
            'Arkansas':'Little Rock',
            'California':'Sacramento',
            'Colorado':'Denver',
            'Connecticut':'Hartford',            
            'Delaware':'Dover',            
            'Florida':'Tallahassee',            
            'Georgia':'Atlanta',            
            'Hawaii':'Honolulu',
            'Idaho':'Boise',            
            'Illinois':'Springfield',
            'INdiana':'Indianapolis',            
            'Iowa':'Des Moines',
            'Kansas':'Topeka',            
            'KEnticky':'Frankfort',            
            'Lousiana':'Baton Rouge',            
            'Maine':'Augusta',
            'Maryland':'Annapolis',
            'Massachusets':'Boston',
            'Michigan':'Lansing',
            'Minnesota':'Saint Paul',
            'Missisipi':'Jackson',
            'Missouri':'Jefferson city',
            'Montana':'Helena',
            'Nebraska':'Lincoln',
            'Nevada':'Carson city',
            'New Hampshire':'Concord',
            'New Jersey':'Trenton',
            'New Mexico':'Santa Fe',
            'New York':'Albany',
            'North Carolina':'Raleigh',
            'North Dakota':'Bismarck',
            'Ohio':'Columbus',
            'Oklahoma':'Oklahoma City',
            'Origon':'Salem',
            'Pennsylvania':'Harrisburg',
            'Rhode Island':'Providence',
            'South Carolina':'Columbia',
            'South Dakota':'Pierra',
            'tennesse':'Nashville',
            'TExas':'Austin',
            'Utah':'Salt Lake City',
            'Vermont':'Montpeliar',
            'Virgina':'Richmond',
            'Washington':'Olympia',
            'West Virginia':'Charleston',
            'Wisconsin':'Madison',
            'Wyoming':'Cheyenne',
            }
for quizNum in range(35):

    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum +1), 'w')
    quizFile.write('Ism:\n\nVaqt:\n\nKurs\n\n')
    quizFile.write((' ' * 15) + 'Proverka znaniy stolit shtatov  (Bilet %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOption = wrongAnswers + [correctAnswer]
        random.shuffle(answerOption)

        quizFile.write('%s. Shtatni poytaxtini tanlang %s.\n' % (questionNum + 1, states[questionNum]))

        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOption[i]))
            quizFile.write('\n')

            answerKeyFile.write('%s. %s\n' % (questionNum + 1,'ABCD'[answerOption.index(correctAnswer)]))
    
    quizFile.close()
    answerKeyFile.close()