
def stringShift(s, shift):
    return shiftHelper(s, shift, 0)

def shiftHelper(s, shift, cidx):
    if cidx == len(shift):
        return s
    current_shif = shift[cidx]
    shift_step = current_shif[1] % len(s)
    if current_shif[0] == 0:
        # Left Shift
        left = s[:shift_step]
        rem = s[shift_step:len(s)]
        s = rem+left
        print(s)
    else:
        # Right Shift
        if shift_step != 0:
            right = s[-shift_step:]
            rem = s[0:len(s)-shift_step]
            s = right + rem
    return shiftHelper(s, shift, cidx+1)

print(stringShift("mecsk", [[1,4],[0,5],[0,4],[1,1],[1,5]]))

