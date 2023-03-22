//
// Created by zj on 23-3-22.
//

#include <iostream>

#include "../libs/ma/helloma.h"
#include "../libs/mb/himb.h"

int main(int argc, char* argv[]) {
    std::cout << "Hello main" << std::endl;

    HelloMa ma;
    ma.Hello();

    HiMb mb;
    mb.Hi(3, 4);

    return 0;
}