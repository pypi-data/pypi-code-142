print(40*'*')
print('testing location \n')
import sys,math
import unittest



sys.path.append('/media/henskyconsulting/easystore/Hensky/Projects/2022twitloccan/cannuckfind')
from cannuckfind import geolocation


class test_unknownC(unittest.TestCase):
    """
    Test unknownC
    """
    def test_unknownC(self):
        from cannuckfind import geolocation
        testloc = geolocation.unknownC()
        print("Start unKnowC test in canuckfind")
        # print(dir(testloc))
        print(testloc)
        self.assertTrue(testloc.MX == 106)

print('*** test cannuckfind geolocation complete')
print(40*'*')       


if __name__ == '__main__':
    unittest.main()



print(40*'*')


