""" 2. What Day is It?

Dalam data time series, kita biasanya ingin tahu hari apa itu. Biasanya tidak cukup hanya mengetahui 'angka' tanggal, terutama ketika hari yang sangat penting untuk data kita (misalnya: analisis perilaku pelanggan). Dalam skenario analisis perilaku pelanggan, kita mungkin menemukan perilaku yang berbeda pada Monday - Friday vs Saturday - Sunday (akhir pekan). Mengetahui hari juga memungkinkan kita untuk memetakan beberapa musim.
 

Diberikan 3 input: tanggal pertama, lalu bulan, dan terakhir tahun. Bisakah Anda memberi tahu kami hari apa itu? Anda dapat menggunakan library apa pun yang Anda inginkan. Nama fungsi Anda harus bernama find_day.

 

Contoh 1:
find_day(11,10,2021) harus memberikan output "Monday", karena 11 Oktober 2021 adalah hari Senin.
 

Contoh 2:
find_day(17,8,1945) harus memberikan output "Friday", karena 17 Agustus 1945 adalah hari Jumat.
"""

# Complete the 'maximum' function below.
# 
# Returns the day of the week for a given date.
#

def find_day(day, month, year):
    # Write your code here
    
    def is_kabisat(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False
    
    # reference point
    day_0 = 1
    month_0 = 1
    year_0 = 1970

    # days of a week at 1 jan 1970
    days = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Thuesday", "Wednesday"]
    
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
    dif_year = abs(year - year_0)
    dif_month = abs(month - month_0)

    dif_date = 0

    end_y = year
    end_m = month
    end_d = day

    iterate_y = year_0
    iterate_m = month_0
    iterate_d = day_0

    # jika input lebih kecil dari titik referensi, data tanggal ditukar
    if year < year_0:
        end_y = year_0
        end_m = month_0
        end_d = day_0
        iterate_y = year
        iterate_m = month
        iterate_d = day

    # jika ada beda tahun dan bulan maka akan dilakukan iterasi per bulan hingga mencapai bulan dan tahun yang sama
    while (dif_year>0 or dif_month>0):
        dif_date += month_lengths[iterate_m-1] - iterate_d
        
        # jk bln feb pd tahun kabisat
        if (iterate_m == 2) and is_kabisat(iterate_y):
            dif_date += 1
        
        # update data stlh mencapai bln des
        if iterate_m == 12:
            iterate_y += 1 # year + 1
            iterate_m = 1 # diset ke januari
        else:
            iterate_m += 1

        iterate_d = 0

        dif_year = end_y - iterate_y
        dif_month = end_m - iterate_m
    
    # menambahkan perbedaan hari pada bln yg sama dan tahun yang sama
    add = end_d - iterate_d

    dif_date += add

    # jika tahun input lbh kecil dari 1 Jan 1970
    # indeks pencarian hari dimulai dari belakang
    if year < year_0:
        dif_date = 7 - dif_date 
    
    return days[dif_date % 7]

print(find_day(27,10,1980))
