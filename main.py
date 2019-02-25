import json
import random
import matplotlib.pyplot as plt
from validate_email import validate_email

with open('info.json') as f:
    data = json.load(f)

patterns = data['patterns']


class resultGraph:

    def resultOut(self, right, wrong):
        marks = 0
        totalmarks = 0
        print('\n\n' + patterns['u2'] + "RESULTS" + patterns['u2'])
        print('Number of Questions:' + str(10))
        print('Right:' + str(len(right)) + '\n' 'Wrong:' + str(len(wrong)))
        for i in right:
            marks += int(i[1])
        for i in wrong:
            totalmarks += int(i[1])
        totalmarks += marks

        print("\nMARKS SCORED:" + str(marks) + '/' + str(totalmarks))
        self.graphit(right, wrong)

    def graphit(self, right, wrong):
        plotx = []
        ploty = []
        plotter = right + wrong
        for i in range(0, len(plotter)):
            for j in range(0, len(plotter) - i - 1):
                if plotter[j][0] > plotter[j+1][0]:
                    temp = plotter[j][0]
                    plotter[j][0] = plotter[j+1][0]
                    plotter[j+1][0] = temp
        for i in plotter:
            plotx.append(i[0])
        for i in plotter:
            ploty.append(i[1])
        plt.xlabel('QUESTIONS')
        plt.ylabel('MARKS')
        plt.title('Game Of Codes // Akshat Pande')
        plt.xticks(plotx)
        plt.plot(plotx, ploty)
        plt.show()


class assessment(resultGraph):
    question = 0
    questionCount = 0
    right = []
    wrong = []
    level = 1
    ino = 0
    difficulty = [{
        "0": "easy", "ques": []},
        {"1": "medium", "ques": []},
        {"2": "hard", "ques": []
         }]

    def __init__(self, name, email):
        element = data['company']
        print(element['WelcomeMessage'] + name +
              '!!\n' + 'Email:' + email + '\n\n')
        print(patterns['u2'] +
              element['CompanyName'] + patterns['u2'] + '\n')
        self.menu()

    def menu(self):
        element = data['menu']
        print(element['heading'] + '\n' + patterns['u1'] + '\n')
        for i in range(0, 4):
            print(str(i+1) + '-' + element['items'][i]['item'])

    def questions(self, level):
        element = data['questions']
        self.difficulty[level]['ques'].append(self.ino)

        if self.questionCount != 0:
            self.ino = self.randomgen(level)

        print('\n' + element[level]
              [self.difficulty[level][str(level)]][self.ino]['q']['question'])
        print('[' + element[level]['marks'] + ' Marks]\n')

        for i in range(0, 4):
            print(str(i+1) + '-' + element[level]
                  [self.difficulty[level][str(level)]][self.ino]['q']['options'][i]['option'])

        ans = input('\n Enter Anwer Number')
        if int(ans) > 4:
            print("\nChoice Out of Bounds")
            exit()
        self.questionCount += 1
        self.checkAns(self.level, ans)

    def checkAns(self, level, answer):
        if(str(data['questions'][level][self.difficulty[level][str(level)]][self.ino]['q']['answer']) == str(data['questions'][level]
                                                                                                             [self.difficulty[level][str(level)]][self.ino]['q']['options'][int(int(answer) - 1)]['option'])):

            print('\n\n' + data['dialogues']['d2'])
            if self.level < 2:
                self.level += 1
            print(self.level)
            self.right.append(
                [self.questionCount, data['questions'][level]['marks']])

        else:
            print('\n\n' + data['dialogues']['d3'])
            if self.level > 0:
                self.level -= 1
            print(self.level)
            self.wrong.append(
                [self.questionCount, data['questions'][level]['marks']])
        if self.questionCount != 10:
            self.questions(self.level)
        else:
            result = resultGraph()
            result.resultOut(self.right, self.wrong)

    def randomgen(self, level):
        if level == 2:
            x = random.randint(0, 9)
            while x in self.difficulty[level]['ques']:
                x = random.randint(0, 9)
            return x

        elif level != 2:
            x = random.randint(0, 9)
            while x in self.difficulty[level]['ques']:
                x = random.randint(0, 19)
            return x


class home(assessment):

    def author(self):
        print('\n' + data['author'] + '\n')

    def rules(self):
        for i in range(0, 5):
            print('\n' + str(i+1) + '-' + data['rules'][i]['rule'] + '\n')

    def checkMenu(self):
        n = int(input('\n' + "Enter Your Choice:"))
        if n == 1:
            self.questions(user.level)

        elif n == 2:
            self.rules()
            self.menu()
            self.checkMenu()

        elif n == 3:
            self.author()
            self.menu()
            self.checkMenu()

        elif n == 4:
            exit(0)


name = str(input("Enter Your Name:"))
email = str(input("Enter Your Email:"))
if validate_email(email):
    pass
else:
    print('INVALID EMAIL')
    exit()
user = home(name, email)
user.checkMenu()
