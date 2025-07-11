// server/api/posts/[id].ts
import db from '~/server/utils/db'
import type { RowDataPacket } from 'mysql2'

export default defineEventHandler(async (event) => {
  const id = event.context.params?.id

  const [rows] = await db.query<RowDataPacket[]>('SELECT * FROM posts WHERE id = ?', [id])

  if (!rows || rows.length === 0) {
    throw createError({ statusCode: 404, message: 'Post not found' })
  }

  return rows[0]
})
