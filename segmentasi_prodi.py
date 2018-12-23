import pytds
import csv

# mengambil data last access
with pytds.connect('localhost', 'finalproject', 'SA', 'SqlserverAri123') as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT count(distinct matkul) as jml_matkul, count(distinct mhs) as jml_mhs FROM dataset3 WHERE jurusan like 'Biologi'")
        result1 = cur.fetchall()

        cur.execute(
            "SELECT count(distinct matkul) as jml_matkul, count(distinct mhs) as jml_mhs FROM dataset3 WHERE jurusan like 'Fisika'")
        result2 = cur.fetchall()

        cur.execute(
            "SELECT count(distinct matkul) as jml_matkul, count(distinct mhs) as jml_mhs FROM dataset3 WHERE jurusan like 'Kimia'")
        result3 = cur.fetchall()

        cur.execute(
            "SELECT count(distinct matkul) as jml_matkul, count(distinct mhs) as jml_mhs FROM dataset3 WHERE jurusan like 'Teknik Fisika'")
        result4 = cur.fetchall()

        cur.execute(
            "SELECT count(distinct matkul) as jml_matkul, count(distinct mhs) as jml_mhs FROM dataset3 WHERE jurusan like 'Teknik Industri'")
        result5 = cur.fetchall()

        cur.execute(
            "SELECT count(distinct matkul) as jml_matkul, count(distinct mhs) as jml_mhs FROM dataset3 WHERE jurusan like 'Teknik Kimia'")
        result6 = cur.fetchall()

        cur.execute(
            "SELECT count(distinct matkul) as jml_matkul, count(distinct mhs) as jml_mhs FROM dataset3 WHERE jurusan like 'Teknik Material dan Metalurgi'")
        result7 = cur.fetchall()

        cur.execute(
            "SELECT count(distinct matkul) as jml_matkul, count(distinct mhs) as jml_mhs FROM dataset3 WHERE jurusan like 'Teknik Mesin'")
        result8 = cur.fetchall()

        cur.execute(
            "SELECT count(distinct matkul) as jml_matkul, count(distinct mhs) as jml_mhs FROM dataset3 WHERE jurusan like 'Informatika'")
        result9 = cur.fetchall()

        cur.execute(
            "SELECT count(distinct matkul) as jml_matkul, count(distinct mhs) as jml_mhs FROM dataset3 WHERE jurusan like 'Sistem Informasi'")
        result10 = cur.fetchall()

        cur.execute(
            "SELECT count(distinct matkul) as jml_matkul, count(distinct mhs) as jml_mhs FROM dataset3 WHERE jurusan like 'Teknik Kelautan'")
        result11 = cur.fetchall()

        cur.execute(
            "SELECT count(distinct matkul) as jml_matkul, count(distinct mhs) as jml_mhs FROM dataset3 WHERE jurusan like 'Teknik Perkapalan'")
        result12 = cur.fetchall()

        cur.execute(
            "SELECT count(distinct matkul) as jml_matkul, count(distinct mhs) as jml_mhs FROM dataset3 WHERE jurusan like 'Teknik Sistem Perkapalan'")
        result13 = cur.fetchall()

# write ke csv
with open('segmentasi_prodi.csv', mode='w') as segmentasi_prodi:
    writer = csv.writer(segmentasi_prodi, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for x in result1:
        writer.writerow(['Biologi', x[0], x[1]])

    for x in result2:
        writer.writerow(['Fisika', x[0], x[1]])

    for x in result3:
        writer.writerow(['Kimia', x[0], x[1]])

    for x in result4:
        writer.writerow(['Teknik Fisika', x[0], x[1]])

    for x in result5:
        writer.writerow(['Teknik Industri', x[0], x[1]])

    for x in result6:
        writer.writerow(['Teknik Kimia', x[0], x[1]])

    for x in result7:
        writer.writerow(['Teknik Material dan Metalurgi', x[0], x[1]])

    for x in result8:
        writer.writerow(['Teknik Mesin', x[0], x[1]])

    for x in result9:
        writer.writerow(['Informatika', x[0], x[1]])

    for x in result10:
        writer.writerow(['Sistem Informasi', x[0], x[1]])

    for x in result11:
        writer.writerow(['Teknik Kelautan', x[0], x[1]])

    for x in result12:
        writer.writerow(['Teknik Perkapalan', x[0], x[1]])

    for x in result13:
        writer.writerow(['Teknik Sistem Perkapalan', x[0], x[1]])