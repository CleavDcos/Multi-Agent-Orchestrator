import json
import redis

class RedisMemory:

    def __init__(self):
        #Configure client to communicate with redis server
        self.redis_client = redis.Redis(
            host='redis',
            port=6379,
            decode_responses=True
        )
    #using session id get the current convo
    def get_conversation(self, session_id: str):
        
        key = f"session:{session_id}"
        conversation = self.redis_client.get(key)

        if conversation:
            return json.loads(conversation) #load json format of the convo, which u saved/got using session id
        return []  #if no convo, return empty list
    
    #After loading convo, save it 
    def save_message(self, session_id: str, role: str, content: str):
        key = f"session:{session_id}"
        message = {"role": role, "content": content}

        # Get existing conversation
        conversation = self.get_conversation(session_id)
        conversation.append(
            {
                "role": role,
                "content": content
            }
        )

        # Save updated conversation
        self.redis_client.set(key, json.dumps(conversation))