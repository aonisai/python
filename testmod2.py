# -*- coding: utf-8 -*-

if __name__ == "___main__":

    import testmod
    testclass1 = testmod.testclass()
    testclass1.testmethod("1")

    from testmod import testclass
    testclass2 = testclass()
    testclass2.testmethod("2")