require('dotenv').config();
const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());

app.get('/mapskey', (req, res) => {
    res.json({ key: process.env.AZURE_MAPS_KEY });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});