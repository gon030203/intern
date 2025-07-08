<template>
  <ul>
    <li v-for="student in students" :key="student.id">
      {{ student.name }} - {{ student.age }}
      <button v-if="isAdmin" @click="removeStudent(student.id)">Delete</button>
    </li>
  </ul>
</template>

<script>
import axios from 'axios'
export default {
  props: ['students', 'isAdmin'],
  methods: {
    async removeStudent(id) {
      const token = localStorage.getItem('token')
      await axios.delete(`http://localhost:8000/api/students/${id}/`, {
        headers: { Authorization: `Bearer ${token}` }
      })
      this.$emit('student-deleted')
    }
  }
}
</script>