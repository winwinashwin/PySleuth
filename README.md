# PySleuth

PySleuth is an advanced spyware controllable by email.

## Features

- Keylogging

- Mouse activity (pixel coordinates of presses and release with screenshots)

- Process in the active window

- Screenshots every x seconds

### Upcoming

- Clipboard data

- Webcam access

- Control via other applications

## Requirements

### Linux

python >= 3.6

```bash
pip install -r requirements.txt
sudo apt install xdotool
```

### Windows

Coming soon !

## Usage

- Clone repository

- Make an email for the program and setup password for the application

  - From the Google account to send mail from, go to the [security section](https://myaccount.google.com/security)

  - Navigate to the `2-Step Verification` section and make sure it is turned ON

  - Go to the [App passwords section](https://myaccount.google.com/apppasswords)

  - Select app as `Mail` and choose your device and click on `GENERATE`. Note down the password provided

- Save password of email in env variable

```bash
export PYSLEUTH_EMAIL_PWD="your password here"
```

- Edit [settings.cfg](settings.cfg) according to preference

- Run

```bash
python pysleuth
```
