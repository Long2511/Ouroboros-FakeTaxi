require('dotenv').config();
const express = require('express');
const cors = require('cors');
const app = express();
let fetch;

import('node-fetch').then(nodeFetch => {
    fetch = nodeFetch;
});

app.use(cors());


app.get('/gps', async (req, res) => {
    const response = await fetch('http://localhost:8888/gps');
    const data = await response.json();
    res.json(data);
});

app.get('/mapskey', (req, res) => {
    res.json({ key: process.env.AZURE_MAPS_KEY });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});