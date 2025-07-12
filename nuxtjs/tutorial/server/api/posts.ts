// server/api/posts.ts
import db from '~/server/utils/db'

export default defineEventHandler(async () => {
  const [rows] = await db.query('SELECT * FROM posts ORDER BY created_at DESC')
  return rows
})
