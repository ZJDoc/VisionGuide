//
// Created by zj on 23-3-22.
//

#include "himb.h"

#include <iostream>

#include "common.h"

int HiMb::Hi(int a, int b) {
    std::cout << "Hi MB" << std::endl;

    std::cout << "a = " << a << " b = " << b << std::endl;
    auto cm = Common();
    int r = cm.a_plus_b(a, b);
    std::cout << "result: " << r << std::endl;

    return 0;
}
