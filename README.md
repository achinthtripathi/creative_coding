# 🎨 Creative Visual Coding App

A full-stack application that generates beautiful, animated visuals using AI-powered p5.js code generation. Transform your ideas into stunning motion graphics with just a text description!

## ✨ Features

- **AI-Powered Generation**: Uses GPT-4o to create custom p5.js visual code
- **Real-time Visuals**: Generate up to 20-second animated visuals
- **Interactive Gallery**: Browse and view all your generated creations
- **Modern UI**: Clean, responsive React frontend with beautiful animations
- **Local Storage**: SQLite database for storing all your visual creations
- **Instant Preview**: See your generated visuals immediately in the browser

## 🛠 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Python 3.11** - Programming language
- **Docker** - Containerization
- **GPT-4o** - OpenAI for visual code generation
- **SQLite** - Local database storage

### Frontend
- **TypeScript** - Type-safe JavaScript
- **React 18** - UI framework
- **p5.js** - Creative coding library for visuals
- **CSS3** - Modern styling with gradients and animations

## 📋 Prerequisites

- Docker and Docker Compose installed
- OpenAI API key

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd creative_coding
   ```

2. **Set up environment variables**
   ```bash
   cp env.example .env
   ```
   
   Edit `.env` file with your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Run the setup script**
   ```bash
   ./setup.sh
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - API Documentation: http://localhost:8000/docs

## 📖 Manual Setup

If you prefer to set up manually:

1. **Install dependencies and start services**
   ```bash
   docker-compose up --build
   ```

2. **Stop the application**
   ```bash
   docker-compose down
   ```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

### Getting API Keys

1. **OpenAI API Key**:
   - Visit [OpenAI Platform](https://platform.openai.com/api-keys)
   - Create a new API key
   - Add billing information (required for GPT-4o)

## 📱 Usage

### 1. Create Visual
- Navigate to the "Create Visual" tab
- Describe your visual idea in the text area
- Click "Generate Visual" to start the AI-powered creation
- Wait for the generation to complete

### 2. View Results
- Your generated visual will appear in an interactive preview
- The p5.js animation will run directly in the browser
- Visuals can be up to 20 seconds long

### 3. Browse Gallery
- Switch to the "Gallery" tab to see all your creations
- Click "View Visual" to replay any previous generation
- All visuals are saved locally for future access

## 🎯 Example Prompts

Try these creative prompts to get started:

- "A flowing river with colorful fish swimming in circles"
- "A cosmic dance of particles forming constellations"
- "A growing tree with falling leaves in autumn colors"
- "A digital rain effect with glowing green characters"
- "A sunset over mountains with animated clouds"
- "A geometric pattern that morphs and transforms"
- "A flock of birds flying in formation across the sky"
- "A kaleidoscope of rotating geometric shapes"

## 🏗 Project Structure

```
├── backend/                 # FastAPI backend
│   ├── main.py             # Main application file
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile         # Backend container config
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── App.tsx        # Main app component
│   │   └── index.tsx      # Entry point
│   ├── package.json       # Node.js dependencies
│   └── Dockerfile         # Frontend container config
├── data/                   # SQLite database files (created automatically)
├── docker-compose.yml      # Service orchestration
├── setup.sh               # Quick setup script
├── env.example            # Environment variables template
└── README.md              # This file
```

## 🔍 API Endpoints

- `POST /generate-visual` - Generate visual from user input
- `GET /visuals` - Get all generated visuals
- `GET /visual/{visual_id}` - Get specific visual by ID
- `GET /health` - Health check endpoint
- `WS /ws/{client_id}` - WebSocket for real-time updates

## 🎨 How It Works

1. **User Input**: User describes their visual idea in natural language
2. **AI Processing**: GPT-4o analyzes the description and generates p5.js code
3. **Code Generation**: Complete HTML file with embedded p5.js animation
4. **Instant Preview**: Visual runs immediately in the browser
5. **Storage**: Visual is saved to local database for future access

## 🐛 Troubleshooting

### Common Issues

1. **Docker not running**
   ```bash
   docker --version
   docker-compose --version
   ```

2. **Port conflicts**
   - Ensure ports 3000 and 8000 are available
   - Or modify `docker-compose.yml` to use different ports

3. **API key issues**
   - Verify your OpenAI API key is correct
   - Ensure you have billing set up for GPT-4o access

4. **Database issues**
   - SQLite database is created automatically in the `data/` directory
   - If you encounter database errors, delete the `data/` folder and restart

### Logs

View application logs:
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend
```

## 🔒 Security Notes

- This is a PoC application
- No authentication or user management
- API keys are stored in environment variables
- Data is stored locally in SQLite
- For production use, implement proper security measures

## 🚀 Future Enhancements

- **User Authentication**: Multi-user support with user accounts
- **Visual Categories**: Organize visuals by themes and styles
- **Export Options**: Download visuals as GIF, MP4, or code files
- **Collaborative Features**: Share and remix visuals
- **Advanced Controls**: Customize animation parameters
- **Real-time Collaboration**: Multiple users working on the same visual

## 📝 License

This project is for demonstration purposes only.

## 🤝 Contributing

This is a proof-of-concept application. Feel free to fork and modify for your needs.

---

**Happy Creative Coding! 🎨✨** 