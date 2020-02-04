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


# Parallel Mobile Automation Demo Using Selenium Grid
## Installations
- Download selenium standalone server 2.53.1 (https://selenium-release.storage.googleapis.com/index.html)
- To install required libraries and switch to virtual environment run `source venv_grid.sh`
- In addition to the set of libraries used for base project, 2 new libraries will be installed by the above command: `filelock` and `pytest-xdist`. These are required to run pytest tests in parallel and maintaining `device_configs.json` during parallel execution.
- This might also update any existing outdated libraries. To avoid updating libraries change their versions in `requirements/grid.txt` accordingly (e.g, selenium==2.53.1).

## Running the project
- Activate virtual environment: `source venv_grid.sh`
- Open an iOS Simulator and note down its UDID
- Connet an iOS Real Device and note down its UDID
- Open an Android Emulator and note down its UDID
- Open another Android Emulator and note down its UDID
- We now have 4 devices each of which can run a test case

- Open new terminal tab and run the following:
    `cd grid_configs/`
    `java -jar selenium-server-standalone-2.53.1.jar -role hub` Selenium server starts (note the Hub Url)

- Open 4 new terminal tabs and run 4 instances of appium servers
    `cd grid_configs/`
    `appium --nodeconfig nodeconfig_ios_siml_1.json -p 5000` (terminal 1)
    `appium --nodeconfig nodeconfig_ios_siml_2.json -p 5001` (terminal 2)
    `appium --nodeconfig nodeconfig_android_siml_1.json -p 5002` (terminal 3)
    `appium --nodeconfig nodeconfig_android_siml_2.json -p 5003` (terminal 4)

- Open file `grid_configs/device_configs.json`
- Change the UDIDs according to the connected iOS and Android devices (noted in above steps)
- Open file `grid/smoke.py::TestSmokeGrid` and change the `HUB_URL` to the Selenium Hub Url
- Go to project root and run the grid file: `pytest -v -s grid/smoke.py::TestSmokeGrid -n auto`
    The flag `-n auto` will automatically setup the appropriate number of threads according to system capabilities (dual core, quad core etc).
