from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from tqdm import tqdm

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    current_datetime = datetime.now()
    print(current_datetime)
    a = 0
    for i in tqdm(range(1, 10000000)):
        a += i

