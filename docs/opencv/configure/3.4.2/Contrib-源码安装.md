
# [Ubuntu 16.04][Anaconda3][Python3.6]OpenCV_Contrib-3.4.2源码安装

如果要同时编译`opencv_contrib`模块，那么在`opencv`同一路径下下载`opencv_contrib`源码（**注意：要在同一版本下编译**）

    $ cd ~/<my_working_directory>
    $ git clone https://github.com/opencv/opencv.git
    $ git clone https://github.com/opencv/opencv_contrib.git
    $ cd opencv_contrib
    # 切换到3.4.2
    $ git checkout -b 3.4.2
    $ git show 3.4.2
    warning: refname '3.4.2' is ambiguous.
    tag 3.4.2
    Tagger: Alexander Alekhin <alexander.alekhin@intel.com>
    Date:   Mon Jul 2 18:34:56 2018 +0300

    OpenCV 3.4.2

    commit d4e02869454998c9af5af1a5c3392cdc0c31dd22
    Merge: 02b991a edd4514
    Author: Alexander Alekhin <alexander.a.alekhin@gmail.com>
    Date:   Mon Jul 2 10:57:26 2018 +0000

        Merge pull request #1679 from SongChiYoung:master
    $ git reset --hard d4e02869454998c9af5af1a5c3392cdc0c31dd22

在编译`opencv`源码时添加参数`OPENCV_EXTRA_MODULES_PATH`，指向`opencv_contrib/modules`即可

    $ cmake -D CMAKE_BUILD_TYPE=DEBUG -D CMAKE_INSTALL_PREFIX=../install -D BUILD_DOCS=ON -D BUILD_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D PYTHON3_EXECUTABLE=/home/zj/software/anaconda/anaconda3/envs/py36/bin/python -D PYTHON3_LIBRARY=/home/zj/software/anaconda/anaconda3/envs/py36/lib/libpython3.6m.so -D PYTHON3_INCLUDE_DIR=/home/zj/software/anaconda/anaconda3/envs/py36/include/python3.6m -D PYTHON3_NUMPY_INCLUDE_DIRS=/home/zj/software/anaconda/anaconda3/envs/py36/lib/python3.6/site-packages/numpy/core/include -D Pylint_DIR=/home/zj/software/anaconda/anaconda3/envs/py36/bin/pylint -D OPENCV_EXTRA_MODULES_PATH=/home/zj/opencv/opencv_contrib/modules ..
    ...
    ...
    -- General configuration for OpenCV 3.4.2 =====================================
    --   Version control:               3.4.2
    -- 
    --   Extra modules:
    --     Location (extra):            /home/zj/opencv/opencv_contrib/modules
    --     Version control (extra):     3.4.2
    -- 
    --   Platform:
    --     Timestamp:                   2019-02-26T11:20:33Z
    --     Host:                        Linux 4.15.0-43-generic x86_64
    --     CMake:                       3.5.1
    --     CMake generator:             Unix Makefiles
    --     CMake build tool:            /usr/bin/make
    --     Configuration:               DEBUG
    -- 
    ...
    ...
    --   OpenCV modules:
    --     To be built:                 aruco bgsegm bioinspired calib3d ccalib core datasets dnn dnn_objdetect dpm face features2d flann freetype fuzzy hfs highgui img_hash imgcodecs imgproc java_bindings_generator line_descriptor ml objdetect optflow phase_unwrapping photo plot python2 python3 python_bindings_generator reg rgbd saliency shape stereo stitching structured_light superres surface_matching text tracking ts video videoio videostab xfeatures2d ximgproc xobjdetect xphoto
    --     Disabled:                    js world
    --     Disabled by dependency:      -
    --     Unavailable:                 cnn_3dobj cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev cvv hdf java matlab ovis sfm viz
    --     Applications:                tests perf_tests examples apps
    --     Documentation:               NO
    --     Non-free algorithms:         NO
    -- 
    --   GUI: 
    --     GTK+:                        YES (ver 3.18.9)
    --       GThread :                  YES (ver 2.48.2)
    --       GtkGlExt:                  NO
    --     VTK support:                 NO
    -- 
    --   Media I/O: 
    --     ZLib:                        /home/zj/software/anaconda/anaconda3/envs/py36/lib/libz.so (ver 1.2.11)
    --     JPEG:                        /usr/lib/x86_64-linux-gnu/libjpeg.so (ver 80)
    --     WEBP:                        build (ver encoder: 0x020e)
    --     PNG:                         /usr/lib/x86_64-linux-gnu/libpng.so (ver 1.2.54)
    --     TIFF:                        /usr/lib/x86_64-linux-gnu/libtiff.so (ver 42 / 4.0.6)
    --     JPEG 2000:                   /usr/lib/x86_64-linux-gnu/libjasper.so (ver 1.900.1)
    --     OpenEXR:                     build (ver 1.7.1)
    --     HDR:                         YES
    --     SUNRASTER:                   YES
    --     PXM:                         YES
    -- 
    --   Video I/O:
    --     DC1394:                      YES (ver 2.2.4)
    --     FFMPEG:                      YES
    --       avcodec:                   YES (ver 56.60.100)
    --       avformat:                  YES (ver 56.40.101)
    --       avutil:                    YES (ver 54.31.100)
    --       swscale:                   YES (ver 3.1.101)
    --       avresample:                NO
    --     GStreamer:                   NO
    --     libv4l/libv4l2:              NO
    --     v4l/v4l2:                    linux/videodev2.h
    --     gPhoto2:                     NO
    -- 
    --   Parallel framework:            pthreads
    -- 
    --   Trace:                         YES (with Intel ITT)
    -- 
    --   Other third-party libraries:
    --     Intel IPP:                   2017.0.3 [2017.0.3]
    --            at:                   /home/zj/opencv/opencv/build/3rdparty/ippicv/ippicv_lnx
    --     Intel IPP IW:                sources (2017.0.3)
    --               at:                /home/zj/opencv/opencv/build/3rdparty/ippicv/ippiw_lnx
    --     Lapack:                      NO
    --     Eigen:                       NO
    --     Custom HAL:                  NO
    --     Protobuf:                    build (3.5.1)
    -- 
    --   OpenCL:                        YES (no extra features)
    --     Include path:                /home/zj/opencv/opencv/3rdparty/include/opencl/1.2
    --     Link libraries:              Dynamic load
    -- 
    --   Python 2:
    --     Interpreter:                 /usr/bin/python2.7 (ver 2.7.12)
    --     Libraries:                   /usr/lib/x86_64-linux-gnu/libpython2.7.so (ver 2.7.12)
    --     numpy:                       /usr/lib/python2.7/dist-packages/numpy/core/include (ver 1.11.0)
    --     packages path:               lib/python2.7/dist-packages
    -- 
    --   Python 3:
    --     Interpreter:                 /home/zj/software/anaconda/anaconda3/envs/py36/bin/python (ver 3.6.8)
    --     Libraries:                   /home/zj/software/anaconda/anaconda3/envs/py36/lib/libpython3.6m.so (ver 3.6.8)
    --     numpy:                       /home/zj/software/anaconda/anaconda3/envs/py36/lib/python3.6/site-packages/numpy/core/include (ver 1.15.4)
    --     packages path:               lib/python3.6/site-packages
    -- 
    --   Python (for build):            /usr/bin/python2.7
    --     Pylint:                      /home/zj/software/anaconda/anaconda3/envs/py36/bin/pylint (ver: 3.6.8, checks: 149)
    -- 
    --   Java:                          
    --     ant:                         NO
    --     JNI:                         NO
    --     Java wrappers:               NO
    --     Java tests:                  NO
    -- 
    --   Matlab:                        NO
    -- 
    --   Install to:                    /home/zj/opencv/opencv/install
    -- -----------------------------------------------------------------
    -- 
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /home/zj/opencv/opencv/build

    # 编译
    $ make -j8
    $ sudo make install

编译完成后修改`PKG_CONFIG_PATH`的路径

    $ pkg-config --libs opencv
    -L/home/zj/opencv/opencv/install/lib -lopencv_stitching -lopencv_superres -lopencv_videostab -lopencv_stereo -lopencv_dpm -lopencv_rgbd -lopencv_surface_matching -lopencv_xobjdetect -lopencv_aruco -lopencv_optflow -lopencv_hfs -lopencv_saliency -lopencv_xphoto -lopencv_freetype -lopencv_reg -lopencv_xfeatures2d -lopencv_shape -lopencv_bioinspired -lopencv_dnn_objdetect -lopencv_tracking -lopencv_plot -lopencv_ximgproc -lopencv_fuzzy -lopencv_ccalib -lopencv_img_hash -lopencv_face -lopencv_photo -lopencv_objdetect -lopencv_datasets -lopencv_text -lopencv_dnn -lopencv_ml -lopencv_bgsegm -lopencv_video -lopencv_line_descriptor -lopencv_structured_light -lopencv_calib3d -lopencv_features2d -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -lopencv_phase_unwrapping -lopencv_imgproc -lopencv_flann -lopencv_core

    $ pkg-config --cflags opencv
    -I/home/zj/opencv/opencv/install/include/opencv -I/home/zj/opencv/opencv/install/include

    -DOPENCV_EXTRA_
    MODULES_PATH=/home/zj/opencv/opencv_contrib/modules