class abc:
    def f1(self,a,b):
        return a+b

def load():
#     model = abc()
#     k = model.f1(10,20)
#     return k
    return abc().f1(10,20)
