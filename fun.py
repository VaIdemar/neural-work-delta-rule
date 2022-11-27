def dot(f,z):
    s=0
    for i in range (len(f)):
        s=s+z[i]*f[i]
    return s

def proceed(summ,porog):
    if summ>=porog:
        return 1
    else:
        return 0