# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class WasRun:
    def __init__(self, name):
        self.wasRun = None
        self.name = name
    def run(self):
        # print("a")
        method = getattr(self, self.name)
        method()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = WasRun("testMethod")
    print(test.wasRun)
    test.run()
    print(test.wasRun)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
