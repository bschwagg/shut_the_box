import random

def roll():
    return random.randint(1,6), random.randint(1,6)

def get_match(num, box, elements):
    for i, slot in enumerate(box):
        curval = sum(elements)
        # print ('checking ', slot, ' curval=', curval, elements)
        if (slot + curval) == num:
            # print ("matched ", slot)
            elements.append(slot)
            return True
        if (slot + curval) < num:
            # print ("cont with ", slot, " from slot ", i, box, elements)
            elements.append(slot)
            return get_match(num, box[i+1:], elements)
    return False

def game_done(box):
    return box == []

def simulate():
    box = list(range(9,0,-1))
    while not game_done(box):
        d1, d2 = roll()
        num = d1+d2
        # print ("rolled ", num , box)

        elements = []
        if not get_match(num, box, elements):
            # print ("Failed!")
            return False
        else:
            for i in elements:
                box.remove(i)
            # box = reverse(list( set(box) - set(elements)))
    return True


print ("starting")
trials = 100000
success = 0
for i in range(0,trials):
    # print ("sim ", i+1, " of ", trials, " (", success, " shuts!)")
    if simulate():
        success += 1

print( "Shut the box rate is ", success/trials * 100.0 )









