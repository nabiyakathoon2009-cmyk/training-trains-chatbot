from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():

    return """
    <html>

    <head>
        <title>Training Trains</title>

        <style>

            body{
                background:#0f172a;
                color:white;
                font-family:Arial;
                padding:30px;
            }

            .box{
                background:#1e293b;
                padding:25px;
                border-radius:15px;
                max-width:700px;
                margin:auto;
            }

            h1{
                color:#38bdf8;
            }

            h2{
                color:#f472b6;
            }

            a{
                display:inline-block;
                margin-top:20px;
                padding:12px 20px;
                background:#38bdf8;
                color:black;
                text-decoration:none;
                border-radius:10px;
                font-weight:bold;
            }

        </style>

    </head>

    <body>

        <div class="box">

            <h1>🚀 Training Trains</h1>

            <p>
            Training Trains provides real-time internships
            and industry-level training for students.
            </p>

            <h2>🎓 Domains Available</h2>

            <ul>
                <li>AI & Machine Learning</li>
                <li>Cybersecurity & Ethical Hacking</li>
                <li>IoT & Blockchain</li>
                <li>AWS & Google Cloud</li>
                <li>Full Stack Development</li>
                <li>Digital Marketing & SEO</li>
                <li>Ad Maker - Posters & Reels</li>
            </ul>

            <h2>💰 Mentor Fee Structure</h2>

            <ul>
                <li>10 Days - ₹800</li>
                <li>15 Days - ₹1000</li>
                <li>1 Month - ₹2000</li>
                <li>3 Months - ₹6000</li>
                <li>6 Months - ₹10000</li>
            </ul>

            <h2>📞 Contact</h2>

            <p>
            Email: trainingtrains@gmail.com
            </p>

            <a href="#">
                🚀 Apply Internship
            </a>

        </div>

    </body>

    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
