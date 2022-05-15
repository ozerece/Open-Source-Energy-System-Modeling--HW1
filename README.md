# **Open-Source Energy System Modeling**
## Homework 1

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## License
Copyright 2022 Ece Özer

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



## Description

### Function 1 : norm_df()

- In this function, I'm normalizing the hourly domestic hot water demand of Belgium by dividing each hourly demand by the total demand (sum of all hourly demand).
- **Input data** of this function is _func1_BE_load.csv_.
- **Unittest file** of this function is _test_norm_df.py_.
- In the unittest, I'm checking the sum of each columns equals to 1 or not. If code worked properly, sum of each column should equal to 1.

### Function 2 : interpolate()

- In this function, I'm interpolating the yearly final energy demand of Belgium.
- For years 2000,2005,2010,2015,2020,2025,2030,2035,2040,2045, 2050; we have the demand data. We need to interpolate this demand for each missing year in 5-years time interval.
- **Input data** of this function is _func2_BE_fed.csv_.
- **Unittest file** of this function is _test_interpolate.py_.
- In the unittest, I calculated the difference between years in 5-years interval (eg. 2000-2005; 2005-2010; 2040-2045; 2045-2050), and added the sum of differences to first known year.
- ** For example**, let's look at time interval 2000-2005. I have demand data for 2000 and 2005, and interpolated the demand for years 2001, 2002, 2003 and 2004. To check my function, I calculated the yearly difference in this time interval (2000-2005) and added the sum of the differences in the value of 2000. If this value is equal to 2005, this means that my function is working properly.
