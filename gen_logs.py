from datetime import datetime, timedelta
from random import randint

from memory_profiler import profile

from utils import speedtest


__author__ = "t.me/rebel_sable"


def get_call_session() -> str:
    """FROM:2021-01-30 22:18 TO:2021-01-30 22:31"""
    avg: datetime = datetime.now() - timedelta(seconds=randint(0, 1000000))

    from_datetime: str = (avg - timedelta(seconds=randint(0, 1000))).strftime("%Y-%m-%d %H:%M")
    to_datetime: str = (avg + timedelta(seconds=randint(0, 1000))).strftime("%Y-%m-%d %H:%M")

    call_session: str = f"FROM:{from_datetime} TO:{to_datetime}"
    return call_session


def get_calls_amount(rows_min: int = 1000, rows_max: int = 10_000) -> int:
    return randint(rows_min, rows_max)


# @speedtest
@profile
def main(no_calls: int = 50_000) -> None:
    cur_time = datetime.now().strftime("%Y-%m-%d_%Hh%Mm_%Ss")
    with open(f'logs/{cur_time}', 'w', encoding='utf8') as f:
        for _ in range(no_calls):
            row: str = get_call_session()
            f.write(row + '\n')


if __name__ == '__main__':
    calls_amount: int = get_calls_amount(10_000, 100_000)
    main(no_calls=calls_amount)
