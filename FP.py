import streamlit as st

pola_kalimat = [["K", "SPO"], ["K", "SP"], ["K", "SPOpel"], ["K", "SPOket"], ["K", "SPket"], ["K", "SPpel"]]

rules = [
    ["S", "Noun", "Pronoun", "PropNoun", "NounAdj", "PronounNoun", "NounAdv", "NounPronoun", "NounPropNoun", "NumNoun"],
    ["P", "Verb", "VerbAdj"],
    ["O", "Noun", "Pronoun", "PropNoun", "NounAdj", "PronounNoun", "NounAdv", "NounPronoun", "NounPropNoun", "NumNoun"],
    ["pel", "AdvVerb", "AdvAdj"],
    ["Ket", "PrepPronoun", "PrepPropNoun", "PrepNoun", "PrepAdj"]]

noun = "Noun | dia | kakek| ayah | makanan | gaun| biru | orang | kursi | tua| sepeda | meja | martabak | kampung | sepatu| murid | bapak | ibu | kucing | baju | merah | pak | guru | hunian | doni | lurah | pencuri | polisi | tante | keripik | ikan | pasar | dia | pekerjaan | sultan | kampung | adil | sekolah | putri | mobil | adik | payung | hitam | kakak | karyawan | masakan | anak | sepeda | motor | rumah | andi | otak | jihan | kematian | sedih | fasilitas| umum | kemarin | garam | roti | sifat | david | pohon | lampu | kota | sikap | juara | kabar | mereka | doni | tembok | dapur | tahun | usul | rina | kue | mungkin | kenyataan | dina | mata | agus | mahasiswa | nanda | korban | bencana | alam | uang | saputra | kinan | tugas | beban | ari | gusde | kelas | gereja "
verb = "Verb | membawa | menggunakan | adalah | meduduki | ditaruh | membeli | berkeliaran | memperkenalkan | memberikan | menghukum | menangkap | membuat | dikenal | mendapatkan | menjadi | memiliki | mendengar | berprilaku | mewarnai | menolak | menyatakan | dibuat | menerima | dihukum | lulus | menjawab | mengungsi| mencuri| berlari| tidur| meminjam| mengerjakan| mengangkat| mengantuk"
adj = "Adj | baik | tua | rusak | bulat| manis | liar | baru | nakal | termuda | lihai | pedas | asin | dalam| kaya | mewah | cerdas | baik | terenak | mahal | umum | luas| kokoh | sakit | indah | kecewa | ketus | senang | panik | ramah | muda | sepi | tegas | semanis | setegar | berat | ragu | secepat | tenang| banyak| semampu| kuat"
prep = "Prep | ke | pada | dalam | di| dari | dekat | ketika | sehingga| yang | karena | sejak | dengan"
adv = "Adv | sangat | tidak | masih| sekali | rasa | diam | sedang"

data = []
def appendData():
    data.append(noun.split(" | "))
    data.append(verb.split(" | "))
    data.append(adj.split(" | "))
    data.append(prep.split(" | "))
    data.append(adv.split(" | "))


def TableFilling(lenStr: int) -> list:
    Table = [] #make table filling
    for i in range(lenStr, 0, -1):
        temp = []
        for j in range(i):
            temp.append("")
        Table.append(temp)
    return Table

def RemoveDuplicate(str1: str) -> str:
    final_pola_kalimat = ""
    for i in str1:
        if i not in final_pola_kalimat:
            final_pola_kalimat += i
    return final_pola_kalimat


def convertToSPO(str1: str, RulesSentence: list) -> str: #alba, rules alba berupa list
    ConvertResult = ""
    for i in range(len(RulesSentence[:])):
        for j in RulesSentence[i][1:]:
            if j in str1:
                ConvertResult += RulesSentence[i][0] #str2 itu hasilnya berupa penggabungan pola kalimat S, P, 0 kemudian di cek ada gak duplikasi di bagian pola kalimat pakkek fungsi unique_str
    return RemoveDuplicate(ConvertResult)


def DataMatching(list1: list, list2: list, array: list): # match str user to list of data # test = DataMatching(strinx, data, ar)
    for i in range(0, len(list1)):
        for j in range(len(list2)):
            for k in list2[j][1:]:
                if k in list1[i]:
                    array[i][0] = list2[j][0]
    return array


def CountIndex(y: int, x: int, list1: list):
    x -= 1
    y -= 1
    i = 0
    j = y + 1
    k = x - 1
    while (i < x):
        list1[y][x] = list1[y][i] + list1[j][k]
        i += 1
        j += 1
        k -= 1


def progressingSPO(list1: list, x: int): #  progressingSPO(test, len(strinx))
    leng = x
    for i in range(1, x + 1):
        for j in range(1, leng + 1):
            CountIndex(j, i, list1)
        leng -= 1
    leng = x
    for i in range(0, x):
        for j in range(1, leng):
            alba = list1[i][j]
            alba = convertToSPO(alba, rules)
            list1[i][j] = alba
        leng -= 1


def progressingPolaKalimat(list1: list, x: int):
    leng = x
    for i in range(0, x):
        for j in range(1, leng):
            alba = list1[i][j]
            alba = convertToSPO(alba, pola_kalimat)
            list1[i][j] = alba
        leng -= 1

    for i in range(0, x):
        print(list1[i][:])


def finalCheck(final_pola_kalimat: list) -> bool:
    if "K" in final_pola_kalimat[0][-1]:
        return True
    elif "K" not in final_pola_kalimat[0][-1]:
        return False


def cek_kalimat(strinx):
    strinx = strinx.split(" ") #list ["dia", "adalah", "orang", "baik"]
    appendData()
    ar = TableFilling(len(strinx))
    test = DataMatching(strinx, data, ar)
    progressingSPO(test, len(strinx))
    progressingPolaKalimat(test, len(strinx))
    return finalCheck(test)

st.write("# Cek Tata :red[Bahasa] Indonesia dengan satu kali klik !")


input = st.text_input("Ketik kalimat yang mau di cek", placeholder="ex : dia adalah orang baik")
cek = st.button("Cek tata bahasa kalimat")

if cek:
    if pro.cek_kalimat(input)== True:
        st.success("Kalimat yang anda masukan adalah kalimat yang baku")
    else:
        st.error("kalimat yang anda masukan bukan merupakan kalimat baku")
