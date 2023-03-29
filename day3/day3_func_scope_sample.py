v_global = 1000 #전역변수 선언

def func():
    print(v_global)

func()
print(v_global)

v_global = 2000
func()

def func_ex():
    global v_global
    v_global_ 100
    print(v_global)

#LGB
#Local Global Builtin
#LEGB
#Local nonlocal Global Builin
def func_ex():
    func_outside_v = 10
    def func_inner_1():
        nonlocal func_outside_v
        pass
    def func_inner_2():
        pass
