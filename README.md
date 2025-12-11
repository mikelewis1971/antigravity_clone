# Antigravity Local

A local agentic AI coding assistant that mimics Google Antigravity's features using your own GGUF models.

## 🚀 Features

- **Agentic Workflows**: Autonomous planning, execution, and verification modes
- **Local LLM**: Runs completely offline using llama.cpp with GGUF models
- **Tool Calling**: File operations, command execution, code search, web browsing
- **Modern Web UI**: Beautiful dark mode interface with real-time updates
- **Fast & Private**: All processing happens locally on your machine

## 📋 Requirements

- **Python**: 3.9 or higher
- **RAM**: 8GB minimum (16GB recommended for 8B models)
- **GPU**: Optional but recommended for faster inference
- **GGUF Model**: Qwen3-8B-Q4_K_M (or any compatible model)

## 🛠️ Installation

### 1. Run Setup

```bash
python setup.py
```

This will:
- Check Python version
- Verify model file exists
- Install all dependencies
- Set up directories

### 2. Configure Model Path

Edit `config.yaml` and update the model path if needed:

```yaml
llm:
  model_path: "G:/Jan/llamacpp/models/lmstudio-community/Qwen3-8B-GGUF/Qwen3-8B-Q4_K_M.gguf"
```

### 3. Launch

**Windows:**
```bash
run.bat
```

**Command Line:**
```bash
cd backend
python api.py
```

The web interface will open at: http://localhost:8000

## 🎯 Usage

### Basic Chat
Simply type your message and press Enter. The AI will respond using the local LLM.

### File Operations
```
"Create a Python file called hello.py that prints Hello World"
"Read the contents of config.yaml"
"Edit setup.py to add error handling"
```

### Code Development
```
"Create a REST API using FastAPI for a todo app"
"Add unit tests for the API endpoints"
"Refactor the code to use async/await"
```

### Command Execution
```
"What files are in the current directory?"
"Run the unit tests"
"Check if Python is installed"
```

## ⚙️ Configuration

### config.yaml Options

**LLM Settings:**
- `model_path`: Path to your GGUF model file
- `context_size`: Context window (default: 8192)
- `temperature`: Randomness (0.0-1.0, default: 0.7)
- `gpu_layers`: Number of layers to offload to GPU (0 for CPU only)

**Tool Permissions:**
- `allow_file_read`: Enable reading files (default: true)
- `allow_file_write`: Enable writing files (default: true)
- `allow_file_delete`: Enable deleting files (default: false)
- `allow_command_execution`: Enable command execution (default: true)

**Server Settings:**
- `host`: Server host (default: 127.0.0.1)
- `port`: Server port (default: 8000)

## 🔧 Available Tools

1. **read_file** - Read file contents
2. **write_file** - Create or overwrite files
3. **edit_file** - Edit specific parts of files
4. **list_directory** - List directory contents
5. **search_files** - Find files by pattern
6. **execute_command** - Run PowerShell commands
7. **fetch_url** - Fetch web content

## 🏗️ Architecture

```
antigravity_local/
├── backend/
│   ├── api.py           # FastAPI server
│   ├── agent.py         # Agentic orchestration
│   ├── llm_server.py    # LLM integration
│   ├── tools.py         # Tool implementations
│   └── requirements.txt # Python dependencies
├── frontend/
│   ├── index.html       # Web interface
│   ├── styles.css       # Styling
│   └── app.js           # Frontend logic
├── config.yaml          # Configuration
├── setup.py             # Setup script
└── run.bat              # Launcher
```

## 🎨 Customization

### Using a Different Model

1. Update `config.yaml` with your model path
2. Adjust `context_size` based on model capabilities
3. Tune `gpu_layers` for optimal performance

### Adjusting Tool Permissions

Edit `config.yaml` to enable/disable specific tools based on your security requirements.

### Modifying the System Prompt

Edit the `_load_system_prompt()` method in `backend/agent.py` to customize the AI's behavior.

## 🐛 Troubleshooting

### Model Loading Issues
- Verify the model path in config.yaml is correct
- Ensure you have enough RAM (8GB minimum)
- Try reducing `gpu_layers` if using GPU

### Slow Performance
- Reduce `context_size` in config.yaml
- Use a smaller/quantized model (Q4_K_M or Q2_K)
- Increase `gpu_layers` if you have a GPU

### Connection Errors
- Check if port 8000 is already in use
- Try changing the port in config.yaml
- Ensure firewall isn't blocking connections

## 📝 License

This project is open source and available for personal use.

## 🙏 Acknowledgments

- Inspired by Google Antigravity
- Built with llama.cpp and FastAPI
- Uses Qwen3-8B model for local inference
