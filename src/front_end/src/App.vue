<script setup>
import { onMounted } from 'vue';
import { RouterView, useRouter } from 'vue-router';

const router = useRouter();

onMounted(() => {
  // navigate the route after the component is mounted
  router.push({ path: '/Login' });
});
</script>

<template>
  <RouterView />
</template>

<style scoped>
body {
  font-family: 'Arial', sans-serif;
  margin: 0;
  padding: 0;
}

.router-view {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>
