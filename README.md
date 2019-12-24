# edx-app-test
Automated testing for edX Android and iOS mobile applications.

## Using Docker
- [docker for Mac](./DockerMac.md)
- [docker for Ubuntu](./DockerUbuntu.md)

## Manual Installations
- [node](https://nodejs.org/en/)
- [appium](http://appium.io/)
- [pytest](https://docs.pytest.org/en/latest/getting-started.html)
- [pytest-html](https://pypi.python.org/pypi/pytest-html/)
- [Appium-Python-Client](https://pypi.org/project/Appium-Python-Client/)
- [PyYAML](https://pypi.org/project/PyYAML/)

###### iOS(Simulator)
 - Xcode with command line tools
 - [libimobiledevice](http://www.libimobiledevice.org/)
 - [ios_deploy](https://github.com/phonegap/ios-deploy)

###### Android(Phone/Tablet/Simulator)
 - [Android SDK](https://developer.android.com/studio/index.html)

 Don't forget to set environment variables for adb, platform-tools etc.*

#### Setup
- connect/start Android/iOS Device/Simulator
- Browse tests/ directory 
- Rename 'user_preferences_sample.yml' to 'user_preferences.yml' and set following values, 

    - set `Android' to execute test cases on Android or 'iOS' to execute on iOS

          target_environment: Android

    - set above selected target_environment's OS Version(of specific running device/simulator) like below

          ios_platform_version: iOS emulator version 

          android_platform_version: Android device/emulator version

    - set valid credentials to login

          login_user_name: username 

          login_password: password 

- install edx(iOS/Android) app on specific device/simulator


#### Run
- Check out/download the source code, browse its directory

        git clone https://github.com/edx/edx-app-test

- `pytest` - to run all test cases

- `pytest -v <test case name>` to run specific test case

- `pytest -v <test case name> --html=report.html` to run specific test case and create html report at end of execution

#### Find-element-by-image-installation
- npm install opencv4nodejs
- Create images folder in the root directory and plac all images in it, for which you need to find its elements.
- update appium settings, Add this line before finding image method
      "self.driver.update_settings({"imageMatchThreshold": 0.3})"
- Implement find by image functionality by this line and add exact image path as parameter to this function:
      " self.driver.find_element_by_image('path to image')"
- This method will return an element and you can use this element according to your requirement.
