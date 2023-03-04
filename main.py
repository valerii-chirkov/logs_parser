import datetime

from memory_profiler import profile

from parse_logs import LogParser


"""
Test task for IPChain Python position
"""
__author__ = "t.me/rebel_sable"


path_to_logfile: str = 'logs/2023-03-04_03h34m_07s'
fp = open(f'profile_reports/memory_profiler_{datetime.datetime.now()}.log', 'w+')


def append_logfile_stats(res) -> None:
    with open(path_to_logfile, 'r') as f:
        lines_count: int = len(f.readlines())
        fp.write(f"LINES AMOUNT: {lines_count}\n")
    fp.write(f"Min need of operators is {res}\n\n")


@profile(stream=fp)
def main(path: str) -> None:
    parser = LogParser(path)
    res: int = parser()
    f"Min need of operators is {res}"
    append_logfile_stats(res)  # optional not optimal


if __name__ == "__main__":
    main(path=path_to_logfile)
