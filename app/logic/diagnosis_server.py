DIAGNOSIS_FILE = "diagnosis_keys.txt"

def upload_diagnosis_keys(keys):
    with open(DIAGNOSIS_FILE, "a") as f:
        for key in keys:
            f.write(key + "\n")

def get_diagnosis_keys():
    try:
        with open(DIAGNOSIS_FILE) as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []