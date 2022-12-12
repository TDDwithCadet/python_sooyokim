


class TestCase:
    def __init__(self, name):
        self.name = name
    def run(self):
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)


class TestCaseTest(TestCase):
   def testRunning(self):
       test = WasRun("testMethod")
       assert(not test.wasRun)
       # test.run()
       # assert(test.wasRun)




if __name__ == '__main__':
    # test = WasRun("testMethod")
    # print(test.)
    # print(test.wasRun)
    # test.run()
    # print(test.wasRun)

    TestCaseTest("testRunning").run()

