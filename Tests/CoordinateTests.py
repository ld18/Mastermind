
import io
import sys
import Tests.TestCases.AttemptsTest
import Tests.TestCases.EvaluatedCombinationTest
import Tests.TestCases.EvaluationTest
import Tests.TestCases.EvaluatorTest
import Tests.TestCases.GameCoordinatorTest
import Tests.TestCases.ValidatorTest

def callTestcases(sud):
    sys.stdout = text_trap
    sud.testAll()
    sys.stdout = sys.__stdout__

if __name__ == '__main__':
    text_trap = io.StringIO()
    print("Start all Testcases.\n")

    sud = Tests.TestCases.AttemptsTest.Testcases()
    callTestcases(sud)
    print("AttemptsTest -> Done")

    sud = Tests.TestCases.EvaluatedCombinationTest.Testcases()
    callTestcases(sud)
    print("EvaluatedCombinationTest -> Done")

    sud = Tests.TestCases.EvaluationTest.Testcases()
    callTestcases(sud)
    print("EvaluationTest -> Done")

    sud = Tests.TestCases.EvaluatorTest.Testcases()
    callTestcases(sud)
    print("EvaluatorTest -> Done")

    sud = Tests.TestCases.GameCoordinatorTest.Testcases()
    callTestcases(sud)
    print("GameCoordinatorTest -> Done")

    sud = Tests.TestCases.ValidatorTest.Testcases()
    callTestcases(sud)
    print("ValidatorTest -> Done")


    print("\nSucessfully tested all Testcases")

