def reversUserString():
    print("Enter any string od data to reverse")
    try:
        text = str(input())
        return text[::-1]
    except ValueError:
        return "That was not a valid string rerun to try again "
print(reversUserString())