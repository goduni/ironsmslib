import asyncio

from ironsms import AsyncIronSMS
from loguru import logger

from ironsms.exceptions import BadQueryException

loop = asyncio.get_event_loop()
api = AsyncIronSMS('YOUR_API_KEY')


async def main():
    balance = await api.get_balance()
    logger.info(f'Your balance: {balance.balance}')

    services = await api.get_services()
    logger.info(f'All services: {services}')

    countries = await api.get_countries()
    logger.info(f'All countries: {countries}')

    prices = await api.get_prices('US')
    logger.info(f'USA prices: {prices}')


async def get_number(country: str, service: str):
    number = await api.get_number(country=country, service=service)
    code = None
    while not code:
        code = await api.get_status(number.activation_id)
    return number.phone


async def error_from_api():
    try:
        await api.get_prices("0")
    except BadQueryException as e:
        logger.error(e)


loop.run_until_complete(main())
loop.run_until_complete(get_number('1', '1'))
loop.run_until_complete(error_from_api())
