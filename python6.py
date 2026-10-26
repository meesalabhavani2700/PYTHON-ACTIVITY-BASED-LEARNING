key = "ABCD"
answers = input("Enter answers (use - for blank): ").upper()

if len(answers) != len(key):
    print("Invalid answer length")
else:
    correct = 0
    wrong = 0
    blank = 0

    for i in range(len(key)):
        if answers[i] == "-":
            blank += 1
        elif answers[i] == key[i]:
            correct += 1
        else:
            wrong += 1

    score = correct - wrong * 0.25

    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Unanswered:", blank)
    print("Final score:", score)