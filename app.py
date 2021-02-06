from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'test'
app.config['MYSQL_PASSWORD'] = '987654321'
app.config['MYSQL_DB'] = 'db_consorcio'
mysql = MySQL(app)

################################(GLOBALS)################################
SERVER_ERROR = "[!] Error en el servidor."
CLIENT_ERROR = "[!] Request invalida."
CODE_ERROR = "[!] Código invalido"
#########################################################################

# Esta ruta permite que se renderice el home.
@app.route('/')
def Index():
    return render_template('index.html')

# Esta ruta sera utilizada para proporcionar datos desde la base de datos a la plantilla HTML del pdf.
@app.route('/get_pdf', methods=['GET'])
def get_pdf():
    return 'get pdf'

# Ruta de prueba para agregar codigos a la base de datos. (MOTIVOS DE TESTEO)
@app.route('/create_code', methods=['POST'])
def create_code():
    codigo_introducido = request.form['create_code']

    # Verificamos que el codigo sea de 8 digitos.
    if int(codigo_introducido) > 9999999 and int(codigo_introducido) < 99999999:
        try:
            cur = mysql.connection.cursor()
            # Inserta el codigo introducido por el usuario en la base de datos.
            cur.execute("""INSERT INTO codes (access_code) VALUES (%(codigo)s)""", {'codigo': codigo_introducido})
            mysql.connection.commit()
            return "[+] Código creado: {} ".format(codigo_introducido)
        except Exception:
            print(SERVER_ERROR)
    else:
        return CODE_ERROR

# Cuando el usuario introduce el codigo y presiona el boton de "Ingresar" hacemos la consulta a la base de datos,
# verificamos que el codigo sea valido, si es valido lo redireccionamos a la web donde puede descargar el pdf.
# si es invalido, proporcionamos un mensaje de error para notificar que el codigo es invalido.
@app.route('/verify_code', methods=['POST'])
def verify_code():
    if request.method == 'POST':

        codigo_introducido = request.form['codigo']
        cur = mysql.connection.cursor()

        # Utilizamos COUNT(*) para contar los resultados totales, 
        # lo uso para saber la cantidad de clientes que existen en la base de datos.
        try:
            cur.execute('SELECT COUNT(*) FROM codes;')
            clientes_totales = cur.fetchone() # cambiar a fetchone()
            print("clientes totales {} ".format(clientes_totales[0]))
        except Exception:
            print(SERVER_ERROR)

        # Comparamos el codigo introducido con todos los codigos de la base de datos.
        for i in range(clientes_totales[0]):
            try:
                cur.execute("""SELECT access_code FROM codes WHERE ID = %(code)s""", {'code': i + 1})
                codigo_en_db = cur.fetchone()
                codigo_en_db = codigo_en_db[0]
            except Exception:
                print(SERVER_ERROR)

            # Si encontramos un codigo valido, redireccionamos al usuario a la pagina donde puede descargar el pdf.
            if int(codigo_introducido) == codigo_en_db:
                return "[*] Código valido: {}".format(codigo_en_db)

        # En caso de que no se haya encontrado ningun codigo que coincida, se devuelve este mensaje:
        return CODE_ERROR
    else:
        return CLIENT_ERROR

if __name__ == '__main__':
    app.run(port = 3000, debug = True)