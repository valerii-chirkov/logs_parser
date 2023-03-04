from datetime import datetime


__author__ = "t.me/rebel_sable"


def speedtest(func) -> callable:
    def wrapper(*args, **kwargs) -> callable:
        t1 = datetime.now()

        res = func(*args, **kwargs)
        if kwargs:
            print(f"{kwargs['no_calls']} rows written for", datetime.now() - t1)
        else:
            print("The call took", datetime.now() - t1)
        return res
    return wrapper