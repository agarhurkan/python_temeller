
class Question : 
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
       return self.answer == answer
        

# print(q1.checkAnswer(12)) 


class Quiz : 
   
    def __init__(self,questions):
        self.questions = questions
        self.score = 0 
        self.questionIndex = 0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices :
            print("-", q)
        
        answer = int(input("Cevabinizi girin: "))
        self.guess(answer)
        question.checkAnswer(answer)
        self.loadQuestion()
        
        
        
    def guess(self, answer) :
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
            
            print("Doğru cevap verdiniz")
            
        else:
            print("Yanlış cevap verdiniz")
        self.questionIndex +=1



    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else : 
            self.displayQuestion() 
        
    def showScore(self):
        print("Dogru cevap sayiniz: ", self.score)

    def rightAnswers (self):
        self.rightAnswers = []
        print(f"Dogru verdiginiz sorular: {self.rightAnswers + 1}" )


q1 = Question("(3*16)/4",[8,12,7,14],12)
q2 = Question("(3*16)/2",[24,4,6,2],24)
q3 = Question("(3*12)/2",[12,18,14,24],18)


questions = [q1,q2,q3]

quiz = Quiz(questions)
quiz.displayQuestion()

 