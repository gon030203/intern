<!-- layouts/orange.vue -->
<template>
  <div class="orange-layout">
    <!-- Phải có <slot /> để hiển thị nội dung trang -->
    <slot />
  </div>
</template>

<style scoped>
.orange-layout {
  padding: 2rem;
  background-color: orange;
  min-height: 100vh;
}
</style>
