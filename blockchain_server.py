from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Cyber Defense Dashboard</title>
    <style>
        body {
            background-color: black;
            color: #00FF00;
            font-family: 'Courier New', monospace;
            margin: 0;
            overflow: hidden;
        }
        header {
            background: linear-gradient(90deg, #001100, #003300);
            padding: 15px;
            text-align: center;
            color: #00FF00;
            text-shadow: 0 0 10px #00FF00;
            font-size: 22px;
            border-bottom: 2px solid #00FF00;
            position: relative;
        }
        #status {
            position: absolute;
            right: 30px;
            top: 18px;
            font-size: 14px;
            color: #0f0;
        }
        #controls {
            text-align: center;
            margin: 10px;
        }
        button {
            background-color: black;
            border: 1px solid #00FF00;
            color: #00FF00;
            padding: 6px 12px;
            margin: 5px;
            cursor: pointer;
            border-radius: 5px;
            font-family: inherit;
        }
        button:hover {
            background-color: #00FF00;
            color: black;
        }
        #terminal {
            height: 80vh;
            overflow-y: auto;
            white-space: pre-wrap;
            padding: 15px;
            margin: 10px;
            border: 2px solid #00FF00;
            box-shadow: 0 0 25px #00FF00;
        }
        .alert {
            color: #FF3333;
            font-weight: bold;
            animation: flash 1s infinite alternate;
        }
        .info {
            color: #00BFFF; /* Blue for normal */
            font-weight: bold;
        }
        .error {
            color: #FFD700; /* Yellow for errors */
            font-weight: bold;
        }
        .type {
            font-weight: bold;
        }
        @keyframes flash {
            from { text-shadow: 0 0 5px #FF0000; }
            to { text-shadow: 0 0 25px #FF0000; }
        }
        canvas {
            position: fixed;
            top: 0;
            left: 0;
            z-index: -1;
            width: 100%;
            height: 100%;
        }
        #glow-bar {
            height: 5px;
            width: 100%;
            background: linear-gradient(90deg, red, yellow, lime, cyan, blue, magenta, red);
            animation: glowMove 5s linear infinite;
        }
        @keyframes glowMove {
            from {background-position: 0 0;}
            to {background-position: 1000px 0;}
        }
    </style>
</head>
<body>
    <canvas id="matrix"></canvas>
    <header>
        🛡️ Real-Time Cyber Defense Dashboard
        <span id="status">🟢 Active</span>
    </header>
    <div id="glow-bar"></div>

    <div id="controls">
        <button onclick="fetchLogs()">🔄 Refresh Logs</button>
        <button onclick="location.reload()">🔁 Reload Dashboard</button>
        <button onclick="setFilter('all')">All Logs</button>
        <button onclick="setFilter('alert')">Alerts Only</button>
        <button onclick="setFilter('info')">Normal Only</button>
        <button onclick="setFilter('error')">Errors Only</button>
    </div>

    <div id="terminal"></div>

    <audio id="alertSound" src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg"></audio>

    <script>
        let currentFilter = 'all';
        async function fetchLogs() {
            const res = await fetch('/logs');
            const text = await res.text();
            document.getElementById('terminal').innerHTML = text;
            document.getElementById('terminal').scrollTop = document.getElementById('terminal').scrollHeight;
            applyFilter();

            // Play sound when attack detected
            if (text.includes("🚨")) {
                document.getElementById('alertSound').play().catch(()=>{});
            }
        }

        setInterval(fetchLogs, 1500);
        fetchLogs();

        function setFilter(f) {
            currentFilter = f;
            applyFilter();
        }

        function applyFilter() {
            document.querySelectorAll('.alert, .info, .error').forEach(el => {
                if (currentFilter === 'all') el.style.display = 'block';
                else if (currentFilter === 'alert' && el.classList.contains('alert')) el.style.display = 'block';
                else if (currentFilter === 'info' && el.classList.contains('info')) el.style.display = 'block';
                else if (currentFilter === 'error' && el.classList.contains('error')) el.style.display = 'block';
                else el.style.display = 'none';
            });
        }

        // Matrix background
        const c = document.getElementById("matrix");
        const ctx = c.getContext("2d");
        c.height = window.innerHeight;
        c.width = window.innerWidth;
        const chars = "01";
        const fontSize = 14;
        const columns = c.width / fontSize;
        const drops = Array(Math.floor(columns)).fill(1);

        function draw() {
            ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
            ctx.fillRect(0, 0, c.width, c.height);
            ctx.fillStyle = "#0F0";
            ctx.font = fontSize + "px Courier";
            for (let i = 0; i < drops.length; i++) {
                const text = chars.charAt(Math.floor(Math.random() * chars.length));
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                if (drops[i] * fontSize > c.height && Math.random() > 0.975)
                    drops[i] = 0;
                drops[i]++;
            }
        }
        setInterval(draw, 33);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/logs')
def logs():
    if not os.path.exists("alerts.log"):
        return "<div class='info'>No alerts.log found — waiting for packets...</div>"

    with open("alerts.log", "r") as f:
        lines = f.readlines()[-60:]

    output = ""
    for line in lines:
        line = line.strip()
        # Clean up Python-style list formatting
        line = line.replace("[", "").replace("]", "").replace("'", "")

        if "Attack" in line or "[ALERT]" in line or "Detected" in line:
            output += f"<div class='alert'>🚨 {line}</div>"
        elif "Normal" in line:
            output += f"<div class='info'>🟦 {line}</div>"
        elif "Error" in line:
            output += f"<div class='error'>⚠️ {line}</div>"
        else:
            output += f"<div class='info'>{line}</div>"

    return output


if __name__ == "__main__":
    print("🌐 Starting Cyber Dashboard on http://localhost:5050")
    app.run(host="0.0.0.0", port=5050)

