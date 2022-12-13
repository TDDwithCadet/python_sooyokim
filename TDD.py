
class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
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



class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    # def testRunning(self):
    #     self.test.run()
    #     assert(self.test.wasRun)

    def testSetUp(self):
        self.test.run()
        assert("setUp testMethod " == self.test.log)

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)


if __name__ == '__main__':
    # test = WasRun("testMethod")
    # print(test.wasRun)
    # test.run()
    # print(test.wasRun)
    # TestCaseTest("testRunning").run()
    # TestCaseTest("testSetUp").run()
    TestCaseTest("testTemplateMethod").run()

