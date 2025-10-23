class DSstudent:
    def __init__(self, stu_id, name):
        self.stu_id=stu_id
        self.name=name
    
    def show_info(self):
        print('학번: ',self.stu_id,',이름: ',self.name)

student=DSstudent(202501, '김덕성')
student.show_info()