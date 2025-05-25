import csv
import subprocess
import time

def get_imei():
    try:
        result = subprocess.run(["ideviceinfo"], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if "InternationalMobileEquipmentIdentity" in line or "IMEI" in line:
                return line.split(":")[1].strip()
        return None
    except Exception as e:
        print("Error getting IMEI:", e)
        return None

def lookup_code(imei, csv_file="example.csv"):
    try:
        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["IMEI"] == imei:
                    return row["Code"]
        return None
    except FileNotFoundError:
        print(f"CSV file '{csv_file}' not found.")
        return None

seen_imeis = set()

while True:
    imei = get_imei()
    if imei and imei not in seen_imeis:
        print("Detected IMEI:", imei)
        code = lookup_code(imei)
        if code:
            print("Matched Code:", code)
        else:
            print("No code found for this IMEI.")
        seen_imeis.add(imei)
    time.sleep(2)
