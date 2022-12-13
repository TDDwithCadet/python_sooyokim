
class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)
    def testMethod(self):
        self.wasRun = 1
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)
       # test = WasRun("testMethod")
       # print(test.wasRun)
       # assert(not test.wasRun)
       # test.run()
       # print(test.wasRun)
       # assert(self.test.wasRun)
       # print("complete")

    def testSetUp(self):
        # test = WasRun("testMethod")
        self.test.run()
        assert(self.test.wasSetUp)





if __name__ == '__main__':
    # test = WasRun("testMethod")
    # print(test.wasRun)
    # test.run()
    # print(test.wasRun)

    TestCaseTest("testRunning").run()
    TestCaseTest("testSetUp").run()

