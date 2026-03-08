import re
import requests

contest_id = 676640  # change this

handles_raw = """
Zelalem-G
net_123
xe-non
khalidg243
https://codeforces.com/profile/creator-ermias
kidy1924 
abirham_gedefaw 
@bethelsahle00
SORA0
fdoolyrabie82
jedidiha
Alphaxardjr
https://codeforces.com/profile/Karabo_M
Meriem8b
h
jealsab
redeat.ephrem@a2sv.org
@Dave051621
Bekii7
Bekii7
natnael-esk
@dagin34
@tkanateydadzie
MotiAbe
@Simanga
habtamu_tesf
biruk.birhanu
@eilafsalah649
@weldemdhinnahom
TsedeniyaG
DawitH
abdulsoburoyewale
nm_zenagui
Ghadeer_Elsalhawy
@Nahla98
ephrem64
yerosen_tamrat
birukmj
noskiya
youssef_hany
BlenBizuayehu
abelgideon
mailtoruhiru@gmail.com
chadawiii
ZiglaCity
chadawiii
azizexp00
A7madMuddathir
BlenBizuayehu
@ob22a
BIN01
@theniitettey
https://codeforces.com/profile/firaoltegene
@yosef.abebe
pwnxr
beamalk
https://codeforces.com/profile/ayalworku
@ier2077
ta9i
@Natty_04
Johannes_613
HelenTewoldebirhan
@kaleabalebachew3
@mthabisi.ndlovu
@semako123
@Abrham_Abe
Samatsam0020
https://codeforces.com/profile/knesibu3
Hazemkisuke 
its.done
abelzeleke5173
@ier2077
abelzeleke5173
https://codeforces.com/profile/knesibu3
https://codeforces.com/profile/Abija
evarigusponticus
rafa_houssam
Pidoxy
Katamansokirk
https://codeforces.com/profile/Noah_Liknaw
musanje.richard
@Sebhiii
@jonazz
BeimnetTefera
@pablo_blart
toyibah7
@pablo_blart
aldricrealm
@akuuzume
@samilili
@emmanuel_mingo
getayawkal
Alexen267
MomenHossam
Omar_Abo_Elward
meron_yeneneh
https://codeforces.com/profile/gelilla
irenebusah
@peterase_1
Hassan_Luqman_Adelani
saani_mustaf1
@besu179
@Psychic_Cyclone
mohamoha2006d
Collinskobby
Ahmed.H_Zoldyck
daduam
KbromMehari
Collinskobby
@hosanna1616
rsambing
elsabetwuletaw
shekiii
https://codeforces.com/profile/habtamu16
@Hiwot_Belay_Mekonnen
chioma.annan
jan_elle
yoni_54
@enielect
DawitH
@notoriousdev
DawitH
__Kuayi
MotiAbe
@Yoseph_won
biruk.birhanu
nourmaj
https://codeforces.com/profile/samuelflatie
@dino_aser
wintana
net_123
https://codeforces.com/profile/samuelteshome79
abirham_gedefaw
Samrawit7
boituu.xz
hawipaul308
https://codeforces.com/profile/firaoltegene
ibkvictor
@xtypercode
Ofori
RuhamaKassahun
habtamu_tesf
veranyagaka 
sdmh725
Semhal
zachabera1999
Samrawit7
@notoriousdev
@achib
ghazali_ensia
Alexen267
Hassan_Luqman_Adelani
elikem.fenuku
@siyam_aman
veranyagaka
"""

handles = set()

for line in handles_raw.splitlines():
    line = line.strip()

    if not line:
        continue

    # extract from CF link
    if "codeforces.com/profile/" in line:
        handle = line.split("/")[-1]
        handles.add(handle)
        continue

    # remove @
    if line.startswith("@"):
        line = line[1:]

    # skip emails
    if "@" in line:
        continue

    handles.add(line)

handles = list(handles)

url = "https://codeforces.com/api/contest.standings"

params = {
    "contestId": contest_id,
    "handles": ";".join(handles),
    "showUnofficial": "true"
}

data = requests.get(url, params=params).json()
if data["status"] != "OK":
    print("API Error:", data)
    exit()
for r in data["result"]["rows"]:
    print(
        r["rank"],
        r["party"]["members"][0]["handle"],
        r["points"],
        r["penalty"]
    )