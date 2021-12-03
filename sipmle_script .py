import json_logging, logging, sys

json_logging.init_non_web(enable_json=True)

logger = logging.getLogger("Logger my app")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler('/var/log/myapp.log'))

print("Введите число")
val = int(input())
double = val * 2
print("Удваиваем число и получаем", double)

logger.info(f'Введенное число {val}')
