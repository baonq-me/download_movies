#!/usr/bin/python3

from requests import get  # to make GET request

# Run after finish 
# ffmpeg -f concat -safe 0 -i <(for f in *.mp4; do echo "file '$PWD/$f'"; done) -c copy output.mp4

chap1 = "https://xxx.xyz/img/c617361622fab51a28490cbd957c4862/{p}.html?slug=L2hsczUv"
chap2 = "https://xxx.xyz/img/014ec14f4d55fb8373a911742955c42c/{p}.html?slug=L2hsczMv"
chap3 = "https://xxx.xyz/img/59130ec3ff96f26f6952296ba54077a0/{p}.html?slug=L2hsczEv"

def download(url):
    # open in binary mode
    i = 0
    while True:
        print(i)
        with open(str(i) + ".mp4", "wb") as file:
            # get request
            response = get(url.replace('{p}', str(i)))
            if response.status_code != 200:
                break
            file.write(response.content)
            i = i + 1

download(chap2)
