import re
from datetime import datetime
from collections import defaultdict

from utils import speedtest


__author__ = "t.me/rebel_sable"


class LogParser:
    """
    Time Complexity: O(N*log N)
    Auxiliary Space: O(N)

    Another possible solution is using:
    Time Complexity: O(N2)
    Auxiliary Space: O(1)

    with for loops, but it takes much longer on a distance
    """

    def __init__(self, logfile_path: str) -> None:
        self.logfile_path: str = logfile_path
        self.timestamps: list = self._get_timestamps()
        self.intersections = defaultdict(int)
        self.timestamps_amount: int = len(self.timestamps)

    def __call__(self, *args, **kwargs) -> int:
        return self.get_result()

    @speedtest
    def get_result(self) -> int:
        self._binary_search_right()
        self._binary_search_left()
        return self._get_operators()

    @staticmethod
    def parse_log_line(line: str) -> tuple:
        re_datetime: str = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}"
        start, end = re.findall(re_datetime, line)
        start_seconds = int(datetime.strptime(start, '%Y-%m-%d %H:%M').timestamp())
        end_seconds = int(datetime.strptime(end, '%Y-%m-%d %H:%M').timestamp())
        return start_seconds, end_seconds

    def _get_timestamps(self) -> list[tuple]:
        with open(self.logfile_path, 'r', encoding='utf8') as f:
            timestamps: list = [self.parse_log_line(line) for line in f]
        return timestamps

    def _get_operators(self) -> int:
        operators: int = 0
        for _, val in sorted(self.intersections.items()):
            operators: int = max(operators, self.timestamps_amount - val + 1)
        return operators

    def _binary_search_right(self) -> None:
        self.timestamps.sort()  # sort by first elem
        for i in range(self.timestamps_amount):
            end, low, high = self.timestamps[i][1], i + 1, self.timestamps_amount - 1
            ans = -1
            while low <= high:
                mid = low + (high - low) // 2
                if self.timestamps[mid][0] > end:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            if ans != -1:
                self.intersections[self.timestamps[i]] = self.timestamps_amount - ans

    def _binary_search_left(self) -> None:
        self.timestamps.sort(key=lambda x: (x[1], x[0]))  # sort by last elem
        for i in range(self.timestamps_amount):
            start, low, high = self.timestamps[i][0], 0, i - 1
            ans = -1
            while low <= high:
                mid = low + (high - low) // 2
                if self.timestamps[mid][1] < start:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            if ans != -1:
                self.intersections[self.timestamps[i]] += (ans + 1)
