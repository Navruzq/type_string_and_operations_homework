def main(x,y):
    """
    Given three integers, x, y, return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    s='"'+'('+str(x)+'+'+str(y)+')*2='+str((x+y)*2)+'"'
    return s
print(main(4,6))