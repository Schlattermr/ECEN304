from utils import convolve_1d
import numpy as np



def determine_sizes_Equal(studentArray,correctArray):
    if studentArray.shape != correctArray.shape:
        raise ValueError('Shapes Unequal Yours: {}, Mine: {}'.format(studentArray.shape,correctArray.shape))
    return True

def checkArrays(studentArray,correctArray):
    if studentArray.size != correctArray.size:
        if studentArray.size > correctArray.size:
            index = correctArray.size
        else:
            index = studentArray.size
    else:
        index = studentArray.size
    result = correctArray[0:index].astype(float) - studentArray[0:index].astype(float)
    result[correctArray[0:index] != 0] = result[correctArray[0:index] != 0] / correctArray[0:index][correctArray[0:index] != 0].astype(float)
    result = np.abs(result)*100
    if np.max(result) > 5:
        raise ValueError('Maximum percentage error over 5% {:.4}'.format(np.max(result)))
    if np.mean(result) > 5:
        raise ValueError('Mean percentage error over 5% {:.4}'.format(np.mean(result)))

def runTestCases(testCases, studentFunction, errorFunctions):
    passedAllTests = True
    for test in testCases:
        testCasePassed = True
        for errorFunc in errorFunctions:
            try:
                studentResult = studentFunction(test['A'],test['B'])
                errorFunc(studentResult,test['Result'])
            except ValueError as e:
                print(e, " Error in function: ", errorFunc.__name__)
                passedAllTests = False
                testCasePassed = False
        if testCasePassed:
            print(test['Name'], " has passed all test cases\n")
        else:
            print(test['Name'], " did not pass all test cases\n")
    return passedAllTests

if __name__ == "__main__":
    TestCaseA = {"Name":"unitStep",
                'A': np.array([1.0,1,1,1,0,0,0,0]),
                'B': np.array([1.0,1,1,1,0,0,0,0]),
                'Result': np.array([1.0, 2, 3, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0])}
    
    TestCaseB = {"Name":"Sine",
                'A': np.array([1,0,0,0,0,0,0,0]),
                'B': np.sin(np.arange(20)*np.pi/20),
                'Result': np.array([ 0.0, 0.15643446504023087, 0.3090169943749474, 0.45399049973954675,
                                     0.5877852522924731, 0.7071067811865476, 0.8090169943749475,
                                     0.8910065241883678, 0.9510565162951535, 0.9876883405951378,
                                     1.0, 0.9876883405951378, 0.9510565162951536, 0.8910065241883679,
                                     0.8090169943749475, 0.7071067811865476, 0.5877852522924732,
                                     0.45399049973954686, 0.3090169943749475, 0.15643446504023098,
                                     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])}  
    TestCaseC = {"Name":"Square",
                'A': np.array([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1.0]),
                'B': np.array([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0.0]),
                'Result': np.array([0, 1.0, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12,
                                    0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1, 0])} 
    
    TestCases = [TestCaseA,TestCaseB,TestCaseC]
    testFuncs = [checkArrays,determine_sizes_Equal]
    runTestCases(TestCases,convolve_1d,testFuncs)

