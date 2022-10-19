
# 初级使用

## 概念

主要有两个概念：

1. 测试集：`Test Suite`
2. 测试用例：`Test`

可以存在多个测试集，每个测试集包含多个测试用例；不同测试集中的测试用例可以同名。

## 断言

`Google Test`使用断言判断测试结果是否符合条件，存在两种方式断言：

1. `ASSERT_*`：当出现致命错误时，及时停止程序；
2. `EXPECT_*`：允许测试出现失败，会完成所有测试程序。

另外，`GTest`允许在断言之后执行流操作：

```c++
ASSERT_EQ(x.size(), y.size()) << "Vectors x and y are of unequal length";

for (int i = 0; i < x.size(); ++i) {
  EXPECT_EQ(x[i], y[i]) << "Vectors x and y differ at index " << i;
}
```

## 简单测试

单元测试定义如下：

```
TEST(TestSuiteName, TestName) {
  ... test body ...
}
```

* `TEST()`宏定义了一个测试用例
* `TestSuiteName`：测试集名
* `TestName`：测试用例名

**注意：`TestSuiteName`和`TestName`的命名均不允许下划线**

```c++
// Tests factorial of 0.
TEST(FactorialTest, HandlesZeroInput) {
  EXPECT_EQ(Factorial(0), 1);
}

// Tests factorial of positive numbers.
TEST(FactorialTest, HandlesPositiveInput) {
  EXPECT_EQ(Factorial(1), 1);
  EXPECT_EQ(Factorial(2), 2);
  EXPECT_EQ(Factorial(3), 6);
  EXPECT_EQ(Factorial(8), 40320);
}
```

## Test Fixtures

如果在多个测试中使用了相同数据，可以定义`Test Fixtures`

1. 首先定义数据类，派生自`::testing::Test`，在`protected`权限下定义函数和数据成员
2. 可以在数据类的构造器或者`SetUp()`函数中赋值数据，`GTest`会在每个测试开始之前调用该函数
3. 完成操作后，可以在数据类的析构器或者`TearDown()`函数中释放相关数据

对于测试用例，定义如下：

```c++
TEST_F(TestFixtureName, TestName) {
  ... test body ...
}
```

1. 使用`TEST_F()`宏来声明`Test Fixtures`
2. `TestFixtureName`：使用数据类名
3. `TestName`：测试用例名，不允许下划线

使用示例如下：

```c++
class QueueTest : public ::testing::Test {
 protected:
  void SetUp() override {
     q1_.Enqueue(1);
     q2_.Enqueue(2);
     q2_.Enqueue(3);
  }

  // void TearDown() override {}

  Queue<int> q0_;
  Queue<int> q1_;
  Queue<int> q2_;
};

TEST_F(QueueTest, IsEmptyInitially) {
  EXPECT_EQ(q0_.size(), 0);
}

TEST_F(QueueTest, DequeueWorks) {
  int* n = q0_.Dequeue();
  EXPECT_EQ(n, nullptr);

  n = q1_.Dequeue();
  ASSERT_NE(n, nullptr);
  EXPECT_EQ(*n, 1);
  EXPECT_EQ(q1_.size(), 0);
  delete n;

  n = q2_.Dequeue();
  ASSERT_NE(n, nullptr);
  EXPECT_EQ(*n, 2);
  EXPECT_EQ(q2_.size(), 1);
  delete n;
}
```

操作流程如下：

1. `GTest`构造`QueueTest`对象`t1`
2. 使用`t1.SetUp()`初始化
3. 运行第一个测试`IsEmptyInitially`
4. 使用`TearDown()`清理数据
5. `t1`被销毁，调用析构器
6. 重复上述过程，测试第二个用例`DequeueWorks`

## 运行所有测试

`Google Test`提供了函数`RUN_ALL_TESTS()`来运行所有测试

```
...
...
int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
```

运行`main`函数，相同文件、不同文件测试均会运行

## 相关阅读

* [Googletest Primer](http://google.github.io/googletest/primer.html)
* [Assertions Reference](http://google.github.io/googletest/reference/assertions.html)
* [GoogleTest FAQ](http://google.github.io/googletest/faq.html)
* [Googletest Samples](http://google.github.io/googletest/samples.html)