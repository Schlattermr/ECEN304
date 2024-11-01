from utils import *
import numpy as np

"""
At least one period will be provided to your function, however there may be multiple periods provided.
The functions are expected to be in this format:
    calculate_fourier_coefficients(signal, time, period, n_harmonics)
        Signal: numpy array of the provided signal
        Time:   numpy array of the time steps for that signal EX: [0, .01, .02, .03 ...
        Period: The period of the given signal
        N_Harmonics: Number of harmonics to calculate for

    approximate_fourier_series(coefficients, n_harmonics, time, period):
        coefficients: Value provided by calculate_fourier_coefficients
        N_Harmonics: Number of harmonics to calculate for
        Time:   numpy array of the time steps for that signal EX: [0, .01, .02, .03 ...
        Period: The period of the given signal
"""


def get_Output(TestCase):
    out = calculate_fourier_coefficients(TestCase['Signal'],TestCase['Time'],TestCase['Period'],TestCase['n_harmonics'])
    return approximate_fourier_series(out,TestCase['n_harmonics'], TestCase['Time'],TestCase['Period'])
    

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
        print("Yours: ", studentArray, "\n Mine: ", correctArray)
        raise ValueError('Maximum percentage error over 5% {:.4}'.format(np.max(result)))
    if np.mean(result) > 5:
        raise ValueError('Mean percentage error over 5% {:.4}'.format(np.mean(result)))

def runTestCases(testCases, studentFunction, errorFunctions):
    passedAllTests = True
    for test in testCases:
        testCasePassed = True
        for errorFunc in errorFunctions:
            try:
                studentResult = studentFunction(test)
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
    sineWave = np.array([0.00000000e+00,  1.25333234e-01,  2.48689887e-01,  3.68124553e-01,
                        4.81753674e-01,  5.87785252e-01,  6.84547106e-01,  7.70513243e-01,
                        8.44327926e-01,  9.04827052e-01,  9.51056516e-01,  9.82287251e-01,
                        9.98026728e-01,  9.98026728e-01,  9.82287251e-01,  9.51056516e-01,
                        9.04827052e-01,  8.44327926e-01,  7.70513243e-01,  6.84547106e-01,
                        5.87785252e-01,  4.81753674e-01,  3.68124553e-01,  2.48689887e-01,
                        1.25333234e-01,  1.22464680e-16, -1.25333234e-01, -2.48689887e-01,
                        -3.68124553e-01, -4.81753674e-01, -5.87785252e-01, -6.84547106e-01,
                        -7.70513243e-01, -8.44327926e-01, -9.04827052e-01, -9.51056516e-01,
                        -9.82287251e-01, -9.98026728e-01, -9.98026728e-01, -9.82287251e-01,
                        -9.51056516e-01, -9.04827052e-01, -8.44327926e-01, -7.70513243e-01,
                        -6.84547106e-01, -5.87785252e-01, -4.81753674e-01, -3.68124553e-01,
                        -2.48689887e-01, -1.25333234e-01, -2.44929360e-16,  1.25333234e-01,
                        2.48689887e-01,  3.68124553e-01,  4.81753674e-01,  5.87785252e-01,
                        6.84547106e-01,  7.70513243e-01,  8.44327926e-01,  9.04827052e-01,
                        9.51056516e-01,  9.82287251e-01,  9.98026728e-01,  9.98026728e-01,
                        9.82287251e-01,  9.51056516e-01,  9.04827052e-01,  8.44327926e-01,
                        7.70513243e-01,  6.84547106e-01,  5.87785252e-01,  4.81753674e-01,
                        3.68124553e-01,  2.48689887e-01,  1.25333234e-01,  3.67394040e-16,
                        -1.25333234e-01, -2.48689887e-01, -3.68124553e-01, -4.81753674e-01,
                        -5.87785252e-01, -6.84547106e-01, -7.70513243e-01, -8.44327926e-01,
                        -9.04827052e-01, -9.51056516e-01, -9.82287251e-01, -9.98026728e-01,
                        -9.98026728e-01, -9.82287251e-01, -9.51056516e-01, -9.04827052e-01,
                        -8.44327926e-01, -7.70513243e-01, -6.84547106e-01, -5.87785252e-01,
                        -4.81753674e-01, -3.68124553e-01, -2.48689887e-01, -1.25333234e-01])
    sineTime = np.array([0.  , 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1 ,
                        0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2 , 0.21,
                        0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3 , 0.31, 0.32,
                        0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4 , 0.41, 0.42, 0.43,
                        0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5 , 0.51, 0.52, 0.53, 0.54,
                        0.55, 0.56, 0.57, 0.58, 0.59, 0.6 , 0.61, 0.62, 0.63, 0.64, 0.65,
                        0.66, 0.67, 0.68, 0.69, 0.7 , 0.71, 0.72, 0.73, 0.74, 0.75, 0.76,
                        0.77, 0.78, 0.79, 0.8 , 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87,
                        0.88, 0.89, 0.9 , 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98,
                        0.99])
    TriangleWave = np.array([2.22044605e-16,  2.00000000e-01,  4.00000000e-01,  6.00000000e-01,
                             8.00000000e-01,  1.00000000e+00,  8.00000000e-01,  6.00000000e-01,
                             4.00000000e-01,  2.00000000e-01,  2.22044605e-16, -2.00000000e-01,
                            -4.00000000e-01, -6.00000000e-01, -8.00000000e-01, -1.00000000e+00,
                            -8.00000000e-01, -6.00000000e-01, -4.00000000e-01, -2.00000000e-01,
                            -1.11022302e-16,  2.00000000e-01,  4.00000000e-01,  6.00000000e-01,
                             8.00000000e-01,  1.00000000e+00,  8.00000000e-01,  6.00000000e-01,
                             4.00000000e-01,  2.00000000e-01,  2.22044605e-16, -2.00000000e-01,
                            -4.00000000e-01, -6.00000000e-01, -8.00000000e-01, -1.00000000e+00,
                            -8.00000000e-01, -6.00000000e-01, -4.00000000e-01, -2.00000000e-01,
                            -2.22044605e-16,  2.00000000e-01,  4.00000000e-01,  6.00000000e-01,
                             8.00000000e-01,  1.00000000e+00,  8.00000000e-01,  6.00000000e-01,
                             4.00000000e-01,  2.00000000e-01,  1.55431223e-15, -2.00000000e-01,
                            -4.00000000e-01, -6.00000000e-01, -8.00000000e-01, -1.00000000e+00,
                            -8.00000000e-01, -6.00000000e-01, -4.00000000e-01, -2.00000000e-01,
                             6.66133815e-16,  2.00000000e-01,  4.00000000e-01,  6.00000000e-01,
                             8.00000000e-01,  1.00000000e+00,  8.00000000e-01,  6.00000000e-01,
                             4.00000000e-01,  2.00000000e-01, -2.77555756e-15, -2.00000000e-01,
                            -4.00000000e-01, -6.00000000e-01, -8.00000000e-01, -1.00000000e+00,
                            -8.00000000e-01, -6.00000000e-01, -4.00000000e-01, -2.00000000e-01,
                             6.66133815e-16,  2.00000000e-01,  4.00000000e-01,  6.00000000e-01,
                             8.00000000e-01,  1.00000000e+00,  8.00000000e-01,  6.00000000e-01,
                             4.00000000e-01,  2.00000000e-01,  1.99840144e-15, -2.00000000e-01,
                            -4.00000000e-01, -6.00000000e-01, -8.00000000e-01, -1.00000000e+00,
                            -8.00000000e-01, -6.00000000e-01, -4.00000000e-01, -2.00000000e-01,
                             2.22044605e-16,  2.00000000e-01,  4.00000000e-01,  6.00000000e-01,
                             8.00000000e-01,  1.00000000e+00,  8.00000000e-01,  6.00000000e-01,
                             4.00000000e-01,  2.00000000e-01, -2.55351296e-15, -2.00000000e-01,
                            -4.00000000e-01, -6.00000000e-01, -8.00000000e-01, -1.00000000e+00,
                            -8.00000000e-01, -6.00000000e-01, -4.00000000e-01, -2.00000000e-01,
                             2.22044605e-16,  2.00000000e-01,  4.00000000e-01,  6.00000000e-01,
                             8.00000000e-01,  1.00000000e+00,  8.00000000e-01,  6.00000000e-01,
                             4.00000000e-01,  2.00000000e-01, -2.22044605e-15, -2.00000000e-01,
                            -4.00000000e-01, -6.00000000e-01, -8.00000000e-01, -1.00000000e+00,
                            -8.00000000e-01, -6.00000000e-01, -4.00000000e-01, -2.00000000e-01,
                             4.44089210e-15,  2.00000000e-01,  4.00000000e-01,  6.00000000e-01,
                             8.00000000e-01,  1.00000000e+00,  8.00000000e-01,  6.00000000e-01,
                             4.00000000e-01,  2.00000000e-01,  2.22044605e-15, -2.00000000e-01,
                            -4.00000000e-01, -6.00000000e-01, -8.00000000e-01, -1.00000000e+00,
                            -8.00000000e-01, -6.00000000e-01, -4.00000000e-01, -2.00000000e-01,
                            -1.11022302e-16,  2.00000000e-01,  4.00000000e-01,  6.00000000e-01,
                             8.00000000e-01,  1.00000000e+00,  8.00000000e-01,  6.00000000e-01,
                             4.00000000e-01,  2.00000000e-01,  2.66453526e-15, -2.00000000e-01,
                            -4.00000000e-01, -6.00000000e-01, -8.00000000e-01, -1.00000000e+00,
                            -8.00000000e-01, -6.00000000e-01, -4.00000000e-01, -2.00000000e-01,
                            -2.22044605e-16,  2.00000000e-01,  4.00000000e-01,  6.00000000e-01,
                             8.00000000e-01,  1.00000000e+00,  8.00000000e-01,  6.00000000e-01,
                             4.00000000e-01,  2.00000000e-01, -1.77635684e-15, -2.00000000e-01,
                            -4.00000000e-01, -6.00000000e-01, -8.00000000e-01, -1.00000000e+00,
                            -8.00000000e-01, -6.00000000e-01, -4.00000000e-01, -2.00000000e-01])
    TriTime = np.array([0.  , 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1 ,
                        0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2 , 0.21,
                        0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3 , 0.31, 0.32,
                        0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4 , 0.41, 0.42, 0.43,
                        0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5 , 0.51, 0.52, 0.53, 0.54,
                        0.55, 0.56, 0.57, 0.58, 0.59, 0.6 , 0.61, 0.62, 0.63, 0.64, 0.65,
                        0.66, 0.67, 0.68, 0.69, 0.7 , 0.71, 0.72, 0.73, 0.74, 0.75, 0.76,
                        0.77, 0.78, 0.79, 0.8 , 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87,
                        0.88, 0.89, 0.9 , 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98,
                        0.99, 1.  , 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09,
                        1.1 , 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18, 1.19, 1.2 ,
                        1.21, 1.22, 1.23, 1.24, 1.25, 1.26, 1.27, 1.28, 1.29, 1.3 , 1.31,
                        1.32, 1.33, 1.34, 1.35, 1.36, 1.37, 1.38, 1.39, 1.4 , 1.41, 1.42,
                        1.43, 1.44, 1.45, 1.46, 1.47, 1.48, 1.49, 1.5 , 1.51, 1.52, 1.53,
                        1.54, 1.55, 1.56, 1.57, 1.58, 1.59, 1.6 , 1.61, 1.62, 1.63, 1.64,
                        1.65, 1.66, 1.67, 1.68, 1.69, 1.7 , 1.71, 1.72, 1.73, 1.74, 1.75,
                        1.76, 1.77, 1.78, 1.79, 1.8 , 1.81, 1.82, 1.83, 1.84, 1.85, 1.86,
                        1.87, 1.88, 1.89, 1.9 , 1.91, 1.92, 1.93, 1.94, 1.95, 1.96, 1.97,
                        1.98, 1.99])
    
    TestCaseA = {"Name":"Sine 1",
                'Period': 0.5,
                'n_harmonics': 1,
                'Signal': sineWave.copy(),
                'Time': sineTime.copy(),
                'Result': np.array([0.00374023 , 0.12901448 ,  0.25227386 ,  0.37157449 , 0.48503494 , 0.59086586,
                                           0.68739825 , 0.77310971 ,  0.84664854 ,  0.90685499 , 0.95277955 , 0.98369798,
                                           0.99912267 , 0.99881036 ,  0.98276598 ,  0.95124256 , 0.90473725 , 0.84398345,
                                           0.7699393  , 0.6837725  ,  0.58684198 ,  0.48067637 , 0.36694997 , 0.24745632,
                                           0.1240799  ,-0.00123357 , -0.12650781 , -0.24976719 ,-0.36906783 ,-0.48252828,
                                           -0.5883592 , -0.68489158,  -0.77060305,  -0.84414188, -0.90434832, -0.95027289,
                                           -0.98119131, -0.996616  ,  -0.99630369,  -0.98025932, -0.9487359 , -0.90223058,
                                           -0.84147678, -0.76743263,  -0.68126584,  -0.58433531, -0.4781697 , -0.36444331,
                                           -0.24494966, -0.12157324,   0.00374023,   0.12901448,  0.25227386,  0.37157449,
                                           0.48503494 , 0.59086586 ,  0.68739825 ,  0.77310971 , 0.84664854 , 0.90685499,
                                           0.95277955 , 0.98369798 ,  0.99912267 ,  0.99881036 , 0.98276598 , 0.95124256,
                                           0.90473725 , 0.84398345 ,  0.7699393  ,  0.6837725  , 0.58684198 , 0.48067637,
                                           0.36694997 , 0.24745632 ,  0.1240799  , -0.00123357 ,-0.12650781 ,-0.24976719,
                                           -0.36906783, -0.48252828,  -0.5883592 ,  -0.68489158, -0.77060305, -0.84414188,
                                           -0.90434832, -0.95027289,  -0.98119131,  -0.996616  , -0.99630369, -0.98025932,
                                           -0.9487359 , -0.90223058,  -0.84147678,  -0.76743263, -0.68126584, -0.58433531,
                                           -0.4781697 , -0.36444331,  -0.24494966,  -0.12157324])
                        }
    TestCaseB = {"Name":"Sine 2",
                 'Period': 0.5,
                 'n_harmonics': 2,
                 'Signal': sineWave.copy(),
                 'Time': sineTime.copy(),
                 'Result': np.array([ 0.00616814,  0.13121109,  0.25410114,  0.37291763,  0.48580954,  0.59102326,
                                      0.68692854 , 0.77204243 , 0.84505074 , 0.90482705 , 0.95044891 , 0.98121108,
                                      0.99663577 , 0.99647972 , 0.98073805 , 0.94964475 , 0.90366996 , 0.84351375,
                                      0.77009669 , 0.68454711 , 0.58818512 , 0.48250365 , 0.36914658 , 0.24988423,
                                      0.12658657 , 0.00119435 ,-0.12431121 ,-0.24793991 ,-0.36772469 ,-0.48175367,
                                      -0.58820181, -0.68536128, -0.77167033, -0.84573969, -0.90637626, -0.95260352,
                                      -0.98367821, -0.9991029 , -0.99863433, -0.98228725, -0.95033371, -0.90329787,
                                      -0.84194649, -0.76727524, -0.68049124, -0.58299217, -0.47634242, -0.3622467,
                                      -0.24252174, -0.11906657,  0.00616814,  0.13121109,  0.25410114,  0.37291763,
                                      0.48580954 , 0.59102326 , 0.68692854 , 0.77204243 , 0.84505074 , 0.90482705,
                                      0.95044891 , 0.98121108 , 0.99663577 , 0.99647972 , 0.98073805 , 0.94964475,
                                      0.90366996 , 0.84351375 , 0.77009669 , 0.68454711 , 0.58818512 , 0.48250365,
                                      0.36914658 , 0.24988423 , 0.12658657 , 0.00119435 ,-0.12431121 ,-0.24793991,
                                      -0.36772469, -0.48175367, -0.58820181, -0.68536128, -0.77167033, -0.84573969,
                                      -0.90637626, -0.95260352, -0.98367821, -0.9991029 , -0.99863433, -0.98228725,
                                      -0.95033371, -0.90329787, -0.84194649, -0.76727524, -0.68049124, -0.58299217,
                                      -0.47634242, -0.3622467 , -0.24252174, -0.11906657])}  
    
    TestCaseC = {"Name":"Triangle 5",
                 'Period': 0.2,
                 'n_harmonics': 5,
                 'Signal': TriangleWave.copy(),
                 'Time': TriTime.copy(),
                 'Result': np.array([3.15687576e-02,  2.09045640e-01,  3.78278228e-01,  5.96198622e-01,
                                     8.39305964e-01,  9.49305964e-01,  8.31758336e-01,  5.96198622e-01,
                                     3.88883203e-01,  2.09045640e-01,  7.91922202e-04, -2.09045640e-01,
                                     -3.90638908e-01, -5.96198622e-01, -8.29305964e-01, -9.49305964e-01,
                                     -8.44119016e-01, -5.96198622e-01, -3.56522523e-01, -1.59045640e-01,
                                     3.15687576e-02,  2.09045640e-01,  3.78278228e-01,  5.96198622e-01,
                                     8.39305964e-01,  9.49305964e-01,  8.31758336e-01,  5.96198622e-01,
                                     3.88883203e-01,  2.09045640e-01,  7.91922202e-04, -2.09045640e-01,
                                     -3.90638908e-01, -5.96198622e-01, -8.29305964e-01, -9.49305964e-01,
                                     -8.44119016e-01, -5.96198622e-01, -3.56522523e-01, -1.59045640e-01,
                                     3.15687576e-02,  2.09045640e-01,  3.78278228e-01,  5.96198622e-01,
                                     8.39305964e-01,  9.49305964e-01,  8.31758336e-01,  5.96198622e-01,
                                     3.88883203e-01,  2.09045640e-01,  7.91922202e-04, -2.09045640e-01,
                                     -3.90638908e-01, -5.96198622e-01, -8.29305964e-01, -9.49305964e-01,
                                     -8.44119016e-01, -5.96198622e-01, -3.56522523e-01, -1.59045640e-01,
                                     3.15687576e-02,  2.09045640e-01,  3.78278228e-01,  5.96198622e-01,
                                     8.39305964e-01,  9.49305964e-01,  8.31758336e-01,  5.96198622e-01,
                                     3.88883203e-01,  2.09045640e-01,  7.91922202e-04, -2.09045640e-01,
                                     -3.90638908e-01, -5.96198622e-01, -8.29305964e-01, -9.49305964e-01,
                                     -8.44119016e-01, -5.96198622e-01, -3.56522523e-01, -1.59045640e-01,
                                     3.15687576e-02,  2.09045640e-01,  3.78278228e-01,  5.96198622e-01,
                                     8.39305964e-01,  9.49305964e-01,  8.31758336e-01,  5.96198622e-01,
                                     3.88883203e-01,  2.09045640e-01,  7.91922202e-04, -2.09045640e-01,
                                     -3.90638908e-01, -5.96198622e-01, -8.29305964e-01, -9.49305964e-01,
                                     -8.44119016e-01, -5.96198622e-01, -3.56522523e-01, -1.59045640e-01,
                                     3.15687576e-02,  2.09045640e-01,  3.78278228e-01,  5.96198622e-01,
                                     8.39305964e-01,  9.49305964e-01,  8.31758336e-01,  5.96198622e-01,
                                     3.88883203e-01,  2.09045640e-01,  7.91922202e-04, -2.09045640e-01,
                                     -3.90638908e-01, -5.96198622e-01, -8.29305964e-01, -9.49305964e-01,
                                     -8.44119016e-01, -5.96198622e-01, -3.56522523e-01, -1.59045640e-01,
                                     3.15687576e-02,  2.09045640e-01,  3.78278228e-01,  5.96198622e-01,
                                     8.39305964e-01,  9.49305964e-01,  8.31758336e-01,  5.96198622e-01,
                                     3.88883203e-01,  2.09045640e-01,  7.91922202e-04, -2.09045640e-01,
                                     -3.90638908e-01, -5.96198622e-01, -8.29305964e-01, -9.49305964e-01,
                                     -8.44119016e-01, -5.96198622e-01, -3.56522523e-01, -1.59045640e-01,
                                     3.15687576e-02,  2.09045640e-01,  3.78278228e-01,  5.96198622e-01,
                                     8.39305964e-01,  9.49305964e-01,  8.31758336e-01,  5.96198622e-01,
                                     3.88883203e-01,  2.09045640e-01,  7.91922202e-04, -2.09045640e-01,
                                     -3.90638908e-01, -5.96198622e-01, -8.29305964e-01, -9.49305964e-01,
                                     -8.44119016e-01, -5.96198622e-01, -3.56522523e-01, -1.59045640e-01,
                                     3.15687576e-02,  2.09045640e-01,  3.78278228e-01,  5.96198622e-01,
                                     8.39305964e-01,  9.49305964e-01,  8.31758336e-01,  5.96198622e-01,
                                     3.88883203e-01,  2.09045640e-01,  7.91922202e-04, -2.09045640e-01,
                                     -3.90638908e-01, -5.96198622e-01, -8.29305964e-01, -9.49305964e-01,
                                     -8.44119016e-01, -5.96198622e-01, -3.56522523e-01, -1.59045640e-01,
                                     3.15687576e-02,  2.09045640e-01,  3.78278228e-01,  5.96198622e-01,
                                     8.39305964e-01,  9.49305964e-01,  8.31758336e-01,  5.96198622e-01,
                                     3.88883203e-01,  2.09045640e-01,  7.91922202e-04, -2.09045640e-01,
                                     -3.90638908e-01, -5.96198622e-01, -8.29305964e-01, -9.49305964e-01,
                                     -8.44119016e-01, -5.96198622e-01, -3.56522523e-01, -1.59045640e-01])}  
    TestCaseD = {"Name":"Triangle 10",
                 'Period': 0.2,
                 'n_harmonics': 10,
                 'Signal': TriangleWave.copy(),
                 'Time': TriTime.copy(),
                 'Result': np.array([-0.005,  0.205,  0.395,  0.605,  0.795,  1.005,  0.795,  0.605,
                                      0.395,  0.205, -0.005, -0.195, -0.405, -0.595, -0.805, -0.995,
                                     -0.805, -0.595, -0.405, -0.095, -0.005,  0.205,  0.395,  0.605,
                                      0.795,  1.005,  0.795,  0.605,  0.395,  0.205, -0.005, -0.195,
                                     -0.405, -0.595, -0.805, -0.995, -0.805, -0.595, -0.405, -0.095,
                                     -0.005,  0.205,  0.395,  0.605,  0.795,  1.005,  0.795,  0.605,
                                      0.395,  0.205, -0.005, -0.195, -0.405, -0.595, -0.805, -0.995,
                                     -0.805, -0.595, -0.405, -0.095, -0.005,  0.205,  0.395,  0.605,
                                      0.795,  1.005,  0.795,  0.605,  0.395,  0.205, -0.005, -0.195,
                                     -0.405, -0.595, -0.805, -0.995, -0.805, -0.595, -0.405, -0.095,
                                     -0.005,  0.205,  0.395,  0.605,  0.795,  1.005,  0.795,  0.605,
                                      0.395,  0.205, -0.005, -0.195, -0.405, -0.595, -0.805, -0.995,
                                     -0.805, -0.595, -0.405, -0.095, -0.005,  0.205,  0.395,  0.605,
                                      0.795,  1.005,  0.795,  0.605,  0.395,  0.205, -0.005, -0.195,
                                     -0.405, -0.595, -0.805, -0.995, -0.805, -0.595, -0.405, -0.095,
                                     -0.005,  0.205,  0.395,  0.605,  0.795,  1.005,  0.795,  0.605,
                                      0.395,  0.205, -0.005, -0.195, -0.405, -0.595, -0.805, -0.995,
                                     -0.805, -0.595, -0.405, -0.095, -0.005,  0.205,  0.395,  0.605,
                                      0.795,  1.005,  0.795,  0.605,  0.395,  0.205, -0.005, -0.195,
                                     -0.405, -0.595, -0.805, -0.995, -0.805, -0.595, -0.405, -0.095,
                                     -0.005,  0.205,  0.395,  0.605,  0.795,  1.005,  0.795,  0.605,
                                      0.395,  0.205, -0.005, -0.195, -0.405, -0.595, -0.805, -0.995,
                                     -0.805, -0.595, -0.405, -0.095, -0.005,  0.205,  0.395,  0.605,
                                      0.795,  1.005,  0.795,  0.605,  0.395,  0.205, -0.005, -0.195,
                                     -0.405, -0.595, -0.805, -0.995, -0.805, -0.595, -0.405, -0.095])}  
    
    
    TestCases = [TestCaseA,TestCaseB,TestCaseC,TestCaseD]
    testFuncs = [checkArrays,determine_sizes_Equal]
    runTestCases(TestCases,get_Output,testFuncs)

