# Google GenAI Import Utility

## Prerequisites

### 1. Python Setup
- Python 3.12+ installed
- Virtual environment recommended

### 2. Google Cloud Project
1. Create a Google Cloud project
2. Enable Vertex AI API
3. Set up authentication

### 3. Authentication Methods

#### Option A: Application Default Credentials
```bash
gcloud auth application-default login
```

#### Option B: Service Account
1. Create service account in Google Cloud Console
2. Download JSON key file
3. Set environment variable:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
```

### 4. Library Installation
```bash
pip install google-generativeai
```

## Configuration

1. Update project details in `genai_import_utility.py`:
```python
client = genai.Client(
    vertexai=True,
    project="YOUR_PROJECT_ID",
    location="YOUR_REGION"  # e.g., "us-central1"
)
```

## Running the Script
```bash
python scripts/genai_import_utility.py
```

## Troubleshooting
- Ensure all dependencies are installed
- Verify Google Cloud project credentials
- Check network connectivity
- Confirm Vertex AI API is enabled

## Error Handling
The script includes basic error catching. If issues persist, check:
- API permissions
- Network configuration
- Authentication status

## Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create pull request

## License
[Specify your license]
