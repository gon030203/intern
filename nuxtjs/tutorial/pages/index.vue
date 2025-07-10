<template>
  <div>
    <AppCard>
      <NuxtLink to="/about" class="global-title">Giới thiệu</NuxtLink>
      <p class="title">Tôi tên là Hồ Nguyên Khoa.</p>
      <FancyBox />
      <br />
      <NuxtLink to="/posts/1">Xem bài viết 1</NuxtLink><br />
      <NuxtLink to="/posts/2">Xem bài viết 2</NuxtLink><br />
      <NuxtLink to="/posts/3">Xem bài viết 3</NuxtLink><br />
      <NuxtLink to="/login">Vào trang quản lý học sinh</NuxtLink><br />
      <NuxtLink to="/counter">Trang đếm</NuxtLink>
    </AppCard>
  </div>
</template>

<script setup>
import '~/assets/scss/colors.scss'

definePageMeta({
  title: 'Trang chủ - Nuxt App',
  meta: [
    { name: 'description', content: 'Đây là trang chủ của website Nuxt' }
  ]
})
</script>
