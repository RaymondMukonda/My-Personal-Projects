import express from 'express';
import {config} from 'dotenv';
import { connectDB, disconnectDB } from './config/db.js';
import movieRoutes from './routes/movieRoutes.js';


config();
connectDB();

const app = express();

//API routes
app.use('/movies', movieRoutes);

const PORT = 5001;

app.listen(PORT, () => {
    console.log(`Server runinng on Port:`, PORT);
});

