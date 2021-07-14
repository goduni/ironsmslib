from ironsms import SyncIronSMS
from loguru import logger

from ironsms.exceptions import BadQueryException

api = SyncIronSMS('YOUR_API_KEY')

balance = api.get_balance()
logger.info(f'Your balance: {balance.balance}')

services = api.get_services()
logger.info(f'All services: {services}')

countries = api.get_countries()
logger.info(f'All countries: {countries}')

prices = api.get_prices('US')
logger.info(f'USA prices: {prices}')


def get_number(country: str, service: str):
    number = api.get_number(country=country, service=service)
    code = None
    while not code:
        code = api.get_status(number.activation_id)
    return number.phone


def error_from_api():
    try:
        api.get_prices("0")
    except BadQueryException as e:
        logger.error(e)


phone = get_number('1', '1')
error_from_api()
