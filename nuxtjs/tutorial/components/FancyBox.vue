<template>
  <div :class="[isActive ? $style.active : $style.inactive]">
    I am a Fancy Box 
  </div>
</template>

<script setup lang="ts">
const isActive = ref(true)
</script>

<style module>
.active {
  background: green;
  color: white;
  padding: 10px;
  border-radius: 8px;
}
.inactive {
  background: gray;
  color: black;
}
</style>
