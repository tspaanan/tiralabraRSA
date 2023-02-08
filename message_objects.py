class Message:
    def __init__(self, message_content, encrypted):
        self.message_content = message_content
        self.message_length = -1 #tarvitaanko?
        self.encrypted = encrypted

    def __str__(self):
        return f'Message{" (encrypted)" if self.encrypted else ""}: {self.message_content}'
