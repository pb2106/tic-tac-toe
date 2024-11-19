print("""Games:
a)tic_tac_toe
b)dots and boxes
""")
print("#TIC TAC TOE#")

j = k = 0
a,b,c,d,e,f,g,h,i="","","","","","","","",""
A = ['0','1','2','3','4','5','6','7','8']
B=[0,1,2,3,4,5,6,7,8]
while "XO"not in "".join(A):
    
    print(str(A))
    print(" _________")
    print("|",A[0],"|",A[1],"|",A[2],"|\n|",A[3],"|",A[4],"|",A[5],"|\n|",A[6],"|",A[7],"|",A[8],"|")
    if j%2==0:
        print(" --------------")
        print("\nPlayer 1's move")
    else:
        print(" --------------")
        print("\nPlayer 2's move")
    inp = int(input())
    if inp in B:
        B.remove(inp)
        if k%2==0:
            print("#1")
            print(" _________")
            A[inp] = 'X'
            print("|",A[0],"|",A[1],"|",A[2],"|\n|",A[3],"|",A[4],"|",A[5],"|\n|",A[6],"|",A[7],"|",A[8],"|")
        else:
            print("#2")
            print(" _________")
            A[inp] = 'O'
            print("|",A[0],"|",A[1],"|",A[2],"|\n|",A[3],"|",A[4],"|",A[5],"|\n|",A[6],"|",A[7],"|",A[8],"|")
        if (A[0]=='X' and A[3]=='X' and A[6]=='X') or (A[1]=='X' and A[4]=='X' and A[7]=='X') or (A[2]=='X' and A[5]=='X' and A[8]=='X') or (A[0]=='X' and A[1]=='X' and A[2]=='X') or (A[3]=='X' and A[4]=='X' and A[5]=='X') or (A[6]=='X' and A[7]=='X' and A[8]=='X') or (A[0]=='X' and A[4]=='X' and A[8]=='X') or (A[2]=='X' and A[4]=='X' and A[6]=='X'):
            print("Player 1 wins!!")
            break
        elif (A[0]=='O' and A[3]=='O' and A[6]=='O') or (A[1]=='O' and A[4]=='O' and A[7]=='O') or (A[2]=='O' and A[5]=='O' and A[8]=='O') or (A[0]=='O' and A[1]=='O' and A[2]=='O') or (A[3]=='O' and A[4]=='O' and A[5]=='O') or (A[6]=='O' and A[7]=='O' and A[8]=='O') or (A[0]=='O' and A[4]=='O' and A[8]=='O') or (A[2]=='O' and A[4]=='O' and A[6]=='O'):
            print("Player 2 wins!!")
            break
        k+=1
    else:
        print("Play a proper Move")
else:
    print("Its draw")
    

