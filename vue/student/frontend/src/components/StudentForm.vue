<template>
  <div>
    <input v-model="name" placeholder="Name">
    <input v-model="age" type="number" placeholder="Age">
    <button @click="addStudent">Add</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return { name: '', age: '' }
  },
  methods: {
    async addStudent() {
      const token = localStorage.getItem('token')
      await axios.post('http://localhost:3000/students', {
        name: this.name,
        age: this.age
      }, {
        headers: { Authorization: `Bearer ${token}` }
      })
      this.name = ''
      this.age = ''
      this.$emit('student-added')
    }
  }
}
</script>