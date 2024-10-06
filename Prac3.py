math = float(input("Math: "))
sci = float(input("Science: "))
eng = float(input("English: "))

if math >= 75 or sci >=75 or eng >= 75:
    print(f"Average Grade: {(math+sci+eng)/3}")
    print("Congratulations!")
    print("You passed the semester")
    if math <= 75 or sci <=75 or eng <= 75:
        print("but you need to retake the following subject(s):")
        if math <= 74:
            print("-Math")
        if sci <= 74:
            print("-Science")
        if eng <= 74:
            print("-English")