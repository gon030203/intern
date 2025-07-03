<script>
export default {
    data() {
        return {
            message: "Hello World!",
            counter: {
                count: 0
            },
            text: '',
            awesome: true
        };
    },
        methods: {
            increment() {
                this.counter.count ++
            },
            toggle() {
                this.awesome = !this.awesome
            }
    }
}
</script>

<template>
    <h1 class="message">{{ message }}</h1>
    <br>
  
    <button @click="increment">Count is: {{ counter.count }}</button>
    <br>
  
    <input v-model="text" placeholder="Type here">
    <p>{{ text }}</p>
    <br>
  
    <button @click="toggle">Toggle</button>
    <br>
  
    <h1 v-if="awesome">Vue is awesome</h1>
    <h1 v-else>Oh no</h1>
</template>

<style>
.message {
    color: red;
}
</style>
