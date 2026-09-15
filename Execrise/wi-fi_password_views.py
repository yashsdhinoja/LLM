import subprocess

profiles = subprocess.check_output(
    "netsh wlan show profiles", shell=True
).decode()

names = [
    line.split(":")[1].strip()
    for line in profiles.split("\n")
    if "All User Profile" in line
]

for i, name in enumerate(names, 1):
    print(f"[{i}] {name}")

choice = int(input("\n Choose Wi-Fi number: "))
wifi = names[choice - 1]

result = subprocess.check_output(
    f'netsh wlan show profile "{wifi}" key=clear', shell=True
).decode()

print("\n" + result)