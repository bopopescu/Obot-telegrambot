import telebot

#token
import mytoken
TOKEN=mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)

#sql connector
import mysql.connector
myDB=mysql.connector.connect(host='localhost', user='root', database='db_belajarbot')
sql=myDB.cursor()

#tanggal
from datetime import date
from telebot import apihelper
from datetime import datetime
waktusekarang=datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start', 'help'])
    def start(message):
        teks = mytoken.menyapa + "\n /start untuk memulai "+"\n /help untuk mengetahui saya"+"\n /datasiswa untuk mengetahui data siswa XI RPL 1 SMK Taruna Bhakti Depok"
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "SELECT `nipd`,`nama`,`kelas` FROM `tabel_siswa` "
        sql.execute(query)
        data=sql.fetchall()
        jmldata = sql.rowcount
        databnyk = ''
        if(jmldata > 0):
            no = 0
            for x in data:
                no += 1
                databnyk = databnyk + str(x)+"\n"
                print(databnyk)
                databnyk=databnyk.replace('(', '')
                databnyk=databnyk.replace(')', '')
                databnyk=databnyk.replace("'", '')
                databnyk=databnyk.replace(",", '')
        else:
            print('data kosong')
        myBot.reply_to(message,str(databnyk))

print(myDB)
print("-- Bot Sedang Berjalan")
myBot.polling(none_stop=True)