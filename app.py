from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chi-sono")
def chi_sono():
    return render_template("chi-sono.html")

@app.route("/itinerari")
def itinerari():
    lista_itinerari = [
        {
            "titolo": "Roma classica",
            "descrizione": "Un itinerario tra i grandi simboli della Città Eterna, tra arte, storia e meraviglia.",
            "durata": "2 ore",
            "luogo": "Roma"
        },
        {
            "titolo": "Matera e i Sassi",
            "descrizione": "Un percorso affascinante tra pietra, spiritualità, storia e paesaggi unici.",
            "durata": "2/3 ore",
            "luogo": "Basilicata"
        },
        {
            "titolo": "Borghi di Puglia",
            "descrizione": "Visite guidate tra centri storici, tradizioni locali e architetture tipiche del Sud.",
            "durata": "personalizzabile",
            "luogo": "Puglia"
        }
    ]
    return render_template("itinerari.html", itinerari=lista_itinerari)

@app.route("/tariffe")
def tariffe():
    return render_template("tariffe.html")

@app.route("/galleria")
def galleria():
    return render_template("galleria.html")

@app.route("/recensioni")
def recensioni():
    recensioni_clienti = [
        {
            "testo": "Una visita splendida, ricca di contenuti e raccontata con grande passione.",
            "autore": "Marie, France"
        },
        {
            "testo": "Esperienza molto coinvolgente, organizzata con professionalità e gentilezza.",
            "autore": "Lucia, Italia"
        },
        {
            "testo": "Tour bellissimo, elegante nei modi e molto interessante nei contenuti.",
            "autore": "Jean-Pierre, France"
        }
    ]
    return render_template("recensioni.html", recensioni=recensioni_clienti)

@app.route("/contatti", methods=["GET", "POST"])
def contatti():
    successo = False

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        messaggio = request.form.get("messaggio")

        with open("messaggi.txt", "a", encoding="utf-8") as file:
            file.write(f"Nome: {nome}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Messaggio: {messaggio}\n")
            file.write("-" * 50 + "\n")

        successo = True

    return render_template("contatti.html", successo=successo)

if __name__ == "__main__":
    app.run(debug=True)