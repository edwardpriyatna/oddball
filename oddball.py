import random

def scale_correct_input(left,right): #fucntion to know if the input for left and right scale correct or not
    left = left.split()
    left = [l for l in left if l != '']
    right = right.split()
    right = [r for r in right if r != '']
    try: #if all elements in left and right can't be turned to integer exception
        left = [int(l) for l in left]
        right = [int(r) for r in right]
        for l in left: #if there is number larger than amount of balls in left scale or there is 0 balls exception
            if l>len(ball_list)+1 :
                raise
        for r in right: #if there is number larger than amount of balls in right scale or there is 0 balls exception
            if r>len(ball_list)+1:
                raise
        if len(left)<1 or len(right)<1: #if no ball exception
            raise
        if len(left)!=len(right): #if left and right scale have different amount of balls exception
            raise
        if common_data(left,right) is True: #if there is duplicate ball exception
            raise
        if checkIfDuplicates(left)==True or checkIfDuplicates(right)==True: #if inside left list contains duplicate and for the right also
            raise
        which_scale_is_down(left,right)
        return True
    except:
        print("\ninvalid input!")
        print("\nplease ensure correct ball identifiter 1 -",len(ball_list))
        print("are entered on each pan, no duplicate balls on either or both pan")
        print("both pans should have the same number of balls and have at least one ball")
        return False

def common_data(list1, list2):# Python program to check if two lists have at-least one element common using traversal of list
    result = False
    for x in list1: # traverse in the 1st list
        for y in list2: # traverse in the 2nd list
            if x == y: # if one common
                result = True
                return result
    return result

def checkIfDuplicates(listOfElems): #Check if given list contains any duplicates
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

def which_scale_is_down(left,right):
    leftweight=0
    rightweight=0
    for ball_left in left:
        leftweight=leftweight+ball_list[ball_left-1] #need -1 because the index we enter starts from 1
    for ball_right in right:
        rightweight=rightweight+ball_list[ball_right-1]
    if leftweight>rightweight:
        print("the left scale is down")
    elif rightweight>leftweight:
        print("right scale is down")
    else:
        print("balanced")

def creatingball(): #function to create all the balls
    while True:
        try:
            ball_amount = int(input("enter the number of balls for the game:"))
            if ball_amount % 2 != 0 or ball_amount < 1:
                raise
            else:
                break
        except:
            print("enter even number and there should at least be 2 balls")
    # creating ball list containing all the balls
    global ball_list
    ball_list = []
    for i in range(ball_amount):  # creating all balls
        ball_list.append(1)
    # creating oddball
    global oddball
    oddball = random.randrange(0, len(ball_list))
    ball_list.pop(oddball)
    ball_list.insert(oddball, 2)
    return ball_list

def use_scale():
    while True:
        left = input("enter the ball identifier(s) to be placed in the left pan:")
        right = input("enter the ball identifier(s) to be placed in the right pan:")
        print('Your inputs for left:"', left, '", right:"', right,'"')
        valid = scale_correct_input(left, right)
        if valid: #if valid is true break
            break

def guess():    
    scale_usage = 0
    while True:
        print("\nyou are prompted to enter the balls")
        print("to be placed on the pans of each scale")
        print("separate each ball identifier with one minimum space")
        print("minimum space,e.g 1 2 3")

        use_scale()
        
        cont = False
        while True:
            answer = input("which is oddball or press enter to weigh again:")
            if answer == "":
                cont = True
                break
            else:
                try:
                    answer = int(answer)
                    if answer > len(ball_list) or answer <= 0:  # if answer larger than amount of balls or negative number exception
                        raise
                    break
                except:
                    print("wrong input")
                    print("please ensure correct ball identifiter 1 -", len(ball_list))
                    print("and only enter integers that are larger than 0")
                    continue
        if cont:
            continue
        else:
            if answer - 1 == oddball:
                scale_usage += 1
                print("\ncongratulations !!! scale usage count: ", scale_usage)
                break
            else:
                print("\nyour answer is not correct")
                scale_usage += 1
def main():
    while True:
        print("   welcome to Edward's oddball game you are given")
        print("   an even number of balls,labelled and among the balls")
        print("   one is heavier than the rest called oddball")
        print("\n   your goal is to find out which is the odd one")
        print("   you are given a weighing scale")
        print("\n   good luck and have fun")
        creatingball()
        guess()
        play_again = input("Do you want to play again? (press 1 to play again) ")
        if play_again == "1":
            continue
        else:
            break

if __name__ == "__main__":
   main()