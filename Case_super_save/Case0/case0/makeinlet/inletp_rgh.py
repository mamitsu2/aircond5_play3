import sys
import re

if __name__ == '__main__':
    before_str="""\
    sideWalls
    {
        type            empty;
    }"""
    after_str="""\
    sideWalls
    {
        type            empty;
    }
    inlet
    {
        type            zeroGradient;
    }"""
    f = open(sys.argv[1],'r')
    body = f.read()
    #print(body.replace(before_str,after_str))
    result = body.replace(before_str,after_str)
    f.close()
    with open(sys.argv[1],'w') as f:
        f.write(result)