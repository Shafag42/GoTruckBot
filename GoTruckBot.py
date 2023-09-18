import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
import motor.motor_asyncio
from aiogram import types


# Load environment variables from .env file
load_dotenv()

# Telegram Bot API Token
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Initialize the Bot instance
bot = Bot(token=TELEGRAM_TOKEN)

# Initialize the Dispatcher
dp = Dispatcher(bot)


async def get_order_data():
    # Replace MONGO_URI with your actual MongoDB Atlas connection string
    MONGO_URI = os.getenv("MONGO_URI")

    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
    db = client['GoTruck']
    orders_collection = db['orders']

    # Fetch all documents using a cursor asynchronously
    # cursor = orders_collection.find({}, {'_id': 0})
    cursor = orders_collection.find({})
    order_data = []
    async for document in cursor:
        order_data.append(document)

    return order_data


async def get_group_id():
    group_username = "GoTruckGroup"

    # Get the group info using the group username
    invite_link_info = await bot.get_chat("@" + group_username)

    # Extract and return the group ID
    group_id = invite_link_info.id
    return group_id


async def start_command(message: types.Message):
    # Check if the message is from a group or supergroup
    if message.chat.type in ['group', 'supergroup']:
        message_text = "Salamlar. Bota xoş gəlmisiniz! /Buraya toxunaraq ən son sifarişi görə bilərsiniz."
        await message.answer(message_text)

async def orders_command():
    last_order_id = None  # Initial value, no orders sent yet

    while True:
        # Check for new orders
        order_data = await get_order_data()

        if order_data:
            # Get the latest order
            latest_order = order_data[-1]
            latest_order_id = latest_order.get('_id')

            # If the latest order is different from the last sent order
            if latest_order_id != last_order_id:
                last_order_id = latest_order_id

                # Extract order information
                origin = latest_order.get('origin', 'N/A')
                destination = latest_order.get('destination', 'N/A')
                trucktype = latest_order.get('trucktype', 'N/A')
                minprice = latest_order.get('minpayment', 'N/A')
                maxprice = latest_order.get('maxpayment', 'N/A')
                phone = latest_order.get('number', 'N/A')

                # Compose the message
                message_text = f"Bəylər, yeni sifariş var:\n🗺 Götürüləcək ünvan:{origin}\n🚍 Çatdırılacaq ünvan: {destination}\n🚛 Qoşqunun növü: {trucktype}\n💰 Minimum qiymət: {minprice}\n💰 Maksimum qiymət: {maxprice}\n📞 Əlaqə nömrəsi: {phone}"

                group_id = await get_group_id()
                await bot.send_message(group_id, message_text)

async def check_orders(message: types.Message):
    if message.chat.type in ['group', 'supergroup']:
        # Check for new orders when a user calls /orders command
        order_data = await get_order_data()

        if order_data:
            latest_order = order_data[-1]
            origin = latest_order.get('origin', 'N/A')
            destination = latest_order.get('destination', 'N/A')
            trucktype = latest_order.get('trucktype', 'N/A')
            minprice = latest_order.get('minpayment', 'N/A')
            maxprice = latest_order.get('maxpayment', 'N/A')
            phone = latest_order.get('number', 'N/A')

            message_text = f"Son sifariş:\n🗺 Götürüləcək ünvan:{origin}\n🚍 Çatdırılacaq ünvan: {destination}\n🚛 Qoşqunun növü: {trucktype}\n💰 Minimum qiymət: {minprice}\n💰 Maksimum qiymət: {maxprice}\n📞 Əlaqə nömrəsi: {phone}"

            group_id = await get_group_id()
            await bot.send_message(group_id, message_text)

        else:
            message_text = "Hələki yeni sifariş yoxdur.Təşəkkürlər."

            group_id = await get_group_id()
            await bot.send_message(group_id, message_text)


async def main():
    # Add the command handlers
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(check_orders, commands=["orders","Buraya"])

    # Start the background task to check for new orders and send messages to the group
    asyncio.create_task(orders_command())

    # Start the bot
    await dp.start_polling()


# run the main coroutine until it's completed
if __name__ == "__main__":
    asyncio.run(main())
