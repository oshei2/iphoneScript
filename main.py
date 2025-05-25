import csv
import subprocess

def get_iphone_imei():
    try:
        result = subprocess.run(["ideviceinfo"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        for line in lines:
            if "InternationalMobileEquipmentIdentity" in line or "IMEI" in line:
                return line.split(":")[1].strip()
        return None
    except Exception as e:
        print("Error getting IMEI:", e)
        return None

def lookup_code(imei, csv_file="example.csv"):
    try:
        with open(csv_file, mode="r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["IMEI"] == imei:
                    return row["Code"]
        return None
    except FileNotFoundError:
        print(f"CSV file '{csv_file}' not found.")
        return None

imei = get_iphone_imei()
if imei:
    print("Detected IMEI:", imei)
    code = lookup_code(imei)
    if code:
        print("Matched Code:", code)
    else:
        print("No code found for this IMEI.")
else:
    print("Could not detect IMEI.")
