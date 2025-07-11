// server/utils/db.ts
import mysql from 'mysql2/promise'

const db = mysql.createPool({
  host: '127.0.0.1',
  user: 'root',
  password: '03022003',
  database: 'student',
  port: 3307,
})

export default db
