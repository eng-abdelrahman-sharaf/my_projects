import time
start = time.time()

duration_secs = 5

print("waiting : "  , end='')
while time.time() <= duration_secs + start:
    for i in "-\|/":
        print(f"\b{i}" , end = "" , flush=True)
        time.sleep(.2)
