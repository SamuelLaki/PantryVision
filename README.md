# PantryVision 🚀 🌮

A smart web application that generates recipes using AI-powered food recognition and recipe generation. Simply upload a photo of your ingredients, and PantryVision will identify the food items and create delicious recipes for you!

## ✨ Features

- **AI-Powered Food Recognition**: Uses LogMeal API to identify ingredients from uploaded photos
- **Smart Recipe Generation**: Leverages Google's Generative AI to create detailed recipes using only the detected ingredients
- **User-Friendly Interface**: Clean, responsive web interface built with Django and Bootstrap
- **Real-time Processing**: Instant ingredient detection and recipe generation
- **Celebration Effects**: Fun confetti animation when recipes are generated

## 🛠️ Technology Stack

- **Backend**: Django 4.2.3
- **Frontend**: HTML, CSS, Bootstrap 5
- **AI Services**: 
  - LogMeal API (food recognition)
  - Google Generative AI (recipe generation)
- **Database**: SQLite3
- **Media Storage**: Local file system

## 📋 Prerequisites

Before running this application, you'll need:

1. **Python 3.8+**
2. **Django 4.2.3**
3. **LogMeal API Token** - Get your token from [LogMeal](https://logmeal.es/)
4. **Google Generative AI API Key** - Get your key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd PantryVision
```

### 2. Install Dependencies
```bash
pip install django requests google-generativeai pillow
```

### 3. Configure API Keys
Update the API keys in `myapp/views.py`:
```python
# Replace with your actual API keys
api_user_token = 'YOUR_LOGMEAL_API_TOKEN'
palm.configure(api_key="YOUR_GOOGLE_AI_API_KEY")
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📱 How to Use

1. **Upload Image**: Navigate to the home page and click "Choose file" to upload a photo of your ingredients
2. **Process Image**: Click "Upload" to send the image for processing
3. **View Results**: The system will automatically detect ingredients and generate recipes
4. **Get Recipes**: View the detailed recipe with ingredients and cooking instructions

## 🏗️ Project Structure

```
PantryVision/
├── myapp/                    # Main Django application
│   ├── models.py            # Database models
│   ├── views.py             # Business logic and API integration
│   ├── forms.py             # Form definitions
│   ├── urls.py              # URL routing
│   └── templates/           # HTML templates
│       ├── upload.html      # Image upload page
│       ├── recipes.html     # Recipe display page
│       └── success.html     # Success confirmation page
├── pantryvisionwebapp/      # Django project settings
├── media/                   # Uploaded images storage
├── food_detect_test/        # Testing scripts
└── manage.py               # Django management script
```

## 🔧 Configuration

### Environment Variables
For production deployment, consider using environment variables for API keys:

```python
import os
api_user_token = os.environ.get('LOGMEAL_API_TOKEN')
google_api_key = os.environ.get('GOOGLE_AI_API_KEY')
```

### Media Settings
The application is configured to store uploaded images in the `media/images/` directory. Make sure this directory exists and has proper write permissions.

## 🧪 Testing

The project includes a test script in `food_detect_test/food_test_1.py` that demonstrates the core functionality without the web interface.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [LogMeal](https://logmeal.es/) for food recognition API
- [Google Generative AI](https://ai.google.dev/) for recipe generation
- [Django](https://www.djangoproject.com/) for the web framework
- [Bootstrap](https://getbootstrap.com/) for the UI components

## 📞 Support

If you encounter any issues or have questions, please open an issue on the repository.

---

**Note**: This is a demo application. For production use, ensure proper security measures, error handling, and API key management.


