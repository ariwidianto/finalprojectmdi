import pytds
import datetime
import csv

# mengambil data last access
with pytds.connect('localhost', 'finalproject_bu', 'SA', 'SqlserverAri123') as conn:
    with conn.cursor() as cur:
        cur.execute("select last_access from dataset3")
        result = cur.fetchall()

with open('segmentasi_user.csv', mode='w') as segmentasi_user:
    writer = csv.writer(segmentasi_user, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for x in result:
        # convert last access
        d = datetime.datetime.strptime(x[0], "%A, %d %B %Y,  %I:%M %p")

        # convert jam last access ke desimal
        jam_desimal = d.hour*3600+d.minute*60

        # write ke csv
        writer.writerow([d.weekday(), jam_desimal])

        # print(d.weekday(), jam_desimal)

        # # convert jam desimal ke format jam
        # jam = time.strftime('%H:%M:%S', time.gmtime(jam_desimal))
        # print(jam)