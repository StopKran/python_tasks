# -*- coding: cp1251 -*-
# пока что без поддержки *args, **kwargs

def curry (func):
    def args_excec_generator(num, args_name):
        rez = ""
        for i in xrange(num):
            rez += args_name + "[" + str(i) + "],"
        return rez[:-1]
    
    def args_to_str(sargs):
        rez = ""
        for i in sargs:
            rez += i + ","
        return rez[:-1]
            
    def args_wrapper(*args, **kwargs):
        have_args = False
        have_kvargs = True
        var_count = func.func_code.co_argcount
        variables = func.func_code.co_varnames[:var_count]

        if len(args) >= var_count:
            cfunc = func
            return eval("cfunc(" + args_excec_generator(len(args), "args") + ")")
        else:
            cfunc = func
            new_func_args = args_to_str(variables[len(args):])
            new_func_code = "def carred_function("+ new_func_args +"): \n" + \
                            "   curred_args = args \n"  + \
                            "   curred_func = cfunc \n"  + \
                            "   return curred_func(" + \
                            args_excec_generator(len(args), "curred_args") + \
                            "," + new_func_args + ")"
            exec new_func_code in locals()
            return carred_function
    return args_wrapper

@curry
def myf(x, y):
    return x + y

myf2 = myf(1)
print myf2(2)

@curry 
def myf3(x, y, z, *args):
    rez = x + y + z
    for i in args:
        rez += i
    return rez

  
print myf3(1, 1, 1)
print myf3(1, 1, 10, 100)
myf4 = myf3(1000)
print(myf4(1, 5, 100))










    
