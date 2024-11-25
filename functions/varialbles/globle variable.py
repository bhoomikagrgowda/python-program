a=10#var outside function space
def display():
    global a#keyword def
    a=10#access
    print(a)
    a-=5#modify
    print(a)
display()
print(a)
#varaible can created outside the function
#access and modified inside the function
#inoder to make normal variable to global variable we use GLOBEL as a keyword
