#include "gtest/gtest.h"
#include <iostream>

int sum(int a, int b) {
  return a + b;
}

TEST(TestDemo, First) {
  int res = sum(3, 5);

  EXPECT_EQ(res, 8);
}

int main(int argc, char *argv[]) {
  ::testing::InitGoogleTest(&argc, argv);
  int res = RUN_ALL_TESTS();

  std::cout << "Hello, World!" << std::endl;
  return 0;
}
