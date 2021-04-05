import requests
import re
from media_map import MEDIA_MAP


result = []
for key in MEDIA_MAP:
    for bulk in MEDIA_MAP[key]:
        for item in bulk:
            result.append(item[0])

# counter = 0
# for image in result:
#     response = requests.get(image)
#     counter += 1
#     if response.status_code == 200:
#         with open(f"images/{counter}.jpg", 'wb') as f:
#             f.write(response.content)


new_images = '''https://i.postimg.cc/MTSjQTmh/1.jpg
https://i.postimg.cc/Xvwr4W6x/10.jpg
https://i.postimg.cc/0j5n7ZCR/100.jpg
https://i.postimg.cc/C5vN7DvZ/101.jpg
https://i.postimg.cc/CMJmwTFF/102.jpg
https://i.postimg.cc/ZKRjR7R6/103.jpg
https://i.postimg.cc/gkTs6VXQ/104.jpg
https://i.postimg.cc/nh9kKXqz/105.jpg
https://i.postimg.cc/wv2cxLYW/106.jpg
https://i.postimg.cc/CKjst9Pp/107.jpg
https://i.postimg.cc/FRNVQG8d/108.jpg
https://i.postimg.cc/8cCd7c1T/109.jpg
https://i.postimg.cc/XqDJQ79N/11.jpg
https://i.postimg.cc/SRt6C4sC/110.jpg
https://i.postimg.cc/dQWmz2B3/111.jpg
https://i.postimg.cc/02bdxzWf/112.jpg
https://i.postimg.cc/rFKzzxLD/12.jpg
https://i.postimg.cc/3JVNGNKn/13.jpg
https://i.postimg.cc/0QnrKCQw/14.jpg
https://i.postimg.cc/zvfvCRbP/15.jpg
https://i.postimg.cc/52z0SJy1/16.jpg
https://i.postimg.cc/YSwSXPLF/17.jpg
https://i.postimg.cc/1tm3SNH5/18.jpg
https://i.postimg.cc/2608S8cd/19.jpg
https://i.postimg.cc/prVhs67C/2.jpg
https://i.postimg.cc/Wp9h2SxR/20.jpg
https://i.postimg.cc/3N682fHd/21.jpg
https://i.postimg.cc/rpCw795P/22.jpg
https://i.postimg.cc/05HygjJP/23.jpg
https://i.postimg.cc/ZKBKJmr3/24.jpg
https://i.postimg.cc/HsqWxN2N/25.jpg
https://i.postimg.cc/RZwSnTpZ/26.jpg
https://i.postimg.cc/q70kcCWX/27.jpg
https://i.postimg.cc/QMbjfd3L/28.jpg
https://i.postimg.cc/3NWr45Vs/29.jpg
https://i.postimg.cc/DZP4dTCm/3.jpg
https://i.postimg.cc/QtdhwZ8F/30.jpg
https://i.postimg.cc/Ss1kp1RD/31.jpg
https://i.postimg.cc/SRXqQLzq/32.jpg
https://i.postimg.cc/J098sybX/33.jpg
https://i.postimg.cc/QNPh4zRM/34.jpg
https://i.postimg.cc/c4nZVmSB/35.jpg
https://i.postimg.cc/sgCyyhfd/36.jpg
https://i.postimg.cc/3xjhwxWy/37.jpg
https://i.postimg.cc/Pqtjvn8S/38.jpg
https://i.postimg.cc/zf01n2C8/39.jpg
https://i.postimg.cc/3wMksRVd/4.jpg
https://i.postimg.cc/SsRbVLd8/40.jpg
https://i.postimg.cc/YjKcp5Hf/41.jpg
https://i.postimg.cc/cC8yGsVL/42.jpg
https://i.postimg.cc/HWfjcjW3/43.jpg
https://i.postimg.cc/8PMchDjG/44.jpg
https://i.postimg.cc/JnFVFyYF/45.jpg
https://i.postimg.cc/7PCfZS4f/46.jpg
https://i.postimg.cc/dVF16Xyy/47.jpg
https://i.postimg.cc/Njx0z46P/48.jpg
https://i.postimg.cc/cJ4JynT1/49.jpg
https://i.postimg.cc/yYbgTnTh/5.jpg
https://i.postimg.cc/LsC8H80t/50.jpg
https://i.postimg.cc/k42XDPkk/51.jpg
https://i.postimg.cc/gJ1cZBpr/52.jpg
https://i.postimg.cc/nr7FYYV2/53.jpg
https://i.postimg.cc/NGrjcY8X/54.jpg
https://i.postimg.cc/sDdDf8KN/55.jpg
https://i.postimg.cc/xTvjXR4T/56.jpg
https://i.postimg.cc/W1sNgkBm/57.jpg
https://i.postimg.cc/P5Kt4qHg/58.jpg
https://i.postimg.cc/3wR3bHJd/59.jpg
https://i.postimg.cc/D0CWHc3T/6.jpg
https://i.postimg.cc/W4HTBfhS/60.jpg
https://i.postimg.cc/fLSDDjds/61.jpg
https://i.postimg.cc/prNxThQF/62.jpg
https://i.postimg.cc/rsSTtVgY/63.jpg
https://i.postimg.cc/pV8RSCxY/64.jpg
https://i.postimg.cc/PrjTnD5G/65.jpg
https://i.postimg.cc/rFNcVpDD/66.jpg
https://i.postimg.cc/T32xpXbC/67.jpg
https://i.postimg.cc/7ZBkzQMD/68.jpg
https://i.postimg.cc/TPpXJqCb/69.jpg
https://i.postimg.cc/c1T8vdgb/7.jpg
https://i.postimg.cc/JhvC6D22/70.jpg
https://i.postimg.cc/XqcMY27R/71.jpg
https://i.postimg.cc/MTB2hZkK/72.jpg
https://i.postimg.cc/PJkshGhb/73.jpg
https://i.postimg.cc/9XGHbftL/74.jpg
https://i.postimg.cc/CL7Ty62D/75.jpg
https://i.postimg.cc/15shjZvs/76.jpg
https://i.postimg.cc/DwzV7PVN/77.jpg
https://i.postimg.cc/Y0xVHhdk/78.png
https://i.postimg.cc/3xfsN0Yx/79.jpg
https://i.postimg.cc/6534RFC5/8.jpg
https://i.postimg.cc/jjGBQVWV/80.jpg
https://i.postimg.cc/9MZKLxTD/81.jpg
https://i.postimg.cc/x8Q7hKyt/82.jpg
https://i.postimg.cc/h48Nx5cw/83.jpg
https://i.postimg.cc/15JT7Vgr/84.jpg
https://i.postimg.cc/028FC0NN/85.jpg
https://i.postimg.cc/qvqFPByV/86.jpg
https://i.postimg.cc/fb0rbH88/87.jpg
https://i.postimg.cc/0QRHKp3P/88.jpg
https://i.postimg.cc/rm1Z1DXW/89.jpg
https://i.postimg.cc/Mpfc3RsC/9.jpg
https://i.postimg.cc/VvzGDzmh/90.jpg
https://i.postimg.cc/NFbNnZ0j/91.jpg
https://i.postimg.cc/CM46dn4p/92.jpg
https://i.postimg.cc/yYYpR6fg/93.jpg
https://i.postimg.cc/pXGGJN70/94.jpg
https://i.postimg.cc/6pFMFrBn/95.jpg
https://i.postimg.cc/nhXddRfn/96.jpg
https://i.postimg.cc/PqZSHCqc/97.jpg
https://i.postimg.cc/9MhJQcRf/98.jpg
https://i.postimg.cc/rmNgd7xN/99.jpg'''

image_list = new_images.split('\n')

def get_key(x):
    key = int(re.match('\d+', x.split('/')[4]).group(0))
    return key

image_list.sort(key = lambda x: get_key(x))
print(image_list)

with open('links.txt', 'a') as txt:
    for item in image_list:
        txt.write(item + '\n')
