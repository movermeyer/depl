from depl.deploy import redis
from depl.deploy import Package


def test_redis_dependencies():
    redis_settings = {}
    commands = redis.load(redis_settings)
    assert commands == (Package('redis'),)
