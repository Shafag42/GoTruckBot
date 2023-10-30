# GoTruckBot

The GoTruck bot is a Telegram bot designed to help users find and post trucking orders. This README provides information on what the bot does, how to set it up, and how to use it effectively.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

- **Order Posting:** Users can post new trucking orders, specifying details such as origin, destination, truck type, and pricing.

- **Order Notifications:** The bot sends order notifications to a specified Telegram group whenever a new order is posted.

- **Order Retrieval:** Users can check the most recent order using the `/orders` command.

## Requirements

- Python 3.6+
- A MongoDB database for storing orders
- A Telegram Bot Token

## Installation

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/Shafag42/gotruck-bot.git
    ```

2. Change to the project directory:

    ```
    cd gotruck-bot
    ```

3. Create a virtual environment (recommended):

    ```
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

    ```
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```
    source venv/bin/activate
    ```

5. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

## Configuration

Before running the bot, you need to configure it with your Telegram Bot Token and MongoDB connection string. To do this:

1. Create a `.env` file in the project directory.

2. Add the following lines to the `.env` file:

    ```
    TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
    MONGO_URI=YOUR_MONGODB_CONNECTION_STRING
    ```

3. Replace `YOUR_TELEGRAM_BOT_TOKEN` and `YOUR_MONGODB_CONNECTION_STRING` with your actual Telegram Bot Token and MongoDB connection string.

## Usage

To run the bot:


Now, users can interact with the bot on Telegram by starting a chat with it and using the available commands.

- `/start`: Start a chat with the bot.
- `/orders`: Retrieve the most recent order posted.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.


