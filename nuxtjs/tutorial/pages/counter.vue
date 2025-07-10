<script setup>
const counter = useState('counter', () => 0)
</script>

<template>
  <div>
    <h1>Bạn đã bấm: {{ counter }} lần</h1>
    <button @click="counter++">Tăng</button>
    <button @click="counter = 0">Reset</button>
  </div>
</template>
