from memory.redis_memory import RedisMemory

memory = RedisMemory()

memory.save_message(
    "test123",
    "user",
    "Hello Redis"
)

print(
    memory.get_conversation(
        "test123"
    )
)