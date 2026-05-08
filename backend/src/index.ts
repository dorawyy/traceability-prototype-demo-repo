import dotenv from 'dotenv';

import { createApp } from './app';
import { connectDB } from './database';

dotenv.config();

const app = createApp();
const PORT = process.env.PORT ?? 3000;

connectDB();
app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
});
