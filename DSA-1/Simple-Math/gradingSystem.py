# Simple program to test if and else concept

def gradingSystem(score):
    if score >= 0 and score < 25:
        return 'F'
    elif score >= 25 and score < 45:
        return 'E'
    elif score >= 45 and score < 50:
        return 'D'
    elif score >= 50 and score < 60:
        return 'C'
    elif score >= 60 and score < 80:
        return 'B'
    elif score >= 80 and score <= 100:
        return 'A'
    else:
        return "Invalid"

# NOTE: Please do not modify this function
def main():
    score = float(input())
    grade = gradingSystem(score)
    print(grade)

if __name__=="__main__":
    main()
