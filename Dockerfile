FROM python:slim
ENV TOKEN='5213330402:AAH9LI9o-TnGg5JeC6SurcZhOl6TSu0p4O0'
COPY . .
RUN pip install -r requirements.txt
# WORKDIR .
CMD python bot.py