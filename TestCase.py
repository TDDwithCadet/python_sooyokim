
class TestCase:
    def __init__(self, name):
        self.name = name
    def run(self):
        method = getattr(self, self.name)
        method()

class TestCaseTest(TestCase):
   def testRunning(self):
       test = WasRun("testMethod")
       assert(not test.wasRun)
       test.run()
       assert(test.wasRun)
TestCaseTest("testRunning").run()


if __name__ == '__main__':
    test = TestCase("testCase")
    print(test.wasRun)
    test.run()
    print(test.wasRun)