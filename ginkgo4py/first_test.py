from ginkgo4py import Ginkgo4Py

fixtures = "../fixtures"

def test_ginkgo4py_can_discover_test_files():
    assert Ginkgo4Py().DiscoverFrom(fixtures).Files() == ["../fixtures/test_file.py"]


def test_given_discovered_files_discover_tests():
    testFiles = Ginkgo4Py().DiscoverFrom(fixtures).Files()
    assert Ginkgo4Py().DiscoverTestNamesFrom(testFiles) == ["A first test"]