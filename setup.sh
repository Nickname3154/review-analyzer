#!/bin/bash

# 필수 시스템 패키지 설치
apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    libnss3 \
    libxss1 \
    libasound2 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    fonts-liberation \
    xdg-utils

# Chrome 설치
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb || apt-get -fy install

# ChromeDriver 버전 일치
CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f 1)
CHROMEDRIVER_VERSION=$(curl -sS "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION")

wget -N "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip"
unzip -o chromedriver_linux64.zip -d /usr/local/bin/
chmod +x /usr/local/bin/chromedriver

# 환경 변수 설정 (선택적으로 .bashrc나 Dockerfile에서도 설정 가능)
export CHROME_BIN=/usr/bin/google-chrome
export PATH=$PATH:/usr/local/bin
