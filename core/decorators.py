import time


def wait_until(wait_time=10, period=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = time.time() + wait_time
            while time.time() < total_time:
                if func(*args, **kwargs):
                    return True
                time.sleep(period)
            raise Exception(f'In {wait_time} seconds nothing happened.')
        return wrapper
    return decorator
