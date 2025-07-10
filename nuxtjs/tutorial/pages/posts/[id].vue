<script setup>
const { data: posts, pending, error } = await useFetch('/api/posts')
</script>

<template>
  <div v-if="pending">Đang tải...</div>
  <div v-else>
    <AppCard v-for="post in posts" :key="post.id">
      <h3>{{ post.title }}</h3>
      <NuxtLink :to="`/posts/${post.id}`">Xem chi tiết</NuxtLink>
    </AppCard>
  </div>
</template>
