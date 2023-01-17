is_old = True
is_licenced = True

if is_old:
    print("You are old enogh to drive")
elif is_licenced:
    print("You can drive now")
else:
    print("You are not old enough to drive")
#And logic proof, check for both conditions 
if is_licenced and is_old:
    print("You can drive")


