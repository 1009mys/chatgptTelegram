docker 빌드\
docker build . --tag chatgpt_telegram

docker 실행\
docker run -d -t -p 80:80/tcp -p 88:88/tcp -p 443:443/tcp --restart unless-stopped -v /home/a1009mys/chatgptTelegram:/home/workspace --name chatgptTelegram_0.1.1 chatgpt_telegram:0.1.1