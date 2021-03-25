
# [SSH][OpenCV]远程图像显示

调用远程服务器进行`OpenCV`开发，想要在本地显示图像/视频，示例程序如下：

```
# 示例一
import cv2

if __name__ == '__main__':
    img = cv2.imread('box.png')
    cv2.imshow('img', img)
    cv2.waitKey(0)
# 示例二
import cv2

if __name__ == '__main__':
    source = './demo.mp4'
    display_width = 0
    display_height = 0

    cap = cv2.VideoCapture(source)

    if display_width > 0 and display_height > 0:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, display_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, display_height)
    else:
        display_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        display_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if not cap.isOpened():
        raise IOError("Video {} cannot be opened".format(source))

    output_fps = cap.get(cv2.CAP_PROP_FPS)

    print(cap)
    print(display_width, display_height)
    print(output_fps)

    while True:
        ret, frame = cap.read()
        # print(ret)
        if ret:
            cv2.imshow('cap', frame)
            cv2.waitKey(60)
        else:
            break
```

在`PyCharm`上执行命令出错：

```
qt.qpa.xcb: could not connect to display 
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "/home/zj/anaconda3/envs/zhonglian/lib/python3.7/site-packages/cv2/qt/plugins" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb, eglfs, minimal, minimalegl, offscreen, vnc, webgl.
```

在网上找了很久，发现`PyCharm`并没有使用`OpenSSH`进行远程连接，而是使用了另一款工具`JSch`。参考[How to enable X11 forwarding in PyCharm SSH session?](https://stackoverflow.com/questions/41892039/how-to-enable-x11-forwarding-in-pycharm-ssh-session)

通过另一篇文章发现可以通过`OpenSSH`进行图像显示，参考[OpenCV Development Over SSH](https://richarthurs.com/2019/01/20/raspberrypi-cv-setup/)，关键在于启动`SSH`的`X Window Forwarding`设置

1. 配置服务端`sshd_config`

        $ vim /etc/ssh/sshd_config
        $ cat /etc/ssh/sshd_config | grep X11Forward
        X11Forwarding yes
        #	X11Forwarding no

2. 重启服务端`ssh`并重新连接

        $ sudo /еtс/іnіt.d/ѕѕh rеѕtаrt
        $ ssh -X pi@192.169.1.1

这样在命令行窗口启动`OpenCV`命令即可在本地实现远程服务器的图像界面

如果要在客户端配置文件`~/.ssh/config`中进行配置，设置

```
ForwardX11 yes
```