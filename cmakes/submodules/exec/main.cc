//
// Created by zj on 23-3-22.
//

#include <iostream>

#include "common.h"
#include "helloma.h"
#include "himb.h"

int main(int argc, char* argv[]) {
    std::cout << "Hello main" << std::endl;

    HelloMa ma;
    ma.Hello();

    HiMb mb;
    mb.Hi(3, 4);

    Common cm;
    std::cout << cm.a_plus_b(5, -3) << std::endl;

    return 0;
}