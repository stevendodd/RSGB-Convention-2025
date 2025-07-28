import os
import subprocess

binary = "irtools"
if os.name == "nt":
    binary = "flirc_util.exe"

command = [
    binary,
    "sendir",
    "--repeat=1",
    '--raw="+9092 -4402 +638 -456 +639 -451 +643 -452 +643 -451 +669 -426..."',
]

p = None
p = subprocess.run(command, capture_output=True, text=True)

if p.stdout:
    print(p.stdout.strip())
