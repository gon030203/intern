<template>
  <div class="login-container">
    <input v-model="username" placeholder="Username">
    <input v-model="password" type="password" placeholder="Password">
    <button @click="login">Login</button>
  </div>
</template>

<script>
import axios from 'axios'
import '../assets/login.css'
export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async login() {
      try {
        const res = await axios.post('http://localhost:3000/auth/login', {
          username: this.username,
          password: this.password
        })
        localStorage.setItem('token', res.data.token)
        localStorage.setItem('role', res.data.role)
        this.$router.push('/dashboard')
      } catch {
        alert('Login failed')
      }
    }
  }
}
</script>
