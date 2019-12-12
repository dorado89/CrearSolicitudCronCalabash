from time import sleep
import datetime
import Settings
import json
import subprocess
from SQSConnection import SQSConnection


def execute_test(script,urlapk):
    subprocess.Popen([format(Settings.ANDROID_HOME) + "/emulator/emulator", '-avd', 'Pixel_2_API_28'])
    subprocess.run(['wget', '-N', urlapk])
    subprocess.run(['wget', '-N', script])
    subprocess.run(['unzip','-o', './'+script.rsplit('/',1)[-1], '-d','./features/'])
    subprocess.run(['calabash-android', 'resign', './'+urlapk.rsplit('/',1)[-1]])
    sleep(500)
    output = subprocess.call(['calabash-android','run', './'+urlapk.rsplit('/',1)[-1]])
    subprocess.run([format(Settings.ANDROID_HOME) + "/platform-tools/adb", 'shell', 'reboot', '-p'])
    sleep(500)
    subprocess.run([format(Settings.ANDROID_HOME) + "/emulator/emulator", '-avd', 'Pixel_2_API_28','-wipe-data'])
    subprocess.run(['find', '.','-name','"*.feature"','-type','f','-delete'])
    if output < 0:
        print('error en ejecución de prueba')

def process():
    try:
        sqs_connection = SQSConnection(Settings.AWS_QUEUE_URL_OUT_CALABASH)

        with sqs_connection:
            sqs_connection.receive()
            if sqs_connection.message is not '':
                message_body = sqs_connection.message.get('Body')
                msg = json.loads(message_body)
                listapruebas = msg[0]["fields"]["pruebas"]
                script=""
                urlapk=""
                for prueba in listapruebas:
                    script=prueba["script"]
                    urlapk=prueba["url_apk"]
                # sqs_connection.delete()
                execute_test(script,urlapk)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    while True:
        process()
        st = str(datetime.datetime.now())
        sleep(Settings.SLEEP_TIME)
