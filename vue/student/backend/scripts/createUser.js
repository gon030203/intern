const bcrypt = require('bcrypt');
const db = require('../db');

const username = 'admin'; // đổi thành tên mong muốn
const password = '123456'; // đổi thành mật khẩu mong muốn
const role = 'admin'; // hoặc 'user'

bcrypt.hash(password, 10, (err, hash) => {
  if (err) throw err;
  db.query('INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
    [username, hash, role],
    (err, result) => {
      if (err) throw err;
      console.log(`✅ User "${username}" (${role}) created!`);
      process.exit();
    }
  );
});
