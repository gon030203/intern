const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

app.use('/auth', require('./routes/auth'));
app.use('/students', require('./routes/students'));

app.listen(3000, () => console.log('Backend running on http://localhost:3000'));