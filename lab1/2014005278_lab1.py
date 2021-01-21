# 해당 코드는 python3.6.9에서 작성되었습니다.

def main():
    with open('input.txt', 'r') as readfile:
        # parameter는 알아서 parse 되어있을 듯 싶다.
        file_line = readfile.read().splitlines()

        parameter = str.split(file_line[0])
        line1 = file_line[1]
        line2 = file_line[2]

        match_score = int(parameter[0])
        mismatch_score = int(parameter[1])
        # indel은 아마 gap의 score
        indel_score = int(parameter[2])

        Backtrack = LCSBackTrack(match_score, mismatch_score, indel_score, line1, line2)

        # cross는 |(\의 shift)와 공백으로 표현하기
    
    with open('output.txt', 'w') as writefile:
        string2 = []
        OutputLCS(Backtrack, line1, 3, len(line1) - 1, len(line2) - 1, string2, len(line1) - 1, len(line2) - 1)
        string2 = ''.join(reversed(string2))
        match_num = string2.count('|')
        writefile.write(str(match_num) + '\n')
        
        string1 = []
        OutputLCS(Backtrack, line1, 1, len(line1) - 1, len(line2) - 1, string1, len(line1) - 1, len(line2) - 1)
        writefile.write(''.join(reversed(string1)) + "\n")
        
        writefile.write(string2 + "\n")

        string3 = []
        OutputLCS(Backtrack, line2, 2, len(line1) - 1, len(line2) - 1, string3, len(line1) - 1, len(line2) - 1)        
        writefile.write(''.join(reversed(string3)) + "\n")


def LCSBackTrack(match, mismatch, indel, line1, line2):
    S = [[0 for col in range(len(line2) + 1)] for row in range(len(line1) + 1)]
    Backtrack = [[0 for col in range(len(line2))] for row in range(len(line1))]
    S[0][0] = 0
    for i in range(1, len(line1)):
        S[i][0] = S[i-1][0] + indel
    for j in range(1, len(line2)):
        S[0][j] = S[0][j-1] + indel
    for i in range(1, len(line1) + 1):
        for j in range(1, len(line2) + 1):
            if line1[i-1] == line2[j-1]:
                temp = match
            else:
                temp = mismatch
            S[i][j] = max(S[i-1][j] + indel, S[i][j-1] + indel, S[i-1][j-1] + temp)
            if S[i][j] == S[i-1][j] + indel:
                Backtrack[i-1][j-1] = "down"
            elif S[i][j] == S[i][j-1] + indel:
                Backtrack[i-1][j-1] = "right"
            elif S[i][j] == S[i-1][j-1] + temp and line1[i-1] == line2[j-1]:
                Backtrack[i-1][j-1] = "cross_mat"
            else:
                Backtrack[i-1][j-1] = "cross_mis"
    return Backtrack

# line_num == 1 : line1
# line_num == 2 : line2
# line_num == 3 : middle '|' line
def OutputLCS(Backtrack, line, line_num, n, m, f, line1_amount, line2_amount):
    k = n
    l = m
    if k == 0 and l == 0:
        if Backtrack[k][l] == "down":
            if line_num == 2:
                f.append('-')
            elif line_num == 1:
                f.append(line[line1_amount])
            elif line_num == 3:
                f.append(' ')
        elif Backtrack[k][l] == "right":
            if line_num == 1:
                f.append('-')
            elif line_num == 2:
                f.append(line[line2_amount])
            elif line_num == 3:
                f.append(' ')
        else:

            if line_num == 1:
                f.append(line[line1_amount])
            elif line_num == 2:
                f.append(line[line2_amount])
            else:
                if Backtrack[k][l] == "cross_mat":
                    f.append('|')
                elif Backtrack[k][l] == "cross_mis":
                    f.append(' ')
        return
    if Backtrack[k][l] == "down":
        if line_num == 2:
            f.append('-')
        elif line_num == 1:
            f.append(line[line1_amount])
            line1_amount -= 1
        elif line_num == 3:
            f.append(' ')
        OutputLCS(Backtrack, line, line_num, k - 1, l, f, line1_amount, line2_amount)
    elif Backtrack[k][l] == "right":
        if line_num == 1:
            f.append('-')
        elif line_num == 2:
            f.append(line[line2_amount])
            line2_amount -= 1
        elif line_num == 3:
            f.append(' ')
        OutputLCS(Backtrack, line, line_num, k, l - 1, f, line1_amount, line2_amount)
    else:
        if line_num == 1:
            f.append(line[line1_amount])
            line1_amount -= 1
        elif line_num == 2:
            f.append(line[line2_amount])
            line2_amount -= 1
        else:
            if Backtrack[k][l] == "cross_mat":
                f.append('|')
            elif Backtrack[k][l] == "cross_mis":
                f.append(' ')
        OutputLCS(Backtrack, line, line_num, k - 1, l - 1, f, line1_amount, line2_amount)

if __name__ == "__main__":
    main()
