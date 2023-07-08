FROM python:3.9.16

RUN apt-get update

RUN pip install openai
RUN pip install python-telegram-bot --upgrade
WORKDIR /home/workspace

ENV TOKEN <your token>
ENV API_KEY <yout api key>

#ENTRYPOINT ["/bin/bash"]
CMD ["python", "main.py"]
