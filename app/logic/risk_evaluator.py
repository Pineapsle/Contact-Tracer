def evaluate_all_devices(devices, diagnosis_keys):
    results = {}
    for device in devices:
        exposed = []
        for _, seen_token in device.contact_log:
            if seen_token in diagnosis_keys:
                exposed.append(seen_token)
        device.exposed_to = exposed
        results[device.device_id] = exposed
    return results