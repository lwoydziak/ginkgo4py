import os
import glob

__Ginkgo4PyRegistry = {}
__CurrentFile = None


class Ginkgo4Py(object):
    def DiscoverFrom(self, directory):
        class Discovered(object):
            def Files(self):
                files = None
                if os.path.exists(directory):
                    files = glob.glob(directory + "/test*.py")
                    assert len(files) == 1
                return files

        return Discovered()

    def DiscoverTestNamesFrom(self, testFiles):
        for file in testFiles:
            __CurrentFile = file
            importPathFull = str(file).lstrip("../")
            importPath = importPathFull.split('.')[0]
            importName = importPath.replace("/", ".")
            __import__(importName)

        return getListOfTestNames()


def getListOfTestNames():
    tests = []
    global __Ginkgo4PyRegistry
    for testFile in __Ginkgo4PyRegistry.keys():
        aTest = __Ginkgo4PyRegistry[testFile]
        tests.append(aTest["test_name"])
    return tests


def It(testName, theTest):
    # append to Global Map of tests
    global __Ginkgo4PyRegistry
    __Ginkgo4PyRegistry[__CurrentFile] = {
        "test_name": testName,
        "test": theTest
    }
