def prettypercentchange(x, y):
    return round((x - y)*100/y, 1).astype(str)+'%'
def percentchange(x, y):
    try:
        return ((x - y)*100/y)
    except ZeroDivisionError:
        return 0
def percent(x, y):
    return (x/y)*100
def percentchange(x, y):
    try:
        return ((x - y)*100/y)
    except ZeroDivisionError:
        return 0
def realchange(x, y):
    return x-y
