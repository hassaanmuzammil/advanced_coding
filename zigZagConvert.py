s = "PAYPALISHIRING"

def zigZagConvert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    s_copy = s # copy string
    cn = 1   # column number
    fc = [1+i for i in range(0,100,numRows-1)] # full columns

    pattern = []

    while len(s_copy) != 0:

        if cn in fc: # full column
            x = 2 
            col = [char for char in s_copy[0:numRows]]
            if len(col) < numRows:
                for i in range(numRows-len(col)):
                    col.append('')
            cn = cn + 1
            s_copy = s_copy[numRows:]
            pattern.append(col)
        else:
            col = [] # initialize column
            for i in range(numRows):
                col.append('')

            col[-x] = s_copy[0]
            s_copy = s_copy[1:]
            cn = cn + 1
            x += 1
            pattern.append(col)

    pattern = np.array(pattern).transpose().tolist()
    #print(pattern)

    coded_s = ""
    for row in pattern:
        for r in row:
            coded_s = coded_s + r

    return coded_s

zigZagConvert(s, 4)
#returns 'PINALSIGYAHRPI'


zigZagConvert(s, 3)
#returns 'PAHNAPLSIIGYIR'
