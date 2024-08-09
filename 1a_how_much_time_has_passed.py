""" 1. How Much Time has Passed?

Saat mengerjakan proyek Data Science, kita mungkin menemukan data dalam format Tanggal yang merujuk pada titik waktu tertentu. Mereka sering datang dalam format yang sangat berbeda - beberapa mungkin hanya memiliki tanggal, beberapa mungkin memiliki bulan dan tahun, dan beberapa bahkan memiliki waktu yang tepat (jam, menit, detik) dan zona waktu.

Dalam latihan ini, explore beberapa cara untuk memuat string yang memberi tahu kita tanggal sehingga kita dapat menghitung perbedaan antara dua tanggal input.

Anda akan diminta untuk menulis fungsi bernama duration_count yang mengambil 2 input. Kedua input adalah string yang memberi tahu Anda tanggalnya. Output fungsi Anda haruslah durasi antara 2 input, dalam detik.

Format inputnya adalah: "Tanggal Bulan Tahun Jam:Menit:Detik Informasi_Zona_Waktu"

Contoh 1:
Input 1 = Mon 23 Feb 2017 14:41:10 -0800
Input 2 = Mon 23 Feb 2017 14:41:10 -0200

Kedua input merujuk pada tanggal dan waktu yang sama, tetapi dalam zona waktu yang berbeda. Oleh karena itu, durasi antara kedua tanggal ini adalah: 6 jam. Namun, karena kita ingin jawaban dalam detik, jawaban yang diharapkan adalah 21600 detik. (Outputnya hanya 21600, Anda tidak perlu menulis detik).

Contoh 2:
Input 1 = Mon 23 Dec 2017 14:00:00 -0700
Input 2 = Tue 24 Dec 2017 14:00:00 -0700

Kedua input merujuk pada waktu yang sama dan berada di zona waktu yang sama. Namun, mereka berjarak 1 hari. Oleh karena itu, durasi antara mereka adalah: 1 hari = 1 x 24 x 3600 = 86400 detik.

Extra Clue:
Format harinya disingkat (kita input Mon alih-alih Monday), dan bulannya juga disingkat (kita input Dec alih-alih December).
"""

#
# Calculate the duration in seconds between two given date-time strings.
#

def duration_count(input_1, input_2):
    # Write your code here

    def is_kabisat(year):
        if (year % 400) == 0:
            return True
        if (year % 100) == 0:
            return False
        if (year % 4) == 0:
            return True
        return False
    
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    months = {
        'jan': 0, 'feb': 1, 'mar': 2, 'apr': 3, 'may': 4, 'jun': 5,
        'jul': 6, 'aug': 7, 'sep': 8, 'oct': 9, 'nov': 10, 'dec': 12
    }

    # memecah input menjadi list
    # (Nama_Hari, Tanggal, Bulan, Tahun, Jam, Menit, Detik, Informasi_Zona_Waktu)
    import re
    in_1 = re.sub('(:|-)', ' ', input_1).split()
    in_2 = re.sub('(:|-)', ' ', input_2).split()

    # mengubah ke data numerik dan disimpan ke dalam dict
    arr_1 = {}
    arr_2 = {}

    arr_1['date'] = int(in_1[1]) # tanggal
    arr_1['month'] = months[in_1[2].lower()] # bulan
    arr_1['year'] = int(in_1[3]) # tahun
    arr_1['hour'] = int(in_1[4]) # jam
    arr_1['minute'] = int(in_1[5]) # menit
    arr_1['second'] = int(in_1[6]) # detik
    arr_1['zona'] = in_1[7] # zona

    arr_2['date'] = int(in_2[1]) # tanggal
    arr_2['month'] = months[in_2[2].lower()] # bulan
    arr_2['year'] = int(in_2[3]) # tahun
    arr_2['hour'] = int(in_2[4]) # jam
    arr_2['minute'] = int(in_2[5]) # menit
    arr_2['second'] = int(in_2[6]) # detik
    arr_2['zona'] = in_2[7] # zona

    # mengubah jam ke salah satu zona waktu, jika zona waktu berbeda
    if int(arr_1['zona']) > int(arr_2['zona']):
        arr_2['hour'] = arr_2['hour'] + abs(int(arr_1['zona'][0:2]) - int(arr_2['zona'][0:2]))
        arr_2['minute'] = arr_2['minute'] + abs(int(arr_1['zona'][2:]) - int(arr_2['zona'][2:]))
    if int(arr_1['zona']) < int(arr_2['zona']):
        arr_1['hour'] = arr_1['hour'] + abs(int(arr_1['zona'][0:2]) - int(arr_2['zona'][0:2]))
        arr_1['minute'] = arr_1['minute'] + abs(int(arr_1['zona'][2:]) - int(arr_2['zona'][2:]))
    
    # memberi nilai awal 
    iterate_date = arr_1
    end_date = arr_2

    # mengubah urutan

    is_unsorted = True
    
    # memeriksa tahun
    if arr_1['year'] != arr_2['year']:
        is_unsorted = False
        if arr_1['year'] > arr_2['year']:
            iterate_date = arr_2
            end_date = arr_1
    
    # memeriksa bulan
    if is_unsorted & (arr_1['month'] != arr_2['month']):
        is_unsorted = False
        if arr_1['month'] > arr_2['month']:
            iterate_date = arr_2
            end_date = arr_1
    
    # memeriksa tgl
    if is_unsorted & (arr_1['date'] != arr_2['date']):
        is_unsorted = False
        if arr_1['date'] > arr_2['date']:
            iterate_date = arr_2
            end_date = arr_1

    # memeriksa jam
    if is_unsorted & (arr_1['hour'] != arr_2['hour']):
        is_unsorted = False
        if arr_1['hour'] > arr_2['hour']:
            iterate_date = arr_2
            end_date = arr_1
    
    # memeriksa menit
    if is_unsorted & (arr_1['minute'] != arr_2['minute']):
        is_unsorted = False
        if arr_1['minute'] > arr_2['minute']:
            iterate_date = arr_2
            end_date = arr_1
    
    # memeriksa detik
    if is_unsorted & (arr_1['second'] != arr_2['second']):
        is_unsorted = False
        if arr_1['second'] > arr_2['second']:
            iterate_date = arr_2
            end_date = arr_1
    
    dif_year = abs(end_date['year'] - iterate_date['year'])
    dif_month = abs(end_date['month'] - iterate_date['month'])
    dif_date = 0

    # jika ada beda tahun dan bulan maka iterate_date dan end_date akan dilakukan iterasi
    # hingga mencapai bulan dan tahun yang sama
    while (dif_year>0 or dif_month>0):
        dif_date += month_lengths[iterate_date['month']] - iterate_date['date']
        # jk bln feb pd tahun kabisat
        if (iterate_date['month'] == 1) and is_kabisat(iterate_date['year']):
            dif_date += 1
        
        # jk bln des
        if iterate_date['month'] == 11:
            iterate_date['year'] += 1 # year + 1
            iterate_date['month'] = 0 # diset ke januari
        else:
            iterate_date['month'] += 1
        
        iterate_date['date'] = 0

        dif_year = end_date['year'] - iterate_date['year']
        dif_month = end_date['month'] - iterate_date['month']

    dif_second = dif_date * 24 * 60 * 60
    
    # menambahkan kalkulasi second pada bln yg sama dan tahun yang sama
    add = (24 * 60 * 60 - (iterate_date['hour']*60*60+iterate_date['minute']*60+iterate_date['second'])) + (end_date['date'] - (iterate_date['date'] + 1)) * 24 * 60 * 60 + (end_date['hour']*60*60+end_date['minute']*60+end_date['second'])

    dif_second += add

    return dif_second

"""
# test
input_1 = "Mon 23 Feb 2017 14:41:10 - 0800"
input_2= "Mon 23 Feb 2017 14:41:10 - 0200"
print(duration_count(input_1, input_2))
"""