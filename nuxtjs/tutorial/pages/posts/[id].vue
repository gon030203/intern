<script setup>
const route = useRoute()
const { data: post, pending, error } = await useFetch(`/api/posts/${route.params.id}`)
</script>

<template>
  <div v-if="pending">Đang tải...</div>
  <div v-else-if="error">Lỗi: {{ error.message }}</div>
  <div v-else>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
  </div>
</template>
