import clips

def clips_callable(f):
    def wf(*args, **kwargs):
        if f(*args, **kwargs):
            return clips.Symbol("TRUE")
        else:
            return clips.Symbol("FALSE")
    clips.RegisterPythonFunction(wf, f.__name__)

@clips_callable
def pyprint(s):
    print (s)
    print ("".join(map(str, s)))

def running_clips(info):
    clips.Load("test.clp")
    clips.Reset()
    clips.Run()

    # assert a fact.
    a = clips.Assert("(order (part-id p1) (quantity 20))")
    clips.Run()