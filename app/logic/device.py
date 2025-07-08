import uuid, time, hashlib, random

class Device:
    def __init__(self, x, y):
        self.device_id = str(uuid.uuid4())
        self.position = (x, y)
        self.exposure_tokens = []
        self.contact_log = []
        self.exposed_to = []

    def generate_token(self):
        timestamp = str(int(time.time()))
        token = hashlib.sha256((self.device_id + timestamp).encode()).hexdigest()
        self.exposure_tokens.append((timestamp, token))
        return token

    def receive_token(self, token):
        self.contact_log.append((time.time(), token))

    def upload_if_positive(self):
        return [token for _, token in self.exposure_tokens]

    def distance_to(self, other):
        x1, y1 = self.position
        x2, y2 = other.position
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
