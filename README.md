# Telegram-upbitty
Telegram Bot for inspect upbit cryptocurrency

## Docker & Docker Compose Version
* Docker version 1.13.1, build 64e9980/1.13.1
* docker-compose version 1.26.2, build eefe0d31

## Just Execute!

To run the following command:

```
# Linux(Ubuntu 18.04)
# Example api key : 123456789:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
sed -i 's/HTTP_API : your_telegram_http_api_key/HTTP_API : 123456789:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/g' docker-compose.yml
docker-compose up -d --build
```
