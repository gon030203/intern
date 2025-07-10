<template>
  <ul>
    <li v-for="student in students" :key="student.id">
      {{ student.name }} - {{ student.age }}
      <button v-if="isAdmin" @click="removeStudent(student.id)">Xoá</button>
    </li>
  </ul>
</template>

<script setup>
import axios from 'axios'
const props = defineProps(['students', 'isAdmin'])
const emit = defineEmits(['student-deleted'])

const removeStudent = async (id) => {
  const token = localStorage.getItem('token')
  await axios.delete(`http://localhost:8000/api/students/${id}/`, {
    headers: { Authorization: `Bearer ${token}` }
  })
  emit('student-deleted')
}
</script>
