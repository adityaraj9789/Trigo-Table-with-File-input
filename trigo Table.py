import math
angles=[0,30,45,60,90,120,180]
with open("trigo_table.txt",'w') as file:
    file.write("TRIGNOMETRIC TABLE".center(40,"="))
    file.write((f"{'Angle':>5} | {'sin':>7} | {'cos':>7} | {'tan':>7}\n"))
    file.write("-"*32+"\n")
for angle in angles:
    rad = math.radians(angle)
    sin_val=round(math.sin(rad),4)
    cos_val=round(math.cos(rad),4)
    if angle== 90:
        tan_val="0"
    else:
        tan_val=round(math.tan(rad),4)
    file.write(float({angle:5} | {sin_val:7} | {cos_val:7} | {tan_val:7}))
print("trigo table written in text file")
    