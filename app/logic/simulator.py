from app.logic.device import Device
import random

# Create 5 devices randomly placed on a 10x10 grid
device_pool = [Device(random.randint(0,10), random.randint(0,10)) for _ in range(5)]

def refresh_tokens():
    for device in device_pool:
        device.generate_token()


def simulate_proximity():
    for i, device_a in enumerate(device_pool):
        for device_b in device_pool[i+1:]:
            if device_a.distance_to(device_b) < 5:
                token_a = device_a.exposure_tokens[-1][1]
                token_b = device_b.exposure_tokens[-1][1]
                device_a.receive_token(token_b)
                device_b.receive_token(token_a)