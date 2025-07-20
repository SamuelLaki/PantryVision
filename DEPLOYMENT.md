# PantryVision Deployment Guide

## Deploying to Vercel

### Prerequisites
1. Vercel account (sign up at vercel.com)
2. API keys for:
   - LogMeal API (food detection) - Get from: https://logmeal.es/
   - Google Palm API (recipe generation) - Get from: https://makersuite.google.com/app/apikey

### Deployment Steps

1. **Install Vercel CLI** (if not already installed):
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy the application**:
   ```bash
   vercel
   ```

4. **Set Environment Variables** in Vercel dashboard or via CLI:
   ```bash
   vercel env add LOG_MEAL_TOKEN
   vercel env add PALM_API_KEY
   vercel env add DJANGO_SECRET_KEY
   ```

### Required Environment Variables

- `LOG_MEAL_TOKEN`: Your LogMeal API token for food detection
- `PALM_API_KEY`: Your Google Palm API key for recipe generation  
- `DJANGO_SECRET_KEY`: A secure secret key for Django (generate a new one for production)

### Important Notes

1. **Database**: The app uses an in-memory SQLite database for serverless deployment. For persistent data, consider using a cloud database like PostgreSQL on Vercel or AWS RDS.

2. **File Uploads**: Media files uploaded to Vercel are temporary and will be lost after function execution. For persistent file storage, consider using cloud storage like AWS S3 or Cloudinary.

3. **Function Timeout**: Vercel has execution time limits for serverless functions. API calls to LogMeal and Palm API should complete within this limit.

### Local Development

To run locally with production settings:
```bash
export DJANGO_SETTINGS_MODULE=pantryvisionwebapp.production_settings
python manage.py runserver
```

### Troubleshooting

- If you get import errors, make sure all dependencies are in requirements.txt
- If static files don't load, run `python manage.py collectstatic` locally to test
- Check Vercel function logs in the dashboard for runtime errors 