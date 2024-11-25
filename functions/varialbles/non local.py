'''#process of defining function inside the another function
def outer():
    print('outer function is stareted')
    def inner():
        print('inner is stsred')
        print('innner is end')
    inner()
    print('outer is ended')
outer()
      '''
def outer():
    a=10
    def inner():
        nonlocal a
        print(a)
        a-=5
        print(a)
    inner()
    print(a)
outer()
