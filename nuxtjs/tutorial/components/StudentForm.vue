<template>
  <div>
    <input v-model="name" placeholder="Name" />
    <input v-model="age" type="number" placeholder="Age" />
    <button @click="addStudent">Add</button>
  </div>
</template>

<script setup>
import axios from 'axios'
const emit = defineEmits(['student-added'])
const name = ref('')
const age = ref('')

const addStudent = async () => {
  const token = localStorage.getItem('token')
  await axios.post('http://localhost:8000/api/students/', {
    name: name.value,
    age: age.value
  }, {
    headers: { Authorization: `Bearer ${token}` }
  })
  name.value = ''
  age.value = ''
  emit('student-added')
}
</script>
