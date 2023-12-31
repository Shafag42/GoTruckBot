# Base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /Telegram Bot

# Copy the necessary files into the container
COPY GoTruckBot.py .
COPY requirements.txt .
COPY .env .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot
CMD [ "python", "GoTruckBot.py" ]
