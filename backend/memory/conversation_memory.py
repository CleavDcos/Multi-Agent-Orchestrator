#for now lets use dictionary to store convo

class ConversationMemory:

    def __init__(self):
        self.memory_store ={}


#use sessionid to uniquely identify each convo
    def save_message(self,session_id, role, content):
        #create empty list if its a new convo
        if session_id not in self.memory_store:
            self.memory_store[session_id] = []
        self.memory_store[session_id].append({
            "role": role,
            "content": content
        })
        #role can be agent or user and conntent can b wrt that


    def get_conversation(self,session_id):
        #Return previous convo history, if not there return empty list
        return self.memory_store.get(session_id,[])

        