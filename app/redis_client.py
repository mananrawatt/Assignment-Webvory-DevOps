import redis

client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

def test_redis():
    try:
        client.set("health", "ok")
        return client.get("health")
    except Exception:
        return None