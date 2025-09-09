class Calculator:
    def addition(self, a, b):
        return a + b
    def subtraction(self, a, b):
        return a - b
    def multiplication(self, a, b):
        return a * b
    def division(self, a, b):
        if b==0:
            return "Error! Division by zero."
        return a / b
    def solution(self):
        step1=self.division(5,4)
        print("step1(5/4)=",step1)
        step2=self.subtraction(4,step1)
        print("step2(4-step1)=",step2)
        step3=self.multiplication(3,step2)
        print("step3(3*step2)=",step3)
        step4=self.multiplication(2,step3)
        print("step4(2*step3)=",step4)
        step5=self.division(3,5)
        print("step5(3/5)=",step5)
        step6=self.addition(1,step4)
        print("step6(1+step4)=",step6)
        result=self.subtraction(step6,step5)
        print("result(step6-step5)=",result)

cal=Calculator()
cal.solution()
