
# [VideoWriter]保存H264/MPEG4格式MP4视频

## 实现

```
import cv2

fourcc_type = 'avc1'
# fourcc_type = 'mp4v'

output_path = 'output.mp4'


def main():
    # open camera
    vc = cv2.VideoCapture('/home/zj/test.mp4')
    if not vc.isOpened():
        print('Error: can not opencv camera')
        exit(0)

    ret, frame = vc.read()
    w = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = vc.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*fourcc_type)
    vw = cv2.VideoWriter(output_path, fourcc, fps, (w, h), True)
    while ret:
        vw.write(frame)
        ret, frame = vc.read()

        # cv2.imshow('frame', frame)
        # if cv2.waitKey(int(1 / fps * 1000)) & 0xFF == ord('q'):
        #     break
    # cv2.destroyAllWindows()
    vw.release()


if __name__ == '__main__':
    main()
```

* 使用编解码器`MPEG-4 Video (Simple Profile)`，需要设置`fourcc_type = 'mp4v'`
* 使用编解码器`H.264 (High Profile)`，需要设置`fourcc_type = 'avc1'`    

## 解析

`opencv`使用`ffmpeg`进行视频流的编解码，对于`h264`格式视频，需要额外安装`openh264`

```
  FFMPEG build includes support for H264 encoder based on the OpenH264 library.
  OpenH264 Video Codec provided by Cisco Systems, Inc.
  See https://github.com/cisco/openh264/releases for details and OpenH264 license.
  OpenH264 library should be installed separatelly. Downloaded binary file can be placed into global system path
  (System32 or SysWOW64) or near application binaries (check documentation of "LoadLibrary" Win32 function from MSDN).
  Or you can specify location of binary file via OPENH264_LIBRARY environment variable.
```

使用`conda`安装`libopenh264`库即可。参考[conda-forge / packages / openh264](https://anaconda.org/conda-forge/openh264)

```
conda install -c conda-forge openh264
```

如果无法安装成功，那么就下载该文件进行手动安装

```
pip install --use-local openh264-2.1.1-h780b84a_0.tar.bz2
```

## 相关阅读

* [OpenCV: FFMPEG: tag 0x34363268/'h264' is not supported with codec](https://stackoverflow.com/questions/52932157/opencv-ffmpeg-tag-0x34363268-h264-is-not-supported-with-codec/56723380)

* [Can you support "H264" codec? #299](https://github.com/skvark/opencv-python/issues/299)
