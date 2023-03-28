class Method():
    stack = []
    change=0
    postfix = []
    top = -1
    operation = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3,
    }

    def push(self,e):
        self.stack.append(e)
    def push_post(self,e):
        self.postfix.append(e)


    def Chackop(self,e):
        if e == ")" and self.change!=0:
            self.push(e)
            self.top = 0
        elif e == "(" and self.change!=1:
            self.push(e)
            self.top = 0
        elif self.operation[e] >= self.top :
            self.push(e)
            self.top=self.operation[e]
        elif self.operation[e] < self.top:
            self.postfix.append(self.stack.pop())
            self.top=self.operation[e]
            self.push(e)
    def Chack(self,p):
        if ord(p)>=65 and ord(p)<=122 and p!='^':
            self.push_post(p)
        elif p in ['+','-','*','/','^','%',"("] and self.change!=1:
            self.Chackop(p)
        elif p in ['+','-','*','/','^','%',")"] and self.change==1:
            self.Chackop(p)
        elif p == ")" and self.change==0:
            while "(" in self.stack :
                self.push_post(self.stack.pop())
            self.top=0
            if self.stack!=[]:
                e=self.stack.pop()
                self.top=self.operation[e]
                self.push(e)
        elif p == "(" and self.change==1:
            while ")" in self.stack:
                self.push_post(self.stack.pop())
            self.top = 0
            if self.stack != []:
                e = self.stack.pop()
                self.top = self.operation[e]
                self.push(e)

    def Posi(self):
        for i in range(len(self.postfix)):
            if '(' in self.postfix:
                self.postfix.remove('(')
            if ')' in self.postfix:
                self.postfix.remove(')')
    def pop_all(self):
        for i in range(len(self.stack)):
            self.push_post(self.stack.pop())


    def PreFix(self,x):
        self.change=1
        px=list(x)
        px.reverse()
        for i in px:
            m.Chack(i)
        m.pop_all()
        ppr = ""
        self.Posi()
        pos = self.postfix
        self.postfix=[]
        pos.reverse()
        for i in pos:
            ppr+=i
        return ppr
    def PostFix(self,x):
        self.change=0
        for i in x:
            m.Chack(i)
        m.pop_all()
        pps = ""
        self.Posi()
        for i in self.postfix:
            pps += i
        self.postfix=[]
        return pps
    def print(self,x):
        ss=str(self.stack)
        print(f"Stack : {ss}")
        print(f"PostFix : {self.PostFix(x)}")
        print(f"PreFix : {self.PreFix(x)}")

m=Method()

x=input("Enter The Operation : ")
print(m.PostFix(x))
print(m.PreFix(x))
m.print(x)