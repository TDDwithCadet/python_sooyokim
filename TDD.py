
class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()

    def tearDown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)
    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
        self.log = "setUp "
    def tearDown(self):
        self.log = self.log + "tearDown "

    def testBrokenMethod(self):
        raise Exception



class TestCaseTest(TestCase):
    def setUp(self):
        # self.test = WasRun("testMethod")
        self.result = TestResult()

    # def testRunning(self):
    #     self.test.run()
    #     assert(self.test.wasRun)

    def testSetUp(self):
        self.test.run()
        assert("setUp testMethod " == self.test.log)

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        # result = TestResult()
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        # result = TestResult()
        # test.run(result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        # result = TestResult()
        # test.run()
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedResultFormatting(self):
        # result = TestResult()
        self.result.testStarted()
        self.result.testFail()
        assert("1 run, 1 failed" == self.result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        # result = suite.run()
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())


class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0
    def testFailed(self):
        self.failureCount = self.failureCount + 1
    def testStarted(self):
        self.runCount = self.runCount + 1
    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.failureCount)

class TestSuite:
    def __init__(self):
        self.tests = []
    def add(self, test):
        self.tests.append(test)
    def run(self, result):
        for test in self.tests:
            test.run(result)

if __name__ == '__main__':
    suite = TestSuite()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testResult"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testSuite"))
    result = TestResult()
    suite.run(result)
    print(result.summary())

    # test = WasRun("testMethod")
    # print(test.wasRun)
    # test.run()
    # print(test.wasRun)
    # TestCaseTest("testRunning").run()
    # TestCaseTest("testSetUp").run()
    # TestCaseTest("testTemplateMethod").run()
    # TestCaseTest("TestResult").run()


