class Course():
    def __init__(self, name):
        self.name=name
        self.scores=[]

    def add_scores(self, s):
        return self.scores.append(s)
    
    def avg(self):
        return sum(self.scores)/len(self.scores)
    
    def info(self):
        return f'과목: {self.name}, 평균: {self.avg()}'
    
c=Course('파이썬')
c.add_scores(80)
c.add_scores(90)
print(c.info())