
class TestCaseTest(TestCase):
   def testRunning(self):
       test = WasRun("testMethod")
       assert(not test.wasRun)
       test.run()
       assert(test.wasRun)
TestCaseTest("testRunning").run()



if __name__ == '__main__':
    test = TestCaseTest("testCase")
    print(test.wasRun)
    test.run()
    print(test.wasRun)