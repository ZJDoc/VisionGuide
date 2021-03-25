
# [c++11]weak_ptr

参考：[How to: Create and Use weak_ptr Instances](https://docs.microsoft.com/en-us/cpp/cpp/how-to-create-and-use-weak-ptr-instances?view=vs-2019)

`weak_ptr`是为了避免`shared_ptr`出现循环引用（`cyclic reference`）问题而设计的

`weak_ptr`实例本身不拥有内存资源，它只能指向`shared_ptr`实例保存的共享资源，所以本身不参与引用计数，因此它不能防止引用计数变为零。使用`weak_ptr`实例时，需要先转换成`shared_ptr`实例，再进行访问；当引用计数为`0`时，内存会被删除，此时调用`weak_ptr`有可能会引发`bad_weak_ptr`异常

*`weak_ptr`类似于`Java`的弱引用，一方面能够保证避免循环引用问题，另一方面能够保证资源及时销毁，避免内存泄漏*

## 成员函数

* [expired](http://www.cplusplus.com/reference/memory/weak_ptr/expired/)：是否`weak_ptr`对象为空或者和它相关的`shared_ptr`对象不存在
* [lock](http://www.cplusplus.com/reference/memory/weak_ptr/lock/)：返回一个`shared_ptr`对象，如果`weak_ptr`已经失效（`expired`），返回一个空指针的`shared_ptr`
* [use_count](http://www.cplusplus.com/reference/memory/weak_ptr/use_count/)：`weak_ptr`对象所属的`shared_ptr`的引用计数
* [reset](http://www.cplusplus.com/reference/memory/weak_ptr/reset/)：设置`weak_ptr`对象为空
* [swap](http://www.cplusplus.com/reference/memory/weak_ptr/swap/)：交换两个`weak_ptr`对象的内容，包括所属组

## 创建

```
template<typename T>
struct array_deleter {
    void operator()(T const *p) {
        delete[] p;
    }
};

int main() {
    // 创建整型数组
    std::shared_ptr<int> ints(new int[10], array_deleter<int>());
    for (int i = 0; i < 5; i++) {
        ints.get()[i] = i;
    }

    // 创建weak_ptr
    std::weak_ptr<int> wints(ints);

    cout << wints.use_count() << endl;
    cout << wints.expired() << endl;

    auto sptr = wints.lock();
    for (int i = 0; i < 5; i++) {
        cout << sptr.get()[i] << endl;
    }
}
```