import speedtest
import math


def speed_test_bytes():
    speed_test = speedtest.Speedtest()

    download_speed = speed_test.download()
    print("Your Download speed is", convert_size(download_speed))

    upload_speed = speed_test.upload()
    print("Your Upload speed is", convert_size(upload_speed))
    return convert_size(download_speed), convert_size(upload_speed)


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
