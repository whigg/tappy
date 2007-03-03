#!/usr/bin/env python
#
# Created by: Tim Cera
#
__usage__ = """
First ensure that scipy_core modules are installed.

Build xxx:
  python setup_xxx.py build
Run tests locally:
  python tests/test_foo.py [-l<int>] [-v<int>]

Run tests if scipy is installed:
  python -c 'import scipy;scipy.xxx.test(level=<int>,verbosity=<int>)'
"""

import sys
from numpy.testing import *
import scipy as N

set_package_path()
from pad import *
del sys.path[0]


class test_nearest(ScipyTestCase):
    def check_simple(self):
        a = N.arange(100).astype('f')
        a = pad.mean(a, ((25, 20),), stat_len=((2, 3),))
        b = N.array([0.5,   0.5,   0.5,   0.5,   0.5,   0.5,   0.5,   0.5,
                     0.5,   0.5,   0.5,   0.5,   0.5,   0.5,   0.5,   0.5,
                     0.5,   0.5,   0.5,   0.5,   0.5,   0.5,   0.5,   0.5,
                     0.5,   0. ,   1. ,   2. ,   3. ,   4. ,   5. ,   6. ,
                     7. ,   8. ,   9. ,  10. ,  11. ,  12. ,  13. ,  14. ,
                    15. ,  16. ,  17. ,  18. ,  19. ,  20. ,  21. ,  22. ,
                    23. ,  24. ,  25. ,  26. ,  27. ,  28. ,  29. ,  30. ,
                    31. ,  32. ,  33. ,  34. ,  35. ,  36. ,  37. ,  38. ,
                    39. ,  40. ,  41. ,  42. ,  43. ,  44. ,  45. ,  46. ,
                    47. ,  48. ,  49. ,  50. ,  51. ,  52. ,  53. ,  54. ,
                    55. ,  56. ,  57. ,  58. ,  59. ,  60. ,  61. ,  62. ,
                    63. ,  64. ,  65. ,  66. ,  67. ,  68. ,  69. ,  70. ,
                    71. ,  72. ,  73. ,  74. ,  75. ,  76. ,  77. ,  78. ,
                    79. ,  80. ,  81. ,  82. ,  83. ,  84. ,  85. ,  86. ,
                    87. ,  88. ,  89. ,  90. ,  91. ,  92. ,  93. ,  94. ,
                    95. ,  96. ,  97. ,  98. ,  99. ,  98. ,  98. ,  98. ,
                    98. ,  98. ,  98. ,  98. ,  98. ,  98. ,  98. ,  98. ,
                    98. ,  98. ,  98. ,  98. ,  98. ,  98. ,  98. ,  98. ,
                    98. ])
        assert_array_equal(a, b)


class test_maximum(ScipyTestCase):
    def check_simple(self):
        a = N.arange(100)
        a = pad.maximum(a, (25, 20))
        b = N.array([99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
                     99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
                     99, 99, 99, 99, 99,  0,  1,  2,  3,  4,
                      5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
                      15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                      25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
                      35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
                      45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                      55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
                      65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
                      75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
                      85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
                      95, 96, 97, 98, 99, 99, 99, 99, 99, 99,
                      99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
                      99, 99, 99, 99,99])
        assert_array_equal(a, b)


class test_minimum(ScipyTestCase):
    def check_simple(self):
        a = N.arange(100)
        a = pad.minimum(a, (25, 20))
        b = N.array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                      0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                      0,  0,  0,  0,  0,  0,  1,  2,  3,  4,
                      5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
                      15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                      25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
                      35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
                      45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                      55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
                      65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
                      75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
                      85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
                      95, 96, 97, 98, 99,  0,  0,  0,  0,  0,
                       0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                       0,  0,  0,  0,  0])
        assert_array_equal(a, b)


class test_median(ScipyTestCase):
    def check_simple(self):
        a = N.arange(100).astype('f')
        a = pad.median(a, (25, 20))
        b = N.array([ 49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  
                      49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,
                      49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,
                      49.5,   0. ,   1. ,   2. ,   3. ,   4. ,   5. ,   6. ,
                       7. ,   8. ,   9. ,  10. ,  11. ,  12. ,  13. ,  14. ,
                      15. ,  16. ,  17. ,  18. ,  19. ,  20. ,  21. ,  22. ,
                      23. ,  24. ,  25. ,  26. ,  27. ,  28. ,  29. ,  30. ,
                      31. ,  32. ,  33. ,  34. ,  35. ,  36. ,  37. ,  38. ,
                      39. ,  40. ,  41. ,  42. ,  43. ,  44. ,  45. ,  46. ,
                      47. ,  48. ,  49. ,  50. ,  51. ,  52. ,  53. ,  54. ,
                      55. ,  56. ,  57. ,  58. ,  59. ,  60. ,  61. ,  62. ,
                      63. ,  64. ,  65. ,  66. ,  67. ,  68. ,  69. ,  70. ,
                      71. ,  72. ,  73. ,  74. ,  75. ,  76. ,  77. ,  78. ,
                      79. ,  80. ,  81. ,  82. ,  83. ,  84. ,  85. ,  86. ,
                      87. ,  88. ,  89. ,  90. ,  91. ,  92. ,  93. ,  94. ,
                      95. ,  96. ,  97. ,  98. ,  99. ,  49.5,  49.5,  49.5,
                      49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,
                      49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,
                      49.5])
        assert_array_equal(a, b)


class test_mean(ScipyTestCase):
    def check_simple(self, level=1):
        a = N.arange(100).astype('f')
        a = pad.mean(a, (25, 20))
        b = N.array([ 49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  
                      49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  
                      49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  
                      49.5,   0. ,   1. ,   2. ,   3. ,   4. ,   5. ,   6. ,   
                       7. ,   8. ,   9. ,  10. ,  11. ,  12. ,  13. ,  14. ,  
                      15. ,  16. ,  17. ,  18. ,  19. ,  20. ,  21. ,  22. ,  
                      23. ,  24. ,  25. ,  26. ,  27. ,  28. ,  29. ,  30. ,  
                      31. ,  32. ,  33. ,  34. ,  35. ,  36. ,  37. ,  38. ,  
                      39. ,  40. ,  41. ,  42. ,  43. ,  44. ,  45. ,  46. ,  
                      47. ,  48. ,  49. ,  50. ,  51. ,  52. ,  53. ,  54. ,  
                      55. ,  56. ,  57. ,  58. ,  59. ,  60. ,  61. ,  62. ,  
                      63. ,  64. ,  65. ,  66. ,  67. ,  68. ,  69. ,  70. ,  
                      71. ,  72. ,  73. ,  74. ,  75. ,  76. ,  77. ,  78. ,  
                      79. ,  80. ,  81. ,  82. ,  83. ,  84. ,  85. ,  86. ,  
                      87. ,  88. ,  89. ,  90. ,  91. ,  92. ,  93. ,  94. ,  
                      95. ,  96. ,  97. ,  98. ,  99. ,  49.5,  49.5,  49.5,  
                      49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  
                      49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  49.5,  
                      49.5])
        assert_array_equal(a, b)


class test_constant(ScipyTestCase):
    def check_simple(self):
        a = N.arange(100)
        a = pad.constant(a, (25, 20), (10, 20))
        b = N.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 
                     10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 
                     10, 10, 10, 10, 10,  0,  1,  2,  3,  4, 
                      5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
                     15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
                     25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 
                     35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 
                     45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 
                     55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
                     65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 
                     75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 
                     85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 
                     95, 96, 97, 98, 99, 20, 20, 20, 20, 20, 
                     20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 
                     20, 20, 20, 20, 20])
        assert_array_equal(a, b)


class test_linear_ramp(ScipyTestCase):
    def check_simple(self):
        a = N.arange(100).astype('f')
        a = pad.linear_ramp(a, (25, 20), (4, 5))
        b = N.array([  4.  ,   3.84,   3.68,   3.52,   3.36,   3.2 ,   3.04,
                       2.88,   2.72,   2.56,   2.4 ,   2.24,   2.08,   1.92,
                       1.76,   1.6 ,   1.44,   1.28,   1.12,   0.96,   0.8 ,
                       0.64,   0.48,   0.32,   0.16,   0.  ,   1.  ,   2.  ,
                       3.  ,   4.  ,   5.  ,   6.  ,   7.  ,   8.  ,   9.  ,
                      10.  ,  11.  ,  12.  ,  13.  ,  14.  ,  15.  ,  16.  ,
                      17.  ,  18.  ,  19.  ,  20.  ,  21.  ,  22.  ,  23.  ,
                      24.  ,  25.  ,  26.  ,  27.  ,  28.  ,  29.  ,  30.  ,
                      31.  ,  32.  ,  33.  ,  34.  ,  35.  ,  36.  ,  37.  ,
                      38.  ,  39.  ,  40.  ,  41.  ,  42.  ,  43.  ,  44.  ,
                      45.  ,  46.  ,  47.  ,  48.  ,  49.  ,  50.  ,  51.  ,
                      52.  ,  53.  ,  54.  ,  55.  ,  56.  ,  57.  ,  58.  ,
                      59.  ,  60.  ,  61.  ,  62.  ,  63.  ,  64.  ,  65.  ,
                      66.  ,  67.  ,  68.  ,  69.  ,  70.  ,  71.  ,  72.  ,
                      73.  ,  74.  ,  75.  ,  76.  ,  77.  ,  78.  ,  79.  ,
                      80.  ,  81.  ,  82.  ,  83.  ,  84.  ,  85.  ,  86.  ,
                      87.  ,  88.  ,  89.  ,  90.  ,  91.  ,  92.  ,  93.  ,
                      94.  ,  95.  ,  96.  ,  97.  ,  98.  ,  99.  ,  94.3 ,
                      89.6 ,  84.9 ,  80.2 ,  75.5 ,  70.8 ,  66.1 ,  61.4 ,
                      56.7 ,  52.  ,  47.3 ,  42.6 ,  37.9 ,  33.2 ,  28.5 ,
                      23.8 ,  19.1 ,  14.4 ,   9.7 ,   5.  ])
        assert_array_almost_equal(a, b, decimal=5)


class test_reflect(ScipyTestCase):
    def check_simple(self):
        a = N.arange(100)
        a = pad.reflect(a, (25, 20))
        b = N.array([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 
                     11, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0,  1,  2,
                      3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
                     17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                     31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
                     45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
                     59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                     73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
                     87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 98,
                     97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84,
                     83, 82, 81, 80, 79])
        assert_array_equal(a, b)


class test_wrap(ScipyTestCase):
    def check_simple(self):
        a = N.arange(100)
        a = pad.wrap(a, (25, 20))
        b = N.array([75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
                     89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,  0,  1,  2,
                      3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
                     17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                     31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
                     45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
                     59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                     73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
                     87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,  0,
                      1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
                     15, 16, 17, 18, 19])
        assert_array_equal(a, b)

class test_nearest_rank_2(ScipyTestCase):
    def check_simple(self):
        a = N.arange(30)
        a = N.reshape(a, (6,5))
        a = pad.mean(a, pad_width=((2,3),(3,2)), stat_len=(3,))
        b = N.array([[ 6,  6,  6,  5,  6,  7,  8,  9,  8,  8],
                     [ 6,  6,  6,  5,  6,  7,  8,  9,  8,  8],
                     [ 1,  1,  1,  0,  1,  2,  3,  4,  3,  3],
                     [ 6,  6,  6,  5,  6,  7,  8,  9,  8,  8],
                     [11, 11, 11, 10, 11, 12, 13, 14, 13, 13],
                     [16, 16, 16, 15, 16, 17, 18, 19, 18, 18],
                     [21, 21, 21, 20, 21, 22, 23, 24, 23, 23],
                     [26, 26, 26, 25, 26, 27, 28, 29, 28, 28],
                     [21, 21, 21, 20, 21, 22, 23, 24, 23, 23],
                     [21, 21, 21, 20, 21, 22, 23, 24, 23, 23],
                     [21, 21, 21, 20, 21, 22, 23, 24, 23, 23]])
        assert_array_equal(a, b)

if __name__ == "__main__":
    ScipyTest('pad').run()
