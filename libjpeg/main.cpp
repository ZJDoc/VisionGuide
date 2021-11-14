#include <iostream>
#include "turbojpeg.h"
#include "opencv2/opencv.hpp"

#define DEFAULT_QUALITY  95

const char *subsampName[TJ_NUMSAMP] = {
        "4:4:4", "4:2:2", "4:2:0", "Grayscale", "4:4:0", "4:1:1"
};

const char *colorspaceName[TJ_NUMCS] = {
        "RGB", "YCbCr", "GRAY", "CMYK", "YCCK"
};

bool
read_file_data(const std::string &file_path, unsigned char **jpegBuf, unsigned long &jpegSize) {
    /* Read the JPEG file into memory. */
    FILE *jpegFile = nullptr;
    long size;

    if ((jpegFile = fopen(file_path.c_str(), "rb")) == nullptr) {
        std::cout << "Error: opening input file" << std::endl;
        return EXIT_FAILURE;
    }
    if (fseek(jpegFile, 0, SEEK_END) < 0 || ((size = ftell(jpegFile)) < 0) || fseek(jpegFile, 0, SEEK_SET) < 0) {
        std::cout << "Error: determining input file size" << std::endl;
        return EXIT_FAILURE;
    }
    if (size == 0) {
        std::cout << "Error: determining input file size, Input file contains no data" << std::endl;
        return EXIT_FAILURE;
    }
    jpegSize = (unsigned long) size;
    if ((*jpegBuf = (unsigned char *) tjAlloc((int) jpegSize)) == nullptr) {
        std::cout << "Error: allocating JPEG buffer" << std::endl;
        return EXIT_FAILURE;
    }
    if (fread(*jpegBuf, jpegSize, 1, jpegFile) < 1) {
        std::cout << "Error: reading input file" << std::endl;
        return EXIT_FAILURE;
    }

    if (jpegFile) {
        fclose(jpegFile);
        jpegFile = nullptr;
    }

    return EXIT_SUCCESS;
}

bool
decompress_img_data(unsigned char **jpegBuf, const unsigned long &jpegSize, const int &pixelFormat, const int &flags,
                    unsigned char **imgBuf, int &width, int &height) {
    tjhandle tjInstance = nullptr;
    int inSubsamp, inColorspace;
    if ((tjInstance = tjInitDecompress()) == nullptr) {
        std::cout << "Error: initializing decompressor" << std::endl;
        return EXIT_FAILURE;
    }
    if (tjDecompressHeader3(tjInstance, *jpegBuf, jpegSize, &width, &height,
                            &inSubsamp, &inColorspace) < 0) {
        std::cout << "Error: reading JPEG header" << std::endl;
        return EXIT_FAILURE;
    }

    printf("%s Image:  %d x %d pixels, %s subsampling, %s colorspace\n",
           "Input", width, height, subsampName[inSubsamp], colorspaceName[inColorspace]);


    if ((*imgBuf = (unsigned char *) tjAlloc(width * height *
            tjPixelSize[pixelFormat])) == nullptr) {
        std::cout << ("Error: allocating uncompressed image buffer\n");
        return EXIT_FAILURE;
    }
    if (tjDecompress2(tjInstance, *jpegBuf, jpegSize, *imgBuf, width, 0, height,
                      pixelFormat, flags) < 0) {
        std::cout << "Error: decompressing JPEG image" << std::endl;
        return EXIT_FAILURE;
    }

    if (tjInstance) {
        tjDestroy(tjInstance);
        tjInstance = nullptr;
    }

    return EXIT_SUCCESS;
}

bool compress_img_data(unsigned char **jpegBuf, unsigned long &jpegSize,
                       unsigned char **imgBuf, const int &width, const int &height,
                       int &outQual, const int &outSubsamp, const int &pixelFormat, const int &flags) {
    /* Output image format is JPEG.  Compress the uncompressed image. */
    if (outQual < 0) {
        outQual = DEFAULT_QUALITY;
        return EXIT_FAILURE;
    }

    const char *outFormat = ".jpg";
    printf("Output Image (%s):  %d x %d pixels", outFormat, width, height);
    printf(", %s subsampling, quality = %d\n", subsampName[outSubsamp],
           outQual);

    tjhandle tjInstance = nullptr;
    if ((tjInstance = tjInitCompress()) == nullptr) {
        std::cout << ("Error: initializing compressor\n");
        return EXIT_FAILURE;
    }
    if (tjCompress2(tjInstance, *imgBuf, width, 0, height, pixelFormat,
                    jpegBuf, &jpegSize, outSubsamp, outQual, flags) < 0) {
        std::cout << ("Error: compressing image\n");
        return EXIT_FAILURE;
    }

    if (tjInstance) {
        tjDestroy(tjInstance);
        tjInstance = nullptr;
    }

    return EXIT_SUCCESS;
}

bool write_file_data(const std::string &file_path, unsigned char **jpegBuf, unsigned long &jpegSize) {
    /* Write the JPEG image to disk. */
    FILE *jpegFile = nullptr;
    if ((jpegFile = fopen(file_path.c_str(), "wb")) == nullptr) {
        std::cout << ("Error: opening output file\n");
        return EXIT_FAILURE;
    }
    if (fwrite(*jpegBuf, jpegSize, 1, jpegFile) < 1) {
        std::cout << ("Error: writing output file\n");
        return EXIT_FAILURE;
    }
    fclose(jpegFile);
    jpegFile = nullptr;

    return EXIT_SUCCESS;
}

int main() {
    /* Input image is a JPEG image.  Decompress and/or transform it. */
    std::string file_path = "lena.jpg";
    unsigned char *jpegBuf = nullptr;
    unsigned long jpegSize;
    read_file_data(file_path, &jpegBuf, jpegSize);

    //    parse file data
    unsigned char *imgBuf = nullptr;
    int width, height;
    int pixelFormat = TJPF_BGR; //TJPF_BGRX;
    int flags = TJFLAG_FASTDCT;
    decompress_img_data(&jpegBuf, jpegSize, pixelFormat, flags, &imgBuf, width, height);

    //    auto img = cv::imread("lena.jpg");
    cv::Mat img = cv::Mat::zeros(height, width, CV_8UC3);
    img.data = imgBuf;
    cv::imshow("img", img);
    cv::waitKey(0);

    /* Dynamically allocate the JPEG buffer */
    if (jpegBuf) {
        tjFree(jpegBuf);
        jpegBuf = nullptr;
    }
    jpegSize = 0;

    int outQual = 100;
    int outSubsamp = TJSAMP_444;
    compress_img_data(&jpegBuf, jpegSize,
                      &imgBuf, width, height,
                      outQual, outSubsamp, pixelFormat, flags);

    std::string dst_file_path = "lena_3.jpg";
    write_file_data(dst_file_path, &jpegBuf, jpegSize);

    if (jpegBuf) {
        tjFree(jpegBuf);
        jpegBuf = nullptr;
    }
    std::cout << "Hello, World!" << std::endl;
    return 0;
}