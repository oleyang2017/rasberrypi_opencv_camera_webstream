# rasberrypi_opencv_camera_webstream
这是一个用Raspberry Pi + Pi camera + opencv

requestment:
opencv
Flask
picamera
six
wget
tensorflow

####### Install tensorflow #######
# For Python 2.7
wget https://github.com/samjabrahams/tensorflow-on-raspberry-pi/releases/download/v1.1.0/tensorflow-1.1.0-cp27-none-linux_armv7l.whl
sudo pip install tensorflow-1.1.0-cp27-none-linux_armv7l.whl

# For Python 3.4
wget https://github.com/samjabrahams/tensorflow-on-raspberry-pi/releases/download/v1.1.0/tensorflow-1.1.0-cp34-cp34m-linux_armv7l.whl
sudo pip3 install tensorflow-1.1.0-cp34-cp34m-linux_armv7l.whl

Finally, we need to reinstall the mock library to keep it from throwing an error when we import TensorFlow:

# For Python 2.7
sudo pip uninstall mock
sudo pip install mock

# For Python 3.3+
sudo pip3 uninstall mock
sudo pip3 install mock

####### Install Tensorflow End #######
