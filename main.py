import subprocess

def get_iphone_imei():
    try:
        result = subprocess.run(["ideviceinfo"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        for line in lines:
            if "InternationalMobileEquipmentIdentity" in line or "IMEI" in line:
                print("IMEI:", line.split(":")[1].strip())
                return line.split(":")[1].strip()
        print("IMEI not found.")
    except Exception as e:
        print("Error:", e)

get_iphone_imei()
