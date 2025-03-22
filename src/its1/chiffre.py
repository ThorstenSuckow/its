
text = """
 MYHWY DWUDT KHSXT YUAKU SXUXY DQKIK DTISX HYJJU DKURU HTUDV HYUTX
 EVUYD YWUWH QURUH MQHUD IYSXJ BYSXZ KUDWU HUDTQ JKCIQ DTUHU JHKWU
 DTYUI FKHUD TUHPU YJKDT AKUDT YWJUD LEDTU DYHTY ISXUD JQWUD TUHCE
 UDSXU TYUYD TUDLU HWQDW UDUDZ QXHXK DTUHJ UDXYU HWUBU RJXQJ JUDDQ
 CUDIJ QDTUD QBBUH TYDWI DYSXJ QKVTU DWHQU RUHDD KHISX BYSXJ UIJUY
 DUHDU AHUKP U
"""

chars = {}
for i in text:
    if i.strip() == "":
        continue 
    if not i in chars:
        chars[i] = 0 

    chars[i] += 1;


chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))

first = next(iter(chars))
let = chars[first]
print(f"Most common letter in german is \"E\". Letter {first} appears in chars {chars[first]} times");
print("\n")
shifted = abs(ord(first) - ord("E"))
print(f"Assumption: Text is shifted by {shifted} characters")

print("\n")
print("Applying chr(((ord(i) - ord(\"A\") - shifted) % 26) + ord(\"A\")) to each letter...")
print(f"Processed:")

for i in text:
    if i.strip() == "":
        print(i, end="")
    else:
        print(chr(((ord(i) - ord("A") - shifted) % 26) + ord("A")), end="")
