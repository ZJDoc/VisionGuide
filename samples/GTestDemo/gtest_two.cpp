//
// Created by zj on 2022/10/19.
//
#include "gtest/gtest.h"

int Factorial(int num) {
    int res = 1;
    for (int i = 1; i <= num; i++) {
        res *= i;
    }

    return res;
}

// Tests factorial of 0.
TEST(FactorialTest, HandlesZeroInput) { EXPECT_EQ(Factorial(0), 1); }

// Tests factorial of positive numbers.
TEST(FactorialTest, HandlesPositiveInput) {
    EXPECT_EQ(Factorial(1), 1);
    EXPECT_EQ(Factorial(2), 2);
    EXPECT_EQ(Factorial(3), 6);
    EXPECT_EQ(Factorial(8), 40320);
}
