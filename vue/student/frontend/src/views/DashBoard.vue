<template>
  <div class="dashboard">
    <h2>Dashboard</h2>
    <button class="logout-button" @click="logout">Logout</button>
    <StudentForm v-if="role === 'admin'" @student-added="loadStudents" />
    <StudentList
      :students="students"
      :is-admin="role === 'admin'"
      @student-updated="loadStudents"
      @student-deleted="loadStudents"
    />
  </div>
</template>

<script>
import StudentForm from '../components/StudentForm.vue'
import StudentList from '../components/StudentList.vue'
import axios from 'axios'
import '../assets/dashboard.css'

export default {
  components: { StudentForm, StudentList },
  data() {
    return {
      students: [],
      role: localStorage.getItem('role')
    }
  },
  methods: {
    async loadStudents() {
      const token = localStorage.getItem('token')
      const res = await axios.get('http://localhost:8000/api/students/', {
        headers: { Authorization: `Bearer ${token}` }
      })
      this.students = res.data
    },
    logout() {
      localStorage.removeItem('token')
      localStorage.removeItem('role')
      this.$router.push('/')
    }
  },
  mounted() {
    this.loadStudents()
  }
}
</script>
