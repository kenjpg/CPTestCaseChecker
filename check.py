import os

def checkcase(env):
    allfiles = os.listdir(env)
    results = []
    for file in allfiles:
        if file[-9:] == "check.txt":
            stdout_file = open(env+file, "r")
            testcase_file = open(env+file[0:-9]+".txt", "r")

            stdout_lines = stdout_file.readlines()
            testcase_lines = testcase_file.readlines()
            polish = lambda s: s.rstrip("\n").rstrip(" ")

            stdout_lines = list(map(polish, stdout_lines))
            testcase_lines = list(map(polish, testcase_lines))

            verdict = "NULL"

            for i in range(0, len(testcase_lines)):
                if (stdout_lines[i] != testcase_lines[i]):
                    verdict = "WA on line " + str(i)
                    break
                else:
                    verdict = "AC"
            results.append(file[0:-9]+".txt" + " | " + verdict)
        else:
            continue;
    return results