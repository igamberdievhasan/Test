from sol_sleepin import sol_sleep_in
from user_sleep_in import sleep_in

user = "user_sleep_in.py"


def main(name):
    with open(name + ".log", "r+") as input:
        with open("user_" + name + ".py", "w") as output:
            read = input.readlines()
            input.seek(0)
            for line in read:
                if "!python -m test_codebat.sleep_in.py" not in line:
                    output.write(line)
                    input.write(line)
            input.truncate()
    test(name)


def test(name):


    testCases1 = ["False", "False"]
    testCases2 = ["True", "False"]
    testCases3 = ["False", "True"]

    result1 = sleep_in(testCases1[0], testCases1[1])
    actual1 = sol_sleep_in(testCases1[0], testCases1[1])

    if (result1 == actual1):
        print("Correct")

    else:
        print("not")


    result2 = sleep_in(True,False)
    actual2 = sol_sleep_in(True,False)

    if result2 == actual2:
        print(result2)
        print("Correct")

    else:
        print("not")



if __name__ == '__main__':
    main("sleep_in")
