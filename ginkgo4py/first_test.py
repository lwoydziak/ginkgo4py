import os
import glob


class Ginkgo4Py(object):
    def DiscoverFrom(self, directory):
        class Discovered(object):
            def Files(self):
                files = None
                pwd = os.getcwd()
                print(pwd)
                if os.path.exists(directory):
                    files = glob.glob(directory+"/test*.py")
                    assert len(files) == 1
                return files
        return Discovered()



def test_ginkgo4py_can_discover_test_files():
    assert Ginkgo4Py().DiscoverFrom("fixtures").Files() == ["fixtures/test_file.py"]
