"""VibeGuard 시드 앱 — 취약한 의존성을 일부러 고정해 둔 예제."""
import joblib
import six
import urllib3
from joblib import Parallel, delayed


def add(left, right):
    """두 수를 더한다."""
    return left + right


def normalize_url(raw):
    """앞뒤 공백을 없애고 소문자로 맞춘다."""
    return raw.strip().lower()


def http_pool():
    """urllib3 연결 풀. 네트워크를 쓰지는 않는다."""
    return urllib3.PoolManager()


def is_py3():
    return six.PY3


def fingerprint(items):
    """목록의 내용으로 지문을 만든다. 같은 내용이면 같은 값이 나온다."""
    return joblib.hash(list(items))


def square_all(numbers):
    """각 수를 제곱한다. joblib의 작업 실행기를 한 줄로 쓴다."""
    return Parallel(n_jobs=1)(delayed(pow)(number, 2) for number in numbers)
