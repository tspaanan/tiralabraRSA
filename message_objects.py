class Message:
    def __init__(self, message_content, encrypted):
        self.message_content = message_content
        self.encrypted = encrypted
        #the following are needed for random padding
        self.encrypted_key = None
        self.init_vector = None

    def __str__(self):
        return f'Message{" (encrypted)" if self.encrypted else ""}: {self.message_content}'
