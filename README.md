# calc-be

This is the backend for the AI Calculator project. It provides API endpoints to perform various calculations and supports integration with the frontend application.

## Features

- RESTful API for calculator operations
- Built with Node.js and Express
- Easy integration with frontend
- Modular and extensible codebase

## Getting Started

cd ~/Desktop/AI\ Calculator/calc-be
source venv/bin/activate
uvicorn main:app --reload


1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ansul8012/Calci_backend
   cd calc-be
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the server:**
   ```bash
   npm start
   ```
   Or for development with hot-reloading:
   ```bash
   npm run dev
   ```

4. **API will be available at:**  
   ```
   http://localhost:3000
   ```
   (Change the port in `.env` or `config` if needed.)

## API Endpoints

- `POST /calculate` – Perform a calculation (see API docs for details)

## Frontend Repository

Frontend code is available here: [calc-fe GitHub Repository](https://github.com/Ansul8012/Ai_calci) <!-- Replace with your actual frontend repo link -->

## License

MIT

---

For more information, see the project documentation or