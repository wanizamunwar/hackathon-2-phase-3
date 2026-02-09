# Quickstart: Todo Full-Stack Web Application

This guide covers setting up and running the Phase II full-stack todo application.

## Prerequisites

- Python 3.12+
- Node.js 18+ and npm
- A Neon Serverless PostgreSQL account and database (https://neon.tech)
- Git (for branch management)

## 1. Set Up Neon Database

1. **Create a Neon account** at https://neon.tech (free tier available)
2. **Create a new project** (e.g., "hackathon-todo")
3. **Copy the connection string** from the Neon dashboard — it looks like:
   ```
   postgresql://username:password@ep-xxxxx.us-east-2.aws.neon.tech/dbname?sslmode=require
   ```

## 2. Set Up Environment Variables

1. **Create `.env` file in `backend/`**:
   ```
   DATABASE_URL=postgresql://username:password@ep-xxxxx.us-east-2.aws.neon.tech/dbname?sslmode=require
   BETTER_AUTH_SECRET=your-shared-secret-key-here
   ```

2. **Create `.env.local` file in `frontend/`**:
   ```
   BETTER_AUTH_SECRET=your-shared-secret-key-here
   NEXT_PUBLIC_API_URL=http://localhost:8000
   BETTER_AUTH_URL=http://localhost:3000
   ```

   > The `BETTER_AUTH_SECRET` must be the same in both services.

## 3. Set Up Backend

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**:
   ```bash
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the backend**:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

   The API will be available at `http://localhost:8000`. Swagger docs at `http://localhost:8000/docs`.

## 4. Set Up Frontend

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run the frontend**:
   ```bash
   npm run dev
   ```

   The app will be available at `http://localhost:3000`.

## 5. Using the Application

1. **Sign Up**: Navigate to `http://localhost:3000/signup` and create an account
2. **Sign In**: Navigate to `http://localhost:3000/signin` and log in
3. **Dashboard**: After signin, you'll see the task dashboard where you can:
   - Add new tasks with title, description, priority, and tags
   - View all your tasks
   - Edit task details
   - Delete tasks
   - Toggle task completion
   - Search, filter, and sort tasks

## 6. Running Tests

### Backend Tests
```bash
cd backend
pip install pytest
pytest tests/
```

## API Documentation

Once the backend is running, visit `http://localhost:8000/docs` for interactive Swagger API documentation.
