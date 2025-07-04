const express = require('express');
const db = require('../db');
const { authMiddleware, requireRole } = require('../middleware/auth');
const router = express.Router();

router.get('/', authMiddleware, (req, res) => {
    db.query('SELECT * FROM students', (err, results) => {
        if (err) return res.status(500).json(err);
        res.json(results);
    });
});

router.post('/', authMiddleware, requireRole('admin'), (req, res) => {
    const { name, age } = req.body;
    db.query('INSERT INTO students (name, age) VALUES (?, ?)', [name, age], (err, result) => {
        if (err) return res.status(500).json(err);
        res.json({ id: result.insertId, name, age });
    });
});

router.put('/:id', authMiddleware, requireRole('admin'), (req, res) => {
    const { name, age } = req.body;
    db.query('UPDATE students SET name=?, age=? WHERE id=?', [name, age, req.params.id], (err) => {
        if (err) return res.status(500).json(err);
        res.sendStatus(200);
    });
});

router.delete('/:id', authMiddleware, requireRole('admin'), (req, res) => {
    db.query('DELETE FROM students WHERE id=?', [req.params.id], (err) => {
        if (err) return res.status(500).json(err);
        res.sendStatus(204);
    });
});

module.exports = router;