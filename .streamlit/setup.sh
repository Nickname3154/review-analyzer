wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt update
sudo apt install -y ./google-chrome-stable_current_amd64.deb

#!/bin/bash

# 필요한 시스템 라이브러리 설치
sudo apt update && sudo apt install -y \
  libnss3 \
  libxss1 \
  libappindicator1 \
  libindicator7 \
  fonts-liberation \
  libasound2 \
  libatk-bridge2.0-0 \
  libatk1.0-0 \
  libcups2 \
  libdbus-1-3 \
  libgdk-pixbuf2.0-0 \
  libnspr4 \
  libx11-xcb1 \
  libxcomposite1 \
  libxdamage1 \
  libxrandr2 \
  xdg-utils
