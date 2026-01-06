# Quick Start Guide

## 🚀 Start in 5 Minutes

### Option 1: Docker (Recommended)

```bash
# 1. Clone/navigate to project
cd careervr

# 2. Create .env file
cp backend/.env.example .env
# Edit .env and add your DIFY_API_KEY

# 3. Start everything
docker-compose up

# 4. Open browser
# Frontend: http://localhost
# Backend: http://localhost:8000/health
```

### Option 2: Local Python Setup

```bash
# 1. Create virtual environment (if not already done)
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
cd backend
pip install -r requirements.txt

# 3. Create .env file
cp .env.example ../.env
# Edit ../.env and add your DIFY_API_KEY

# 4. Start backend (from project root)
cd ..
source venv/bin/activate
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

# 5. Open frontend (in another terminal)
# Terminal 2:
source venv/bin/activate
python -m http.server 8001
# Visit http://localhost:8001/index1.html
```

### Option 3: One-Line Deploy Script

```bash
./deploy.sh
# Then run backend from instructions at the end
```

---

## 🔑 Get Your DIFY API Key

1. Go to https://dify.ai
2. Sign up or log in
3. Create a Knowledge Base or Workflow for career guidance
4. Copy API key from Settings → API
5. Add to `.env`:
```
DIFY_API_KEY=app-xxxxxxxxxxxxx
```

---

## ✅ Verify Setup

```bash
# Activate virtual environment first
source venv/bin/activate

# Test backend is running
curl http://localhost:8000/health

# Should return:
# {"status":"ok","message":"CareerVR backend is running"}

# If port 8000 is not accessible, check if server is running in another terminal
# If needed, use a different port (use dot notation, not slash):
# uvicorn backend.main:app --reload --port 8001
```

---

## 🧪 Test Features

1. **Frontend**: Open `index1.html`
2. **Fill student info**: Name, Class, School
3. **Answer 50 questions**: 1=Strongly disagree, 5=Strongly agree
4. **Submit**: See RIASEC results
5. **Chat with AI**: Ask about career paths
6. **Dashboard**: View statistics

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'fastapi'` | Activate venv first: `source venv/bin/activate` then `pip install -r requirements.txt` |
| `command not found: pip` | Activate venv: `source venv/bin/activate` |
| `CORS Error` | Make sure backend is running on `http://localhost:8000` |
| `404 Not Found` | Check API_URL in index.html matches backend location |
| `500 Server Error` | Check DIFY_API_KEY is set in .env file |
| Port 8000 already in use | Use different port: `uvicorn backend.main:app --port 8001` (use dot, not slash) |
| Backend won't start | Check for syntax errors: `cd backend && python3 -c "from main import app"` |
| Python 3.13 issues | Make sure all dependencies installed: `pip install -r requirements.txt` |

---

## 📁 Project Structure

```
careervr/
├── index.html          ← Simple RIASEC test interface
├── index1.html         ← Full-featured dashboard interface
├── backend/
│   ├── main.py         ← FastAPI backend
│   └── requirements.txt ← Python dependencies
├── docker-compose.yml  ← Full stack definition
├── Dockerfile          ← Backend container
├── nginx.conf          ← Web server config
└── deploy.sh           ← Deployment script
```

---

## 🎯 Common Tasks

### Deploy to Production

```bash
# With Docker
docker-compose up -d

# With traditional server
./deploy.sh
cd backend/venv/bin
./gunicorn -w 4 -b 0.0.0.0:8000 'main:app'
```

### View Logs

```bash
# Docker logs
docker-compose logs backend

# Python logs
tail -f /var/log/careervr.log
```

### Reset Student Data

```bash
# Clear browser LocalStorage (from browser console)
localStorage.clear()

# Or via Dashboard UI: Click "Xoá dữ liệu (local)"
```

---

## 📚 Next Steps

- Read [README.md](README.md) for full documentation
- Check [CHANGELOG.md](CHANGELOG.md) for recent updates
- Review [IMPROVEMENTS.md](IMPROVEMENTS.md) for technical details
- See [TESTING.md](TESTING.md) for test suite

---

## 💡 Tips

- Use `index1.html` for best UX (has tabs, progress tracking)
- Keep DIFY_API_KEY in `.env`, never commit it
- Data is stored locally in browser - encourage students to take test on same device
- Backend can be any language - just implement `/run-riasec` endpoint

---

## 🆘 Get Help

Check the full documentation:
```bash
# Main README
cat README.md

# Detailed improvements
cat IMPROVEMENTS.md

# Version history
cat CHANGELOG.md
```

Or test the API directly:
```bash
curl -X POST http://localhost:8000/run-riasec \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test",
    "class": "10A",
    "school": "THPT",
    "answers_json": [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
  }'
```

Happy coding! 🎓
