# VAL_RPC

VAL_RPC is a Python-based Discord Rich Presence tool for [Valorant](https://playvalorant.com).  
It shows your **peak rank** and activity (e.g., coaching or playing) as your Discord status when Valorant is running.

![Discord RPC Example](https://i.imgur.com/3hUzrAi.png) <!-- Optional placeholder image -->

---

## Features

- Auto-detects if Valorant is running
- Displays peak rank as small image icon
- Shows status like "Coaching Valorant" (which you can customize)
- Integrates with Discord using [pypresence](https://pypi.org/project/pypresence/)
- Fetches player data using the [HenrikDev Valorant API](https://dash.valorant-api.com/)
- Includes a join Discord button in your presence

---

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourname/VAL_RPC.git
cd VAL_RPC
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Activate:
# On Windows:
.env\Scriptsctivate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Setup

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application and note your **Client ID**
3. Add Rich Presence assets (e.g., `valorant-logo`, rank icons like `gold-3.png`, etc.)
4. Create a `.env` file in the root folder:

```env
API_KEY=your_henrikdev_api_key
VALUSER=your_username
TAG=your_tag
```

5. Open `main.py` and set your `CLIENT_ID` with your Discord app ID.

---

## ▶️ Running the App

Once everything is configured:

```bash
python main.py
```

VAL_RPC will automatically update your Discord status while Valorant is running.

---

## 🛠 File Structure

```
VAL_RPC/
├── api/
│   └── api.py         # Rank fetch logic
├── main.py            # Main loop + Rich Presence logic
├── requirements.txt
└── .env               # Your secrets (not committed)
```

---

## 📸 Example Presence

> Shows your peak rank and coaching status

- Large icon: Valorant logo
- Small icon: Your peak rank
- Button: "Join Discord"

---

## 📜 License

MIT License. Feel free to fork or modify.

---

## 🙋 Author

**marce**  
Discord: `marce`  
[Discord Server](https://discord.gg/Bp5cFGW8wg)