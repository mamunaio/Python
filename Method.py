class ClassName:
    def InstanceMethod(self):
        print("Instance Method")
    @classmethod
    def ClassMethod(cls):
        print("This is Class Method")
    @staticmethod
    def StaticMethod():
        print("This is Static Method")

v1 = ClassName()
v1.InstanceMethod()
v1.ClassMethod()
v1.StaticMethod()
ClassName.ClassMethod()
ClassName.StaticMethod()
ClassName.StaticMethod()